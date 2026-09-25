from validations.validation_log import validation_log
from validations.validation_log import Error_log

def staff_dashboard():
    try:
        while True:
            print("===================")
            print("\t\tSTAFF DASHBOARD")
            print("===================")
            print("-----------------")
            print(" 1. Table Booking")
            print("-----------------")
            print(" 2. order")
            print("-----------------")
            print(" 3. Logout")
            print("-----------------")
            
            choice = input("Enter your choice :")
            
            if choice == "1":
                pass
            
            elif choice == "2":
                pass
            
            elif choice == "3":
                break
            
            else:
                validation_log("Invalid choice")
                print("--------------")
                print("invalid choice")
                print("--------------")
    
    except Exception as f:
        Error_log(str(f))
        print("--------------------")
        print("Something went wrong")
        print("--------------------")
