import json

dict = {"id" : "101",
        "Full Name" : "Ayan Solanki",
        "user_id" : "ayankhan101",
        "password" : "ayankhan99",
        "Contact" : "8302863793",
        "city" : "jodhpur"}

with open("database/admin_data.json","w") as file:
    json.dump(dict,file,indent=4)