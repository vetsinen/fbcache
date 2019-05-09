""" flask server module for processing fb tokens """
from flask import Flask
import facebook
import sqlite3
from flask import g

app = Flask(__name__)
app.debug = True
userid = "10156265228397361"

DATABASE = 'events.db'


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


@app.route('/')
def hello_world():
    return app.send_static_file('login.html')
    return 'Hello World!'


@app.route('/token/<token>')
def token(token):
    process_events(token)
    return 'Hello token'

def process_events(token):
    graph = facebook.GraphAPI(access_token=token, version="3.1")
    rez = graph.get_all_connections(id=userid, connection_name='events')
    c = 0
    for event in rez:
        c += 1

        print(event)
        break
    print(43)


if __name__ == '__main__':
    app.run()
