import requests


url = 'http://127.0.0.1:5000/send'
data = {
    'name': 'Jack',
    'text': 'Hello'
}

response = requests.post(url, json=data)