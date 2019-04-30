from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return app.send_static_file('login.html')
    return 'Hello World!'

@app.route('/<token>')
def events(token):
    return token


if __name__ == '__main__':
    app.run()
