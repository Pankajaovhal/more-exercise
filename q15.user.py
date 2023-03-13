import json

d={"users": [{"firstName": "vidur",
"lastName": "singla",
"details": {
"age": 21,
"mobileNo": 1234567890,
"City": "Delhi"
}
},
{
"firstName": "rishabh",
"lastName": "verma",
"details": {
"age": 22,
"mobileNo": 12345678320,
"City": "Chandigarh"
}
},
{
"firstName": "abhishek",
"lastName": "gupta",
"details": {
"age": 25,
"mobileNo": 12332567890,
"City": "Gurgaon"
}
}
]
}
with open("user.json","w")as data:
    json.dump(d,data,indent=3)

users = d['users']

for user in d:
  counter = 0
  print ({"users full name is ":d[user][0]})
  while counter < len(d[user]):
        print ({"users mobile number is ":user['details'][counter]['mobileNo']})
        print ({"users age  is ": user['details'][counter]['age']})
        print ({"users city is ": user['details'][counter]['city']})
        counter+=1