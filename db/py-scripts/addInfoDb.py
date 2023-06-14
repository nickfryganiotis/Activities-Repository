import requests 
from competencies import competency_codes
from strategies import strategies_codes
from special_needs import special_needs_codes
from activities import activities

#with open('db.json') as f:
  #data = json.load(f)

#for js in activities:
#  x = requests.post(url, json = js)

#url="http://localhost:5000/create_emosocio_competence"

#for js in emosocio_competencies:
#  x = requests.post(url, json = js)


# url="http://localhost:5000/create_competency/"

# for code in competency_codes:
#     x = requests.post(url, json={"code": code})

# url="http://localhost:5000/create_didactic_strategy/"

# for code in strategies_codes:
#     x = requests.post(url, json={"code": code})

# url="http://localhost:5000/create_special_need/"

# for code in special_needs_codes:
#     x = requests.post(url, json={"code": code})

url = "http://localhost:5000/create_activity/"

for activity in activities:
    x = requests.post(url, json=activity, headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuZnJ5Z2FuaW90aXNAbmV0bW9kZS5udHVhLmdyIiwiaWF0IjoxNjg2NzQ1NjE1LCJleHAiOjE2ODY3NTY0MTV9.1pO8H0YjRkkcsJUPXuWV7WVlP2SFjzHlIvIavCJEyfU"})