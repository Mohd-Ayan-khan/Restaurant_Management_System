from validations.validation_log import Error_log
from validations.validation_log import validation_log

def admin_dashboard():
    try:
        while True:
                print("\n========================")
                print("   ADMIN DASHBOARD")
                print("========================")
                print("------------------------")
                print(" 1. Menu Management")
                print("------------------------")
                print(" 2. Staff Management")
                print("------------------------")
                print(" 3. Inventory Management")
                print("------------------------")
                print(" 4. View Table Booking")
                print("------------------------")
                print(" 5. View Order")
                print("------------------------")
                print(" 6. Exit")
                print("------------------------")
                
                choice = input("Enter your Choice :")
                
                if choice == "1":
                    pass
                
                elif choice == "2":
                    pass
                
                elif choice == "3":
                    pass
                
                elif choice == "4":
                    pass
                
                elif choice == "5":
                    pass
                
                elif choice == "6":
                    break
                
                else:
                    validation_log("invalid choice")
                    print("--------------")
                    print("Invalid choice")
                    print("--------------")

    except Exception as f:
        Error_log(str(f))
        print("--------------------")
        print("Something went wrong")
        print("--------------------")