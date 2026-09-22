from authentication.sign_up import staff
from validations.validation_log import Error_log
from authentication.sign_in import sing_in
def menu():
    
  try:
      while True:
                print("====================")
                print("--- Menu ---")
                print("====================")
                print("1. -- admin --")
                print("--------------------")
                print("2. -- staff --")
                print("--------------------")
                print("3. -- place order --")
                print("--------------------")
                print("4. -- Exit --")
                print("====================")
                
                choice = input("Enter Your choice :")
                
                if choice == "1":
                  id = input("Enter the Admin id :")
                  password = input("Enter your Password :")
                  sing_in().admin_sign_in(id,password)
                  
                elif choice == "2":
                  id = input("Enter the staff id :")
                  password = input("Enter your Password :")
                  sing_in().staff_sign_in(id,password)
                  
  except Exception as a:
    Error_log(str(a))
    print("--------------------")
    print("something went wrong")
    print("--------------------")