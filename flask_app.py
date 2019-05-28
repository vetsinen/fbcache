""" flask server module for processing fb tokens """
from flask import Flask
from flask import render_template
import facebook
import sqlite3
from flask import g
import datetime

app = Flask(__name__)
userid = "143260170135375"  # ryan foster
DATABASE = 'events.db' #problem to get from pythonanywhere
#DATABASE = '/home/xtfkpi/mysite/events.db' #for pythonanywhere

@app.route('/events/')
def list_events(date=datetime.datetime.now().isoformat()[:10]):
    events = grab_events_for_date(date)
    return render_template('events.html',events = events)


@app.route('/token/')
def hello_login():
    return app.send_static_file('login.html')


@app.route('/token/<token>')
def token(token):
    process_events(token)
    return 'Hello token'

def grab_events_for_date(date):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name,time,place,description FROM events WHERE date = '{}' ORDER BY priority, time ;".format(date))
    return cursor.fetchall()


def process_events(token):
    graph = facebook.GraphAPI(access_token=token, version="3.1")
    rez = graph.get_all_connections(id=userid, connection_name='events')

    c = 0
    conn = get_db()
    cursor = conn.cursor()

    for event in rez:
        cursor.execute("SELECT EXISTS (SELECT id FROM events WHERE id = '{}' LIMIT 1);".format(event['id']))
        check = cursor.fetchall()[0][0]
        if check == 1:
            continue
        c += 1
        print(event)
        try:
            place = event['place']['name']
        except:
            place = ''
        date = event['start_time'][:10]
        time = event['start_time'][11:16]
        if event['rsvp_status'] == 'unsure':
            priority = 6
        else:
            priority = 1

        if 'end_time' in event.keys():
            delta = datetime.datetime.strptime(event['end_time'], "%Y-%m-%dT%H:%M:%S%z") - datetime.datetime.strptime(
                event['start_time'], "%Y-%m-%dT%H:%M:%S%z")
            if delta.days > 1:
                priority = 9

        description = event['description'].replace('"', '`').replace("'", "`")
        name = event['name'].replace('"', '`').replace("'", "`")
        place = place.replace('"', '`').replace("'", "`")
        sql = 'insert into events (id,name,date,time,priority,description,place,datetime) values ({},"{}","{}","{}",{},"{}","{}","{}")'. \
            format(event['id'], name, date, time, priority, description, place, event['start_time'])
        cursor.execute(sql)
        conn.commit()
        event['description'] = event['description'][:20]  # taking fragment for printing
        if c > 2000:
            break

    print('events ', c)
    conn.close()


if __name__ == '__main__':
    app.run()


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
