# json string
employee_json_data = """{
  "employee0": {
    "firstName": "John",
    "lastName": "Smith",
    "age": 35,
    "city": "San Francisco"
  },
  "employee1": {
    "firstName": "Zoe",
    "lastName": "Thompson",
    "age": 32,
    "city": "Los Angeles"
  }
}"""

json_array = """
[
  {"one": 1},
  {"two": 2},
  {"three": 3}
]       
"""


import json

employee_data = json.loads(employee_json_data)
print(employee_data)
print(employee_data["employee0"]['firstName'])
# {'employee0': {'firstName': 'John', 'lastName': 'Smith', 'age': 35, 'city': 'San Francisco'}, 'employee1': {'firstName': 'Zoe', 'lastName': 'Thompson', 'age': 32, 'city': 'Los Angeles'}}

employee_array= json.loads(json_array)
print(employee_array)

# [{"one": 1}, {"two": 2},{"three": 3}]A


# read from file


# read from web
# using requests module - PREFERRED
import requests
wjdata = requests.get('url').json()


# using urllib2 module 
import json
weather = urllib2.urlopen('url')
wjson = weather.read()
wjdata = json.loads(wjson)
# wjdata = json.load(urllib2.urlopen('url'))

print wjdata['data']['current_condition'][0]['temp_C']




# ASSIGNING VALUES
MYJSON = {
    'username': 'gula_gut',
    'pics': '/0/myfavourite.jpeg',
    'id': '1'
}

#changing username
MYJSON['username'] = 'calixto'
print(MYJSON['username'])
