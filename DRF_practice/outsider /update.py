import requests
import json 

URL = 'http://127.0.0.1:8000/create/'

data = {
    'id':16,
    'name':'Dr Rased Islam',
    'age':36
}
json_data = json.dumps(data)
r = requests.put(url=URL, data=json_data)
data = r.json()
print(data)