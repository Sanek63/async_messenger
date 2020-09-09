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

    db.append({
        'id': len(db),
        'name': data['name'],
        'text': data['text'],
        'timestamp': time.time()
    })
    return {"ok": True}


@app.route('/messages')
def messages():
    if 'after_id' in request.args:
        after_id = int(request.args['after_id']) + 1
    else:
        after_id = 0
    return {'messages': db[after_id:]}


app.run()
