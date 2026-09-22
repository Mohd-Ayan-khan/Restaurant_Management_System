import json

class sing_in:

    def admin_sign_in(self,id,password):

        with open("database/admin_data.json", "r") as file:
            admin = json.load(file)

        if admin["id"] == id and admin["password"] == password:
            print("data found")
        else:
            print("data not found")

    def staff_sign_in(self,id,password):

        with open("database/staff_data.json", "r") as file:
            staff = json.load(file)

        found = False

        for user in staff:
            if user["id"] == id and user["password"] == password:
                print("staff found")
                found = True
                break

        if found == False:
            print("staff not found")

