import json
from app.validations.sign_in_validation import sign_in_validate
from app.domain.Admin.admin_dashboard import Admin
from app.domain.staff.staff_dashboard import staff
from app.validations.validation_log import Error_log


def sign_in(check):

    try:
        gmail_id = input("Enter Your Gmail id : ")
        password = input("Enter Your password : ")

        gmail_id, password = sign_in_validate(gmail_id, password)

        with open("app/database/user.json", "r") as file:
            users = json.load(file)

        found = False

        for user in users:
            if user["Email"] == gmail_id and user["Password"] == password:

                if check == "admin":

                    if user["Role"] == "admin":
                        found = True
                        print("=================")
                        print("Login successful")
                        print("=================")
                        Admin().admin_dashboard()
                        break

                    else:
                        print("----------------------------")
                        print("This is not an admin account")
                        print("----------------------------")
                        break

                elif check == "staff":

                    if user["Role"] != "admin":
                        found = True

                        print("=======================")
                        print("Staff login successful")
                        print("=======================")
                        staff().staff_dashboard()
                        break

                    else:
                        print("-----------------------------------")
                        print("Admin account cannot login as staff")
                        print("-----------------------------------")
                        break

        if found == False:
            print("-------------------------")
            print("Invalid gmail or password")
            print("-------------------------")

    except Exception as f:
        Error_log(str(f))
        print("--------------------")
        print(f)
        print("--------------------")