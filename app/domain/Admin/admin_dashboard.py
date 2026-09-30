from app.validations.validation_log import Error_log
from app.validations.validation_log import validation_log
from app.domain.Admin.menu_management import menu_management
from app.domain.Admin.staff_management import staff_management
from app.domain.Admin.inventory_management import inventory

class Admin(inventory):
    def menu_mangement_dashbord(self):
        
        try:
            while True:
                        print("\n**********************")
                        print(" -- Menu Management --")
                        print("**********************")
                        print("1. -- Update Item --")
                        print("----------------------")
                        print("2. -- Add Item --")
                        print("----------------------")
                        print("3. -- Delete Item --")
                        print("----------------------")
                        print("4. -- View Items --")
                        print("----------------------")
                        print("5. -- Exit --")
                        print("----------------------")
                            
                        choice = input("Enter your choice :")
                        obj = menu_management()
                            
                        if choice == "1":
                            obj.update_item()
                            
                        elif choice == "2":
                            obj.add_item()
                            
                        elif choice == "3":
                            obj.delete_item()
                            
                        elif choice == "4":
                            obj.item_view()
                        
                        elif choice == "5":
                            break
                            
                        else:
                            validation_log("invalid choice")
                            print("**************")
                            print("Invalid Number")
                            print("**************")
                        
        except Exception as f:
            Error_log(str(f))
            print("\n--------------------")
            print("Error :",f)
            print("--------------------")
    
    
    def staff_management_dashboard(self):
        try:
            while True:
                print("\n************************")
                print(" -- Staff Management -- ")
                print("************************")
                print("1. -- ADD Staff --")
                print("------------------------")
                print("2. -- UPDATE Staff --")
                print("------------------------")
                print("3. -- DELETE Staff --")
                print("------------------------")
                print("4. -- VIEW Staff --")
                print("------------------------")
                print("5. -- SEARCH Staff")
                print("------------------------")
                print("6. -- Exit --")
                print("------------------------")
                
                
                choice = input("Enter your choice :")
                obj = staff_management()
                
                if choice == "1":
                    obj.add_staff()
                
                elif choice == "2":
                    obj.update_staff()
                
                elif choice == "3":
                    obj.delete_staff()
                
                elif choice == "4":
                    obj.view_staff()
                
                elif choice == "5":
                    obj.search_staff()
                    
                elif choice == "6":
                    break
                
                else:
                    print("Invalid choice")
        except Exception as f:
            Error_log(str(f))
            print("\n--------------------")
            print("somthin went wrong")
            print("--------------------")
    
    def inventory_management(self):
        try:
            while True:
                print("\n===========================")
                print(" -- Inventory Management --")
                print("=============================")
                print("1. -- Add Item --")
                print("-----------------------------")
                print("2. -- Update Item --")
                print("-----------------------------")
                print("3. -- Delete Item --")
                print("-----------------------------")
                print("4. -- Exit --")
                print("-----------------------------")
                
                choice = input("Enter your choice :")
                
                if choice == "1":
                    pass
                
                elif choice == "2":
                    pass
                
                elif choice == "3":
                    pass
                
                elif choice == "4":
                    break
                
                else:
                    validation_log("invalid choice")
                    print("**************")
                    print("Invalid choice")
                    print("**************")
        
        except Exception as f:
            Error_log(str(f))
            print("-------------------")
            print("somthing went wrong")
            print("-------------------")
            
    def admin_dashboard(self):
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
                        self.menu_mangement_dashbord()
                    
                    elif choice == "2":
                        self.staff_management_dashboard()
                    
                    elif choice == "3":
                        inventory().add_item()
                    
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
            print("Error :",f)
            print("--------------------")