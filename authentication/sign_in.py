from validations.sign_in_validation import sign_in_validate
from domain.Admin.admin_dashboard import Admin
from domain.staff.staff_dashboard import staff
import json


def sign_in():

    gmail_id = input("Enter Your Gmail id : ")
    password = input("Enter Your password : ")

    gmail_id, password = sign_in_validate(gmail_id, password)

    with open("database/user.json", "r") as file:
        sign = json.load(file)

    found = False

    for user in sign:

        if user["gmail"] == gmail_id and user["password"] == password:

            found = True

            if user["role"] == "admin":
                print("=================")
                print("login successfull")
                print("=================")
                Admin().admin_dashboard()

            else:
                print("=======================")
                print("Staff login successfull")
                print("=======================")
                staff().staff_dashboard()

            break

    if found == False:
        print("-------------------------")
        print("Invalid gmail or password")
        print("-------------------------")

