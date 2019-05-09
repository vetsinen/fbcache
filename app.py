""" flask server module for processing fb tokens """
from flask import Flask
import facebook
import sqlite3
from flask import g

app = Flask(__name__)
userid = "10156265228397361"
DATABASE = 'events.db'


@app.route('/')
def hello_world():
    return app.send_static_file('login.html')


@app.route('/token/<token>')
def token(token):
    process_events(token)
    return 'Hello token'


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
        description = event['description'].replace('"','`').replace("'","`")
        name = event['name'].replace('"','`').replace("'","`")
        place = place.replace('"','`').replace("'","`")
        sql = 'insert into events (id,name,date,time,priority,description,place,datetime) values ({},"{}","{}","{}",{},"{}","{}","{}")'.\
            format(event['id'], name , date, time, priority,description,place,event['start_time'])
        print(sql)
        cursor.execute(sql)
        conn.commit()
        if c>15:
            break


    conn.close()
    print(42)

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
