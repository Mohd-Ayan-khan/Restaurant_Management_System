from Ragistraion.sign_up import staff
from validations.validation_log import Error_log
def check_menu():
    
  try:
      while True:
                print("==============")
                print("--- Menu ---")
                print("==============")
                print("1. -- Admin --")
                print("--------------")
                print("2. -- Staff --")
                print("--------------")
                print("==============")
                
                choice = input("Enter Your choice :")
                
                if choice == "1":
                  pass
                elif choice == "2":
                  staff().staff_sign_up()
                  
  except Exception as a:
    Error_log(str(a))
    print("--------------------")
    print("something went wrong")
    print("--------------------")