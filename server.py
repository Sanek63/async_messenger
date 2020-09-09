from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world 123! <a href='/status'>Статус</a>"

@app.route('/status')
def status():
    return {"status": "ok"}


app.run()