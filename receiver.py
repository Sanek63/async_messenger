import requests


url = 'http://127.0.0.1:5000/messages'

response = requests.get(url, params={'after_id': 2})
print(response.json())