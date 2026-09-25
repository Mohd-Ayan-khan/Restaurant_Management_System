from validations.validation_log import Error_log
from authentication.sign_in import sign_in
from validations.validation_log import validation_log

def menu():
    
  try:
      while True:
                print("==========================")
                print("--- Menu ---")
                print("==========================")
                print("1. -- admin --")
                print("--------------------------")
                print("2. -- staff --")
                print("--------------------------")
                print("3. -- Exit --")
                print("==========================")
                
                choice = input("Enter Your choice :")
                
                if choice == "1":
                  sign_in()
                  
                elif choice == "2":
                  sign_in()
                  
                elif choice == "3":
                  print("=================")
                  print("Thanks for visite")
                  print("=================")
                  break
                                
                else:
                  validation_log("invalid choice")
                  print("--------------")
                  print("invalid choice")
                  print("--------------")
                  
  except Exception as a:
    Error_log(str(a))
    print("--------------------")
    print("something went wrong")
    print("--------------------")
