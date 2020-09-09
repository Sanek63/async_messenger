import time
from datetime import datetime
from flask import Flask, request

app = Flask(__name__)
db = []


@app.route('/')
def hello():
    return "Добро пожаловать в мессенджер <a href='/status'>Статус</a>"


@app.route('/status')
def status():
    dn = datetime.now()
    return {
        "status": True,
        "name": "Messenger",
        "time0": dn,
        "time1": time.asctime(),
        "time2": dn.isoformat(),
        "time3": dn.strftime("%d.%m.%Y %H:%M:%S")
    }


@app.route('/send', methods=['POST'])
def send():
    data = request.json

    timestamp = time.time()
    db.append({
        'id': len(db),
        'name': data['name'],
        'text': data['text'],
        'time': timestamp
    })
    return {"ok": True}


@app.route('/messages')
def messages():
    return {'messages': db}


app.run()
