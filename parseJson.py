import requests
import json
response = requests.get("http://api.open-notify.org/astros.json")
#print(response.status_code)
text = json.dumps(response.json(),sort_keys=True,indent=4)
#print(text)
y=json.loads(text)
for key,value in y.iteritems():
        print key, 'is:', value
print ''
print(y["people"])
~
