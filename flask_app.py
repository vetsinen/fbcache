""" flask server module for processing fb tokens """
from flask import Flask, render_template, redirect
import facebook
import sqlite3
from flask import g
import datetime
import os
from dou_grabber import check_dou_updates

app = Flask(__name__)
# userid = "143260170135375"  # ryan foster
# userid = "10156265228397361"  # vetal
LOCAL_RUN = True if os.getuid() == 1000 else False
if os.getuid() == 1000:  # localrun
    DATABASE = 'events.db'  # problem to get from pythonanywhere
if os.getuid() == 5604817:  # stupid way to define if we launched on server
    DATABASE = '/home/xtfkpi/mysite/events.db'  # for pythonanywhere

def remove_all_quotes(s):
    return s.replace('"','').replace("'","")

@app.route('/')
@app.route('/<date>')
@app.route('/all/<int:fullhouse>')
def list_events(date=None,fullhouse=0):
    today = datetime.datetime.now()
    if not LOCAL_RUN:
        today = today + datetime.timedelta(hours=4)
    tomorrow = (today + datetime.timedelta(days=1)).isoformat()[:10]
    today = date or today.isoformat()[:10]
    events = grab_events_for_date(today) if fullhouse !=1 else grab_allevents()
    return render_template('events.html', events=events,today=today, tomorrow=tomorrow)

def fullhouse():
    return render_template('events.html')

@app.route('/pull/')
def hello_login():
    return app.send_static_file('login.html')


@app.route('/up1/<eventid>')
def up1(eventid):
    conn = get_db()
    cursor = conn.cursor()
    sql = "update events set priority = priority  - 1 where id = '{}'".format(eventid)
    cursor.execute(sql)
    conn.commit()
    return ''


@app.route('/down1/<eventid>')
def down1(eventid):
    conn = get_db()
    cursor = conn.cursor()
    sql = "update events set priority = priority  + 1 where id = '{}'".format(eventid)
    cursor.execute(sql)
    conn.commit()
    return ''


@app.route('/token/<userid>/<token>')
def token(userid, token):
    process_events(userid, token)
    return redirect("/")


def grab_events_for_date(date):
    conn = get_db()
    cursor = conn.cursor()
    sql = "SELECT name,time,address,description,origin,place,latitude,longitude,id FROM events WHERE date <= '{}' AND enddate>='{}' ORDER BY priority, time ;".format(date, date)
    cursor.execute(sql)
    return cursor.fetchall()

def grab_allevents():
    conn = get_db()
    cursor = conn.cursor()
    sql = "SELECT name,time,address,description,origin,place,latitude,longitude FROM events"
    cursor.execute(sql)
    return cursor.fetchall()


def process_events(userid, token):
    c = 0
    conn = get_db()
    cursor = conn.cursor()

    check_dou_updates(cursor)
    conn.commit()


    graph = facebook.GraphAPI(access_token=token, version="3.1")
    rez = graph.get_all_connections(id=userid, connection_name='events')

    for event in rez:
        cursor.execute("SELECT EXISTS (SELECT origin FROM events WHERE origin = 'https://www.facebook.com/events/{}' LIMIT 1);".format(event['id']))
        check = cursor.fetchall()[0][0]
        if check == 1:
            continue
        c += 1
        print(event)
        try:
            place = event['place']['name']
        except:
            place = ''
        description = event['description'].replace('"', '`').replace("'", "`")
        name = event['name'].replace('"', '`').replace("'", "`")
        place = place.replace('"', '`').replace("'", "`")

        date = event['start_time'][:10]
        time = event['start_time'][11:16]
        if event['rsvp_status'] == 'unsure':
            priority = 6
        else:
            priority = 1

        if 'end_time' in event.keys():
            delta = datetime.datetime.strptime(event['end_time'], "%Y-%m-%dT%H:%M:%S%z") - datetime.datetime.strptime(
                event['start_time'], "%Y-%m-%dT%H:%M:%S%z")
            enddate = event['end_time'][:10]
            if delta.days > 1:
                priority = 9
        else:
            enddate = date

        try:
            address = event['place']['location']['street']
        except:
            address = place
        address=remove_all_quotes(address)

        try:
            latitude = event['place']['location']['latitude']
            longitude = event['place']['location']['longitude']
        except:
            latitude = None
            longitude = None


        sql = 'insert into events (origin,name,date,enddate, time,priority,description,place,datetime,address,latitude,longitude) values ("https://www.facebook.com/events/{}","{}","{}","{}","{}",{},"{}","{}","{}","{}","{}","{}")'. \
            format(event['id'], name, date, enddate, time, priority, description, place, event['start_time'],address,latitude,longitude)

        print(sql)
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
