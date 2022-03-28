import requests
url = 'http://localhost:5000/api'
r = requests.post(url, json={'exp': [9.8, 8.0, 9.874687]})
print(r.json())
