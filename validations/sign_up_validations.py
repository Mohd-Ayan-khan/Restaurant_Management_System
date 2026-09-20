
from validations.validation_log import validation_log
from 

def staff_sign_up_validate(user_id,user_name,Full_name,password,Email,phone_number):
        
        while True:
            try:
                if user_name == "":
                    validation_log("Empty username")
                                
                    print("*****************************")
                    print("Enmpty username is not valid")
                    print("*****************************")
                    
                elif len(user_name) < 3:
                    validation_log("short length username")
                    
                    print("**************************************")    
                    print("Username must be at least 3 characters")
                    print("**************************************c")    
            
                
                elif len(user_name) > 20:
                    validation_log("username must be less than 20 characters")
                    
                    print("****************************************")
                    print("username must be less than 20 characters")
                    print("****************************************")
                
                elif " " in user_name:
                    validation_log("username cannot contain spaces")
                    
                    print("*******************************")
                    print("username cannot conatain spaces")
                    print("*******************************")
                
                else:
                    print("---------------")
                    print("Correct Deatail")
                    print("---------------")
                    break
                
                
                if password == "":
                    validation_log("Empty password")
                                            
                    print("*****************************")
                    print("Enmpty password is not valid")
                    print("*****************************")
                
                elif len(password) < 8:
                    validation_log("password must be at least 8 characters")
                    
                    print("-----------------------------")
                    print("password length is must be 8 ")
                    print("-----------------------------")
                
                elif len(password) > 45:
                    validation_log("password must be less than 45 characters")
                    
                    print("----------------------------------------")
                    print("password must be less than 45 characters")
                    print("----------------------------------------")
                else:
                    validation_log("invalid password")
                    print("------------------------")
                    print(" -- invalid password -- ")
                    print("------------------------")
                    
                if Email == "":
                    validation_log("Empty Email")
                                                    
                    print("*****************************")
                    print("Enmpty Email is not valid")
                    print("*****************************")
                
                elif " " in password:
                    validation_log("Email cannot contain spaces")
                                    
                    print("*******************************")
                    print("Email cannot conatain spaces")
                    print("*******************************")
                
                elif "." not in Email:
                    validation_log("Email must contain (.)")
                    
                    print("*************************")
                    print("Email must be contain (.)")
                    print("*************************")
                
                elif "@" not in Email:
                    validation_log("Email must contain (@)")
                                        
                    print("*************************")
                    print("Email must be contain (@)")
                    print("*************************")
                
                elif Email.index("@") > Email.index("."):
                    validation_log("(@) must be first of (.)")
                    
                    print("************************")
                    print("(@) must be first of (.)")
                    print("************************")
                
                else:
                    validation_log("Invalid Email")
                    print("**************")
                    print("Inavalid Email")
                    print("**************")
                
                if phone_number > 10:
                    validation_log("phone number length must be 10")
                    
                    print("******************************")
                    print("phone number length must be 10")
                    print("******************************")
                break
                    
                                    
                    
            except Exception as a:
                with open("logs/error.txt","a") as file:
                    file.write(str(a)+"\n")
                
                print("--------------------")
                print("something went wrong")
                print("--------------------")
        