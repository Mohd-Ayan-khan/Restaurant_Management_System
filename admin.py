import json

data =[]
dict = {"id" : "101",
        "Full Name" : "Ayan Solanki",
        "user_id" : "ayankhan101",
        "gmail" : "ayankhan099@gmail.com",
        "password" : "ayankhan99",
        "role" : "admin"}

data.append(dict)


with open("database/user.json","w") as file:
    json.dump(data,file,indent=4)