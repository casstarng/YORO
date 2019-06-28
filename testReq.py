import requests
import json

event_id = "5d1387b338fd21e#"
url = "http://4fd2bcd1.ngrok.io/yoro/checkInUser"
user = {"cassidy": "catarng"}

name = "cassidy"

data = {"id": event_id + user[name]}
headers = {"Content-Type": "application/json"}
print("Sent Requests: " + str(data))
r = requests.post(url=url, data=json.dumps(data), headers=headers)
print(r)
