from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/hi')
def hi():  # put application's code here
    return 'Hello'

if __name__ == '__main__':
    app.run()
