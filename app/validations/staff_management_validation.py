from app.validations.validation_log import validation_log
from app.validations.validation_log import Error_log
import maskpass

class staff_management_valid:
        def staff_update_validate(self,choice,value):
            try:
                while True:
                    if choice == 1:

                        if value == "":
                            validation_log("Empty username")
                            print("-----------------------------")
                            print("Username cannot be empty")
                            print("-----------------------------")
                            value = input("Enter username again : ")

                        elif len(value) < 3:
                            validation_log("Short username")
                            print("-----------------------------")
                            print("Username must be at least 3 characters")
                            print("-----------------------------")
                            value = input("Enter username again : ")

                        elif len(value) > 20:
                            validation_log("Long username")
                            print("-----------------------------")
                            print("Username must be less than 20 characters")
                            print("-----------------------------")
                            value = input("Enter username again : ")

                        elif " " in value:
                            validation_log("Username contains spaces")
                            print("-----------------------------")
                            print("Username cannot contain spaces")
                            print("-----------------------------")
                            value = input("Enter username again : ")

                        else:
                            return value

                    elif choice == 2:

                        if value == "":
                            validation_log("Empty full name")
                            print("-----------------------------")
                            print("Full name cannot be empty")
                            print("-----------------------------")
                            value = input("Enter full name again : ")
                        
                        elif " " not in value:
                            validation_log("Full Name must contain first name and last name")
                            print("-----------------------------")
                            print("Enter First Name and Last Name")
                            print("-----------------------------")
                            value = input("Enter Full Name again : ")

                        elif not value.replace(" ", "").isalpha():
                            validation_log("Full Name must contain only alphabets")
                            print("-----------------------------")
                            print("Full Name must contain only alphabets")
                            print("-----------------------------")
                            value = input("Enter Full Name again : ")
                            
                        else:
                            return value.upper()

                    elif choice == 3:

                        if value == "":
                            validation_log("Empty password")
                            print("-----------------------------")
                            print("Password cannot be empty")
                            print("-----------------------------")
                            value = maskpass.askpass("Enter password again : ", mask="*")

                        elif len(value) < 8:
                            validation_log("Short password")
                            print("-----------------------------")
                            print("Password must be at least 8 characters")
                            print("-----------------------------")
                            value = maskpass.askpass("Enter password again : ", mask="*")

                        elif len(value) > 45:
                            validation_log("Long password")
                            print("-----------------------------")
                            print("Password must be less than 45 characters")
                            print("-----------------------------")
                            value = maskpass.askpass("Enter password again : ", mask="*")

                        else:
                            return value

                    elif choice == 4:

                        if value == "":
                            validation_log("Empty Email")
                            print("-----------------------------")
                            print("Email cannot be empty")
                            print("-----------------------------")
                            value = input("Enter Email again : ")

                        elif " " in value:
                            validation_log("Email contains spaces")
                            print("-----------------------------")
                            print("Email cannot contain spaces")
                            print("-----------------------------")
                            value = input("Enter Email again : ")

                        elif "@" not in value:
                            validation_log("Email must contain @")
                            print("-----------------------------")
                            print("Email must contain @")
                            print("-----------------------------")
                            value = input("Enter Email again : ")

                        elif "." not in value:
                            validation_log("Email must contain .")
                            print("-----------------------------")
                            print("Email must contain .")
                            print("-----------------------------")
                            value = input("Enter Email again : ")

                        elif value.index("@") > value.index("."):
                            validation_log("@ must be before .")
                            print("-----------------------------")
                            print("@ must be before .")
                            print("-----------------------------")
                            value = input("Enter Email again : ")

                        else:
                            return value

                    elif choice == 5:

                        if value == "":
                            validation_log("Empty phone number")
                            print("-----------------------------")
                            print("Phone number cannot be empty")
                            print("-----------------------------")
                            value = input("Enter phone number again : ")
                        
                        elif " " in value:
                            validation_log("phone contains spaces")
                            print("-----------------------------")
                            print("phone number cannot contain spaces")
                            print("-----------------------------")
                            value = input("Enter phone number again : ")

                        elif not value.isdigit():
                            validation_log("Phone number must contain digits")
                            print("-----------------------------")
                            print("Phone number must contain only numbers")
                            print("-----------------------------")
                            value = input("Enter phone number again : ")

                        elif len(value) != 10:
                            validation_log("Phone number length is not 10")
                            print("-----------------------------")
                            print("Phone number must be 10 digits")
                            print("-----------------------------")
                            value = input("Enter phone number again : ")

                        else:
                            return value

                    elif choice == 6:

                        if value == 1:
                            return "Chef"

                        elif value == 2:
                            return "Manager"

                        elif value == 3:
                            return "Receptionist"

                        elif value == 4:
                            return "Waiter"

                        elif value == 5:
                            return "Cashier"

                        else:
                            validation_log("invalid role")
                            print("-----------------------------")
                            print("Invalid role")
                            print("-----------------------------")
                            value = int(input("Enter role again : "))

            except Exception as f:

                Error_log(str(f))
                print("-----------------------------")
                print("Something went wrong")
                print("-----------------------------")
                return False