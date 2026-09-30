import json
import datetime
from app.validations.validation_log import Error_log
from app.validations.menu_validation import menu_validate

class inventory(menu_validate):
    def add_item(self):
        try:
            obj = menu_validate()
            
            name = input("Enter item name :")
            category = input("Enter item category :")
            quantity = input("Enter item quantity :")
            price = int(input("Enter item price $ :"))
            time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
            
            name,category,price = obj.add_validate(name,category,price)
            
            with open("app/database/inventory.json",'r') as file:
                items = json.load(file)
            
            dict={
                "id": len(items)+1,
                "name": name,
                "category": category,
                "quantity": quantity,
                "price": price,
                "Time" : time 
            }
            items.append(dict)
            with open("app/database/inventory.json",'w') as file:
                json.dump(items,file,indent=4)
            
            print("===================================")
            print("Successfully Item add in Inventory")
            print("===================================")

        except Exception as f:
            Error_log(str(f))
            print("-------------------")
            print(f)
            print("-------------------")