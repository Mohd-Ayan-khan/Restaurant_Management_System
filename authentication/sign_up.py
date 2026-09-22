from validations.sign_up_validations import staff_sign_up_validate
from validations.validation_log import Error_log
import uuid
import maskpass
import json


class staff:

    def __init__(self):

        self.user_id = ""
        self.user_name = ""
        self.full_name = ""
        self.password = ""
        self.Email = ""
        self.phone_number = ""
        self.role = ""

    def staff_sign_up(self):
        data = []

        try:

            self.user_id = str(uuid.uuid4().int)[:3]
            self.user_name = input("Enter your username : ")
            self.full_name = input("Enter your Full Name : ").upper()
            self.password = maskpass.askpass("Enter your password : ",mask="*")
            self.Email = input("Enter your Email id : ")
            self.phone_number = input("Enter your phone number : ")

            if staff_sign_up_validate(self) == False:
                return


            while True:

                print("---------------------------------")
                print("What is your role in Restaurant :")
                print("---------------------------------")
                print("1. Chef")
                print("2. Manager")
                print("3. Receptionist")
                print("4. Waiter")
                print("5. Cashier")
                print("---------------------------------")

                option = input("Enter your role : ")

                if option == "1":
                    self.role = "Chef"
                    break

                elif option == "2":
                    self.role = "Manager"
                    break

                elif option == "3":
                    self.role = "Receptionist"
                    break

                elif option == "4":
                    self.role = "Waiter"
                    break

                elif option == "5":
                    self.role = "Cashier"
                    break

                else:
                    print("**************")
                    print("Invalid Number")
                    print("**************")

            print("\n================================")
            print("----- Ragistration -----")
            print("================================")
            print(f" User_id   :  {self.user_id}")
            print("-----------------------------")
            print(f" Full Name :  {self.full_name}")
            print("-----------------------------")
            print(f" Username  :  {self.user_name}")
            print("-----------------------------")
            print(f" Password  :  *******")
            print("-----------------------------")
            print(f" Email     :  {self.Email}")
            print("-----------------------------")
            print(f" Contact   :  {self.phone_number}")
            print("-----------------------------")
            print(f" Role      :  {self.role}")
            print("=================================\n")
            
            
            dict = {"User Id" : self.user_id,
                    "Full Name" : self.full_name,
                    "Username" : self.user_name,
                    "Password" : self.password,
                    "Email" : self.Email,
                    "Contact" : self.phone_number,
                    "Role" : self.role} 
            
            with open("database/staff_data.json","r") as file:
                add = json.load(file)
            
            add.append(dict)
            
            with open("database/staff_data.json","w") as file:
                json.dump(add,file,indent=4)
            
            print("-------------------")
            print("Sign up successful")
            print("-------------------")


        except Exception as f:

            Error_log(str(f))

            print("--------------------")
            print("Something went wrong")
            print("--------------------")