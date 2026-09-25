from validations.sign_in_validation import sign_in_validate
from domain.admin_dashboard import admin_dashboard
from domain.staff_dashboard import staff_dashboard
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
                admin_dashboard()

            elif user["role"] == "staff":
                staff_dashboard()

            break

    if found == False:
        print("-------------------------")
        print("Invalid gmail or password")
        print("-------------------------")

