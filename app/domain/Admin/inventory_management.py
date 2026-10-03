import json
import datetime
from app.validations.menu_validation import menu_validate
from app.validations.validation_log import Error_log
from app.validations.validator import validator_functions

class inventory():
    def add_item(self):
        obj = validator_functions()
        try:
            name = input("Enter item name :")
            category = input("Enter item category :")
            quantity = input("Enter item quantity :")
            price = input("Enter item price $ :")
            time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
            
            quantity = validator_functions().quantity_validate(quantity)
            name = obj.name_validate(name)
            category = obj.category_validate(category)
            price = obj.price_validate(price)
            
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
    
    def update_item(self):

        try:
            id = input("Enter item id for update : ")
            id = validator_functions().id_validate(id)

            with open("app/database/inventory.json", "r") as file:
                items = json.load(file)

            for item in items:
                if item["id"] == id:

                    print("--------------------------------------")
                    print(f"id          :    {item['id']}")
                    print(f"Name        :    {item['name']}")
                    print(f"Category    :    {item['category']}")
                    print(f"Quantity    :    {item['quantity']}")
                    print(f"Price       :    {item['price']}")
                    print("--------------------------------------")

                    print("-----------------------------")
                    print("1. Update Name")
                    print("2. Update Category")
                    print("3. Update price")
                    print("4. Update quantity")
                    print("-----------------------------")

                    choice = int(input("Enter your choice : "))
                    obj = validator_functions()
                    if choice == 1:

                        name = input("Enter new name : ")
                        name = obj.name_validate(name)
                        item["name"] = name

                    elif choice == 2:

                        category = input("Enter new category : ")
                        category = obj.category_validate(category)
                        item["category"] = category

                    elif choice == 3:

                        price = input("Enter new price : ")
                        price = obj.price_validate(price)
                        item["price"] = price

                    elif choice == 4:

                        quantity = input("Enter new quantity : ")
                        quantity = obj.quantity_validate(quantity)
                        item["quantity"] = quantity

                    else:

                        print("--------------")
                        print("Invalid choice")
                        print("--------------")
                        return

                    with open("app/database/inventory.json", "w") as file:
                        json.dump(items, file, indent=4)

                    print("========================")
                    print("Item update successful")
                    print("========================")
                    return

            print("==============")
            print("Item not found")
            print("==============")

        except Exception as f:
            Error_log(str(f))
            print("===================")
            print(f)
            print("===================")
        
    def delete_item(self):
            try:
                with open("app/database/inventory.json", "r") as file:
                    items = json.load(file)
    
                if len(items) == 0:
    
                    print("-----------------------------")
                    print("No item available")
                    print("-----------------------------")
                    return
    
                item_id = int(input("Enter item id to delete : "))
                item_id = menu_validate().delete_item_validate(item_id,items)
    
                for item in items:
    
                    if item["id"] == item_id:
                        items.remove(item)
                        break
    
                for i in range(len(items)):
                    items[i]["id"] = i + 1
    
                with open("app/database/menu.json", "w") as file:
                    json.dump(items, file, indent=4)
    
                print("-----------------------------")
                print("Item deleted successfully")
                print("-----------------------------")
            
            except Exception as f:
                Error_log(str(f))
                print("-------------------")
                print("Error",f)
                print("-------------------")
    
    