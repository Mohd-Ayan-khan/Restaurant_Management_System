from app.validations.validation_log import validation_log
from app.validations.validation_log import Error_log

class menu_validate:
    
    def add_validate(self,name, category, price):
        try:
            while True:

                if name == "":
                    validation_log("Empty item name")
                    print("-----------------------------")
                    print("Item name cannot be empty")
                    print("-----------------------------")
                    name = input("Enter item name : ")

                elif len(name) < 2:
                    validation_log("name lenght must be 3")
                    print("-----------------------------")
                    print("Item name must be at least 2 characters")
                    print("-----------------------------")
                    name = input("Enter item name : ")

                elif category == "":
                    validation_log("empty category")
                    print("-----------------------------")
                    print("Category cannot be empty")
                    print("-----------------------------")
                    category = input("Enter category : ")

                elif len(category) < 2:
                    validation_log("category length must be 3")
                    print("-----------------------------")
                    print("Category must be at least 2 characters")
                    print("-----------------------------")
                    category = input("Enter category : ")

                elif price <= 0 or price > 2000:
                    validation_log("price must be grater 0 and less than 2000")
                    print("-----------------------------------------------")
                    print("Price must be greater than 0 and less than 2000")
                    print("-----------------------------------------------")
                    price = int(input("Enter price : "))

                else:
                    return name, category, price

        except Exception as f:
            Error_log(str(f))
            print("-------------------")
            print("Somthing went wrong")
            print("-------------------")
    
    
    def update_validate(self,choice,value):
        try:
            while True:
                if choice == 1:
                    name = value
                    if name == "":
                        validation_log("Empty item name")
                        print("-----------------------------")
                        print("Item name cannot be empty")
                        print("-----------------------------")
                        
                        name = input("Enter new item name : ")
                        value = name

                    elif len(name) < 2:
                        validation_log("Item name must be at least 2 characters")
                        print("-----------------------------")
                        print("Item name must be at least 2 characters")
                        print("-----------------------------")

                        name = input("Enter new item name : ")
                        value = name

                    else:
                        return name


                elif choice == 2:
                    category = value
                    
                    if category == "":
                        validation_log("Empty category")
                        print("-----------------------------")
                        print("Category cannot be empty")
                        print("-----------------------------")

                        category = input("Enter new category : ")
                        value = category

                    elif len(category) < 2:
                        validation_log("Category must be at least 2 characters")
                        print("-----------------------------")
                        print("Category must be at least 2 characters")
                        print("-----------------------------")

                        category = input("Enter new category : ")
                        value = category

                    else:
                        return category


                elif choice == 3:
                    price = value

                    if price <= 0 or price >= 2000:
                        validation_log("Price must be greater than 0 and less then 2000")
                        print("-----------------------------------------------")
                        print("Price must be greater than 0 and less then 2000")
                        print("-----------------------------------------------")

                        price = int(input("Enter new price : "))
                        value = price

                    else:
                        return price


                elif choice == 4:

                    if value == 1:
                        return True

                    elif value == 2:
                        return False

                    else:
                        validation_log("Invalid Is Veg choice")

                        print("----------------------------------")
                        print("Please enter 1 for Yes or 2 for No")
                        print("----------------------------------")

                        value = int(input("Is Veg : "))

                else:
                    return None

        except Exception as f:
            Error_log(str(f))
            print("-------------------")
            print("somthing went wrong")
            print("-------------------")
    
    def delete_item_validate(self,item_id, menu):

        try:
             while True:

                if item_id <= 0:

                    print("-----------------------------")
                    print("Item id must be greater than 0")
                    print("-----------------------------")

                    item_id = int(input("Enter item id : "))

                else:

                    found = False

                    for item in menu:
                        if item["id"] == item_id:
                            found = True
                            break

                    if found:
                        return item_id

                    print("-----------------------------")
                    print("Item id not found")
                    print("-----------------------------")

                    item_id = int(input("Enter item id : "))        
        except Exception as f:
            validation_log(str(f))
            print("------------------")
            print("error",f)
            print("------------------")