import requests
import json 

URL = 'http://127.0.0.1:8000/create/'

data = {
    'id':13,
    'name':'billah Islam',
    'age':34
}
json_data = json.dumps(data)
r = requests.put(url=URL, data=json_data)
data = r.json()
print(data)