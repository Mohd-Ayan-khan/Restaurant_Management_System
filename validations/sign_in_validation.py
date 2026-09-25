
from validations.validation_log import validation_log
from validations.validation_log import Error_log


def sign_in_validate(id, password):
    try:
        while True:

            if id == "":
                validation_log("Empty Email")

                print("*****************************")
                print("Empty Email is not valid")
                print("*****************************")

                id = input("Enter your Email again : ")

            elif " " in id:
                validation_log("Email cannot contain spaces")

                print("*******************************")
                print("Email cannot contain spaces")
                print("*******************************")

                id = input("Enter your Email again : ")

            elif "@" not in id:
                validation_log("Email must contain (@)")

                print("*************************")
                print("Email must contain (@)")
                print("*************************")

                id = input("Enter your Email again : ")

            elif "." not in id:
                validation_log("Email must contain (.)")

                print("*************************")
                print("Email must contain (.)")
                print("*************************")

                id = input("Enter your Email again : ")

            elif id.index("@") > id.index("."):
                validation_log("(@) must be before (.)")

                print("************************")
                print("(@) must be before (.)")
                print("************************")

                id = input("Enter your Email again : ")

            else:
                break


        while True:

            if password == "":
                validation_log("Empty password")

                print("*****************************")
                print("Empty password is not valid")
                print("*****************************")

                password = input("Enter your password again : ")

            elif len(password) < 8:
                validation_log("Password must be at least 8 characters")

                print("--------------------------------")
                print("Password must be at least 8 characters")
                print("--------------------------------")

                password = input("Enter your password again : ")

            elif len(password) > 45:
                validation_log("Password must be less than 45 characters")

                print("----------------------------------------")
                print("Password must be less than 45 characters")
                print("----------------------------------------")

                password = input("Enter your password again : ")

            else:
                break
        return id,password
    
    except Exception as f:
        Error_log(str(f))
        print("*******************")
        print("somthing went wrong")
        print("*******************")