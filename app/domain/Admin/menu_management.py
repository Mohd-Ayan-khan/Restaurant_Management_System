import json
from app.validations.validation_log import Error_log
from app.validations.validator import validator_functions
class menu_management:
    def add_item(self):
        obj = validator_functions()
        try:
            with open("app/database/menu.json", "r") as file:
                menu = json.load(file)

            id = len(menu) + 1

            name = input("Enter item name : ")
            category = input("Enter category : ")
            price = input("Enter price : ")

            print("1. is veg")
            print("2. is not veg")
            veg = int(input("Is Veg : "))

            if veg == 1:
                isVeg = True
            else:
                isVeg = False
            
            name = obj.name_validate(name)
            category = obj.category_validate(category)
            price = obj.price_validate(price)

            item = {
                "id": id,
                "name": name,
                "category": category,
                "price": price,
                "isVeg": isVeg,
                "isAvailable": True
            }

            menu.append(item)

            with open("app/database/menu.json", "w") as file:
                json.dump(menu, file, indent=4)

            print("-----------------------------")
            print("Item added successfully")
            print("Item ID :", id)
            print("-----------------------------")

        except Exception as f:
            Error_log(str(f))
            print("--------------------")
            print("Error :",f)
            print("--------------------")
    
    
    
    def update_item(self):
        obj = validator_functions()
        try:
            with open("app/database/menu.json", "r") as file:
                menu = json.load(file)

            id = input("Enter update item id : ")
            id = validator_functions().id_validate(id)
            
            for item in menu:
                if item["id"] == id:
                    
                    print("-------------------------------------")
                    print(f"id          : {item["id"]}")
                    print(f"name        : {item["name"]}")
                    print(f"category    : {item["category"]}")
                    print(f"price       : {item["price"]}")
                    print("-------------------------------------\n")

                    print("-----------------------------")
                    print("1. Update Name")
                    print("2. Update Category")
                    print("3. Update Price")
                    print("4. Update Is Veg")
                    print("-----------------------------")

                    choice = int(input("What do you want to update : "))

                    if choice == 1:
                        name = input("Enter new item name : ")
                        name = obj.name_validate(name)
                        item["name"] = name

                    elif choice == 2:
                        category = input("Enter new category : ")
                        category = obj.category_validate(category)
                        item["category"] = category

                    elif choice == 3:
                        price = int(input("Enter new price : "))
                        price = obj.price_validate(price)
                        item["price"] = price

                    elif choice == 4:
                        print("1. Yes")
                        print("2. No")
                        veg = int(input("Is Veg : "))
                        isVeg = obj.update_validate(choice,veg)

                        if veg == 1:
                            item["isVeg"] = True
                        else:
                            item["isVeg"] = False

                    else:
                        print("--------------")
                        print("Invalid choice")
                        print("--------------")
                        return

                    with open("app/database/menu.json", "w") as file:
                        json.dump(menu, file, indent=4)

                    print("-----------------------------")
                    print("Item updated successfully")
                    print("-----------------------------")
                    break

            else:
                print("--------------------")
                print("Item not found")
                print("--------------------")
        
        except Exception as f:
            Error_log(str(f))
            print("--------------------")
            print("something went wrong")
            print("--------------------")
    
    
    def delete_item(self):
        try:
            with open("app/database/menu.json", "r") as file:
                menu = json.load(file)

            if len(menu) == 0:

                print("-----------------------------")
                print("No item available")
                print("-----------------------------")
                return

            item_id = input("Enter item id to delete : ")
            item_id = validator_functions().id_validate(item_id)

            for item in menu:

                if item["id"] == item_id:
                    menu.remove(item)
                    break

            for i in range(len(menu)):
                menu[i]["id"] = i + 1

            with open("app/database/menu.json", "w") as file:
                json.dump(menu, file, indent=4)

            print("-----------------------------")
            print("Item deleted successfully")
            print("-----------------------------")
        
        except Exception as f:
            Error_log(str(f))
            print("-------------------")
            print("Error",f)
            print("-------------------")
    
    
    def item_view(self):
        try:
            with open("app/database/menu.json", "r") as file:
                menu = json.load(file)

            if len(menu) == 0:
                print("------------------")
                print("No item available")
                print("------------------")
                return

            print("\n==============================================")
            print("                 MENU ITEMS")
            print("================================================")
            for item in menu:
                print("ID          :", item["id"])
                print("Name        :", item["name"])
                print("Category    :", item["category"])
                print("Price       :", item["price"])

                if item["isVeg"]:
                    print("Veg         : Yes")
                else:
                    print("Veg         : No")

                if item["isAvailable"]:
                    print("Available   : Yes")
                else:
                    print("Available   : No")
                print("----------------------------------------------")

        except Exception as f:
            Error_log(str(f))
            print("-------------------")
            print("Error", f)
            print("-------------------")