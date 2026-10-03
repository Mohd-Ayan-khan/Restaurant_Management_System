import json
from app.validations.validation_log import Error_log
from app.authentication.staff_sign_up import staff
from app.validations.validator import validator_functions
from app.validations.staff_management_validation import staff_management_valid

class staff_management(staff):
    
    def add_staff(self):
        obj = staff()
        obj.staff_sign_up()
    
    def update_staff(self):
        try:
            obj = staff_management_valid()
            with open("app/database/user.json", "r") as file:
                staff_data = json.load(file)

            if len(staff_data) == 0:
                print("-----------------------------")
                print("No staff available")
                print("-----------------------------")
                return

            user_id = input("Enter staff user id to update : ")
            user_id = validator_functions().id_validate(user_id)

            for staff in staff_data:

                if staff["User Id"] == user_id:
                    if staff["Role"] in ["Chef", "Manager", "Receptionist", "Waiter", "Cashier"]:

                        print("--------------------------------")
                        print("1. Update Username")
                        print("2. Update Full Name")
                        print("3. Update Password")
                        print("4. Update Email")
                        print("5. Update Contact")
                        print("6. Update Role")
                        print("--------------------------------")

                        choice = int(input("What do you want to update : "))

                        if choice == 1:
                            value = input("Enter new username : ")
                            value = obj.staff_update_validate(choice, value)
                            staff["Username"] = value

                        elif choice == 2:
                            value = input("Enter new full name : ")
                            value = obj.staff_update_validate(choice, value)
                            staff["Full Name"] = value

                        elif choice == 3:
                            value = input("Enter new password : ")
                            value = obj.staff_update_validate(choice, value)
                            staff["Password"] = value

                        elif choice == 4:
                            value = input("Enter new Email : ")
                            value = obj.staff_update_validate(choice, value)
                            staff["Email"] = value

                        elif choice == 5:
                            value = input("Enter new contact : ")
                            value = obj.staff_update_validate(choice, value)
                            staff["Contact"] = value

                        elif choice == 6:
                            value = int(input("Enter new role : "))
                            value = obj.staff_update_validate(choice, value)
                            staff["Role"] = value

                        else:
                            print("-----------------------------")
                            print("Invalid choice")
                            print("-----------------------------")
                            return
                    
                    else:
                        print("-------------------")
                        print("N0 staff data found")
                        print("-------------------")

                    with open("database/user.json", "w") as file:
                        json.dump(staff_data, file, indent=4)

                    print("-----------------------------")
                    print("Staff updated successfully")
                    print("-----------------------------")
                    return

            print("-----------------------------")
            print("Staff not found")
            print("-----------------------------")

        except Exception as f:
            Error_log(str(f))
            print("-----------------------------")
            print("something went wrong")
            print("-----------------------------")
    
    def delete_staff(self):
        try:
            with open("app/database/user.json", "r") as file:
                users = json.load(file)

            if len(users) == 0:
                print("No staff available")
                return

            user_id = input("Enter staff user id to delete : ")
            user_id = validator_functions().id_validate(id)

            for user in users:
                if user["User Id"] == user_id:

                    if user["Role"] in ["Chef","Manager","Receptionist","Waiter","Cashier"]:

                        print("--------------------------------")
                        print("Staff ID   :", user["User Id"])
                        print("Name       :", user["Full Name"])
                        print("Username   :", user["Username"])
                        print("Role       :", user["Role"])
                        print("--------------------------------")

                        users.remove(user)

                        with open("app/database/user.json", "w") as file:
                            json.dump(users, file, indent=4)

                        print("--------------------------")
                        print("Staff deleted successfully")
                        print("--------------------------")
                        return

                    else:
                        print("---------------------------------------------")
                        print("Admin cannot be deleted from staff management")
                        print("---------------------------------------------")
                        return

            print("---------------")
            print("Staff not found")
            print("---------------")

        except Exception as f:
            Error_log(str(f))
            print("Error :", f)
    
    
    def view_staff(self):
        try:
            with open("app/database/user.json", "r") as file:
                users = json.load(file)

            found = False

            for user in users:
                if user["Role"] in ["Chef", "Manager", "Receptionist", "Waiter", "Cashier"]:

                    found = True

                    print("--------------------------------")
                    print("Staff ID   :", user["User Id"])
                    print("Name       :", user["Full Name"])
                    print("Username   :", user["Username"])
                    print("Role       :", user["Role"])
                    print("Email      :", user["Email"])
                    print("Contact    :", user["Contact"])
                    print("--------------------------------")

            if found == False:
                print("-----------------------")
                print("No staff data Available")
                print("-----------------------")

        except Exception as f:
            Error_log(str(f))
            print("--------------------")
            print("Something went wrong")
            print("--------------------")
    
    def search_staff(self):
        try:
            
            with open("app/database/user.json",'r') as file:
                users = json.load(file)
            
            found = False
            
            id = input("Enter search staff Id :")
            
            for user in users:
                if user["User Id"] == id:
                    if user["Role"] in ["Chef", "Manager", "Receptionist", "Waiter", "Cashier"]:
                        found = True
                        
                        print("--------------------------------")
                        print("Staff ID   :", user["User Id"])
                        print("Name       :", user["Full Name"])
                        print("Username   :", user["Username"])
                        print("Role       :", user["Role"])
                        print("Email      :", user["Email"])
                        print("Contact    :", user["Contact"])
                        print("--------------------------------")
            
            if found == False:
                print("----------------------")
                print("staff is not available")
                print("----------------------")
        
        except Exception as f:
            Error_log(str(f))
            print("\n-------------------")
            print("somthing went wrong")
            print("-------------------")