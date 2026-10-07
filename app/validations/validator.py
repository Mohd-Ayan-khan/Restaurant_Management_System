from app.validations.validation_log import validation_log
from app.validations.validation_log import Error_log

class validator_functions:
    
    def id_validate(self,id):
        try:
            while True:
                id = str(id)

                if id == "":
                    validation_log("empty id")
                    print("-----------------------------")
                    print("ID cannot be empty")
                    print("-----------------------------")
                    id = input("Enter ID again : ")

                elif " " in id:
                    validation_log("no allowed space in id")
                    print("-----------------------------")
                    print("ID cannot contain spaces")
                    print("-----------------------------")
                    id = input("Enter ID again : ")

                elif not id.isdigit():
                    validation_log("id only consider number")
                    print("-----------------------------")
                    print("ID must contain only numbers")
                    print("-----------------------------")
                    id = input("Enter ID again : ")
                
                else:
                    id = int(id)
                    
                    if id <= 0 :
                        validation_log("id must be grator than 0")
                        print("------------------------")
                        print("ID must be gratot than 0")
                        print("------------------------")
                        id = int(input("Enter Id again :"))
                    
                    else:
                        return str(id)
        
        except Exception as f:
            Error_log(str(f))
            print("-------------------")
            print(f)
            print("-------------------")
    
    def name_validate(self, name):

        try:
            while True:

                if name == "":
                    validation_log("Empty item name")
                    print("-----------------------------")
                    print("Item name cannot be empty")
                    print("-----------------------------")
                    name = input("Enter item name : ")

                elif name.isspace():
                    validation_log("Item name cannot contain only spaces")
                    print("----------------------------------------")
                    print("Item name cannot contain only spaces")
                    print("----------------------------------------")
                    name = input("Enter item name : ")

                elif len(name) < 2:
                    validation_log("Item name must be at least 2 characters")
                    print("-----------------------------")
                    print("Item name must be at least 2 characters")
                    print("-----------------------------")
                    name = input("Enter item name : ")

                elif len(name) > 30:
                    validation_log("Item name cannot exceed 30 characters")
                    print("-----------------------------")
                    print("Item name cannot exceed 30 characters")
                    print("-----------------------------")
                    name = input("Enter item name : ")

                elif not name.isalpha():
                    validation_log("Item name must contain only alphabets")
                    print("----------------------------------------")
                    print("Item name must contain only alphabets")
                    print("----------------------------------------")
                    name = input("Enter item name : ")

                else:
                    return name

        except Exception as f:
            Error_log(str(f))
            print("-------------------")
            print(f)
            print("-------------------")
    
    
    def category_validate(self, category):
        try:
            while True:

                if category == "":
                    validation_log("Empty category")
                    print("-----------------------------")
                    print("Category cannot be empty")
                    print("-----------------------------")
                    category = input("Enter category : ")

                elif category.isspace():
                    validation_log("Category cannot contain only spaces")
                    print("----------------------------------------")
                    print("Category cannot contain only spaces")
                    print("----------------------------------------")
                    category = input("Enter category : ")

                elif len(category) < 2:
                    validation_log("Category must be at least 2 characters")
                    print("-----------------------------")
                    print("Category must be at least 2 characters")
                    print("-----------------------------")
                    category = input("Enter category : ")

                elif len(category) > 30:
                    validation_log("Category cannot exceed 30 characters")
                    print("-----------------------------")
                    print("Category cannot exceed 30 characters")
                    print("-----------------------------")
                    category = input("Enter category : ")

                elif not category.isalpha():
                    validation_log("Category must contain only alphabets")
                    print("----------------------------------------")
                    print("Category must contain only alphabets")
                    print("----------------------------------------")
                    category = input("Enter category : ")

                else:
                    return category

        except Exception as f:
            Error_log(str(f))
            print("-------------------")
            print(f)
            print("-------------------")
    
    def price_validate(self, price):

        try:
            price = str(price)
            while True:

                if price == "":
                    validation_log("Empty price")
                    print("-----------------------------")
                    print("Price cannot be empty")
                    print("-----------------------------")
                    price = input("Enter price : ")


                elif " " in price:
                    validation_log("Price cannot contain spaces")
                    print("-----------------------------")
                    print("Price cannot contain spaces")
                    print("-----------------------------")
                    price = input("Enter price : ")

                elif not price.isdigit():
                    validation_log("Price must contain only numbers")
                    print("-----------------------------")
                    print("Price must contain only numbers")
                    print("-----------------------------")
                    price = input("Enter price : ")

                else:
                    price = int(price)

                    if price <= 0:
                        validation_log("Price must be greater than 0")
                        print("-----------------------------")
                        print("Price must be greater than 0")
                        print("-----------------------------")
                        price = input("Enter price : ")

                    elif price > 2000:
                        validation_log("Price cannot be greater than 2000")
                        print("-----------------------------")
                        print("Price cannot be greater than 2000")
                        print("-----------------------------")
                        price = input("Enter price : ")

                    else:
                        return price

        except Exception as f:
            Error_log(str(f))
            print("-------------------")
            print(f)
            print("-------------------")

    def quantity_validate(self, quantity):

        try:
            while True:

                if quantity == "":
                    validation_log("Empty quantity")
                    print("-----------------------------")
                    print("Quantity cannot be empty")
                    print("-----------------------------")
                    quantity = input("Enter quantity : ")

                elif quantity.isspace():
                    validation_log("Quantity cannot contain only spaces")
                    print("--------------------------------")
                    print("Quantity cannot contain only spaces")
                    print("--------------------------------")
                    quantity = input("Enter quantity : ")

                elif " " in quantity:
                    validation_log("Quantity cannot contain spaces")
                    print("-----------------------------")
                    print("Quantity cannot contain spaces")
                    print("-----------------------------")
                    quantity = input("Enter quantity : ")

                elif not quantity.isdigit():
                    validation_log("Quantity must contain only numbers")
                    print("-----------------------------------")
                    print("Quantity must contain only numbers")
                    print("-----------------------------------")
                    quantity = input("Enter quantity : ")

                else:
                    quantity = int(quantity)

                    if quantity <= 0:
                        validation_log("Quantity must be greater than 0")
                        print("--------------------------------")
                        print("Quantity must be greater than 0")
                        print("--------------------------------")
                        quantity = input("Enter quantity : ")
                    
                    else:
                        return quantity

        except Exception as f:
            Error_log(str(f))
            print("-------------------")
            print(f)
            print("-------------------")
    
    def phone_validate(self,phone):
        try:
            while True:

                if phone == "":
                    validation_log("Phone number cannot be empty")
                    print("-----------------------------")
                    print("Phone number cannot be empty")
                    print("-----------------------------")
                    phone = input("Enter phone number again : ")

                elif " " in phone:
                    validation_log("Phone number cannot contain spaces")
                    print("-----------------------------")
                    print("Phone number cannot contain spaces")
                    print("-----------------------------")
                    phone = input("Enter phone number again : ")

                elif not phone.isdigit():
                    validation_log("Phone number must contain only numbers")
                    print("--------------------------------------------")
                    print("Phone number must contain only numbers")
                    print("--------------------------------------------")
                    phone = input("Enter phone number again : ")

                elif len(phone) != 10:
                    validation_log("Phone number must be 10 digits")
                    print("--------------------------------")
                    print("Phone number must be 10 digits")
                    print("--------------------------------")
                    phone = input("Enter phone number again : ")
                

                else:
                    return phone

        except Exception as f:
            Error_log(str(f))
            print("-------------------")
            print("Something went wrong")
            print("-------------------")
    
    def duration_validate(self,duration):
        
        try:
            while True:

                if duration == "":
                    print("-----------------------------")
                    print("Duration cannot be empty")
                    print("-----------------------------")
                    duration = input("Enter duration again : ")

                elif " " in duration:
                    print("-----------------------------")
                    print("Duration cannot contain spaces")
                    print("-----------------------------")
                    duration = input("Enter duration again : ")

                elif not duration.isdigit():
                    print("-----------------------------")
                    print("Duration must contain only numbers")
                    print("-----------------------------")
                    duration = input("Enter duration again : ")

                elif int(duration) <= 0:
                    print("-----------------------------")
                    print("Duration must be greater than 0")
                    print("-----------------------------")
                    duration = input("Enter duration again : ")

                else:
                    return int(duration)

        except Exception as f:
            Error_log(str(f))
            print("-----------------------------")
            print("Something went wrong")
            print("-----------------------------")