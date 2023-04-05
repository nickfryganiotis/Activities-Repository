import requests 
from competences import competence_codes
from activities import activities

#with open('db.json') as f:
  #data = json.load(f)

#for js in activities:
#  x = requests.post(url, json = js)

#url="http://localhost:5000/create_emosocio_competence"

#for js in emosocio_competencies:
#  x = requests.post(url, json = js)

url="http://localhost:5000/create_competence"

for code in competence_codes:
    x = requests.post(url, json={"code": code})

url = "http://localhost:5000/create_activity"

for activity in activities:
    x = requests.post(url, json=activity)