from validations.validation_log import validation_log
from validations.validation_log import Error_log
import maskpass


def staff_sign_up_validate(self):

    try:

        while True:

            if self.user_name == "":
                validation_log("Empty username")
                
                print("*****************************")
                print("Empty username is not valid")
                print("*****************************")

                self.user_name = input("Enter your username again : ")

            elif len(self.user_name) < 3:
                validation_log("Short length username")

                print("**************************************")
                print("Username must be at least 3 characters")
                print("**************************************")

                self.user_name = input("Enter your username again : ")

            elif len(self.user_name) > 20:
                validation_log("Username must be less than 20 characters")

                print("****************************************")
                print("Username must be less than 20 characters")
                print("****************************************")

                self.user_name = input("Enter your username again : ")

            elif " " in self.user_name:
                validation_log("Username cannot contain spaces")

                print("*******************************")
                print("Username cannot contain spaces")
                print("*******************************")

                self.user_name = input("Enter your username again : ")

            else:
                break


        while True:

            if self.password == "":
                validation_log("Empty password")

                print("*****************************")
                print("Empty password is not valid")
                print("*****************************")

                self.password = maskpass.askpass("Enter your password again : ",mask="*")

            elif len(self.password) < 8:
                validation_log("Password must be at least 8 characters")

                print("--------------------------------")
                print("Password must be at least 8 characters")
                print("--------------------------------")

                self.password = maskpass.askpass("Enter your password again : ",mask="*")

            elif len(self.password) > 45:
                validation_log("Password must be less than 45 characters")

                print("----------------------------------------")
                print("Password must be less than 45 characters")
                print("----------------------------------------")

                self.password = maskpass.askpass("Enter your password again : ",mask="*")

            else:
                break


        while True:

            if self.Email == "":
                validation_log("Empty Email")

                print("*****************************")
                print("Empty Email is not valid")
                print("*****************************")

                self.Email = input("Enter your Email again : ")

            elif " " in self.Email:
                validation_log("Email cannot contain spaces")

                print("*******************************")
                print("Email cannot contain spaces")
                print("*******************************")

                self.Email = input("Enter your Email again : ")

            elif "@" not in self.Email:
                validation_log("Email must contain (@)")

                print("*************************")
                print("Email must contain (@)")
                print("*************************")

                self.Email = input("Enter your Email again : ")

            elif "." not in self.Email:
                validation_log("Email must contain (.)")

                print("*************************")
                print("Email must contain (.)")
                print("*************************")

                self.Email = input("Enter your Email again : ")

            elif self.Email.index("@") > self.Email.index("."):
                validation_log("(@) must be before (.)")

                print("************************")
                print("(@) must be before (.)")
                print("************************")

                self.Email = input("Enter your Email again : ")

            else:
                break


        while True:

            if self.phone_number == "":
                validation_log("Empty phone number")

                print("-----------------------------")
                print("Phone number cannot be empty")
                print("-----------------------------")

                self.phone_number = input("Enter your phone number again : ")

            elif not self.phone_number.isdigit():
                validation_log("Phone number must contain digits")

                print("-----------------------------")
                print("Phone number must contain only numbers")
                print("-----------------------------")

                self.phone_number = input("Enter your phone number again : ")

            elif len(self.phone_number) != 10:
                validation_log("Phone number length must be 10")

                print("-----------------------------")
                print("Phone number must be 10 digits")
                print("-----------------------------")

                self.phone_number = input("Enter your phone number again : ")

            else:
                break

        return True

    except Exception as a:

        Error_log(str(a))

        print("--------------------")
        print("Something went wrong")
        print("--------------------")

        return False