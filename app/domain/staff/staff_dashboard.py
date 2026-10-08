from app.validations.validation_log import validation_log
from app.validations.validation_log import Error_log
from app.domain.Admin.menu_management import menu_management
from app.domain.Admin.inventory_management import inventory
from app.domain.staff.order_management import order
from app.domain.staff.table_management import Table
from app.domain.staff.billing import generate_bill
class staff(order,menu_management,inventory):
    
    def Table_dashboard(self):
        obj = Table()
        try:
            while True:
                print("\n——————————————————————————")
                print("\tTable Management")
                print("——————————————————————————")
                print("1. Table Booking")
                print("--------------------------")
                print("2. cencle Table ")
                print("--------------------------")
                print("3. View All Tables")
                print("--------------------------")
                print("4. View Booked Table")
                print("--------------------------")
                print("5. View Available Table")
                print("--------------------------")
                print("6. Exit")
                print("--------------------------")
                
                
                choice = input("Enter your choice :")
                
                if choice == "1":
                    obj.book_table()
                
                elif choice == "2":
                    obj.cancel_table()
                
                elif choice == "3":
                    obj.view_All_table()
                
                elif choice == "4":
                    obj.view_booked_table()
                
                elif choice == "5":
                    obj.View_available_table()
                
                elif choice == "6":
                    break
                
                else:
                    print("invalid  choice")
        
        except Exception as f:
            Error_log(str(f))
            print("-------------------")
            print("Somthing went wrong")
            print("-------------------")      
    
    def order_dashboard(self):
        try:
            while True:
                print("\n========================")
                print(" -- Order Management -- ")
                print("========================")
                print("1. -- Order book --")
                print("------------------------")
                print("2. -- Update Order --")
                print("------------------------")
                print("3. -- Cencle Order")
                print("------------------------")
                print("4. -- View Menu --")
                print("------------------------")
                print("5. -- view Orders --")
                print("------------------------")
                print("6. -- Exit --")
                print("------------------------")
                
                choice = input("Enter your Choice :")
                
                if choice == "1":
                    order().place_order()
                
                elif choice == "2":
                    order().update_order()
                
                elif choice == "3":
                    order().delete_order()
                
                elif choice == "4":
                    self.view_menu()
                
                elif choice == "5":
                    order().view_order()
                    
                elif choice == "6":
                    break
                
                else:
                    validation_log("invalid choice")
                    print("\n--------------")
                    print("Invalid Choice")
                    print("--------------")
        
        except Exception as f:
            Error_log(str(f))
            print("\n-------------------")
            print("somthing went wrong")
            print("-------------------")
            
            
    def staff_dashboard(self):
        try:
            while True:
                print("\n===========================")
                print("\tSTAFF DASHBOARD")
                print("===========================")
                print("--------------------")
                print(" 1. Table Management")
                print("--------------------")
                print(" 2. order Management")
                print("--------------------")
                print(" 3. view Menu")
                print("--------------------")
                print(" 4. view Inventory")
                print("--------------------")
                print(" 5. Billing")
                print("--------------------")
                print(" 6. Exit")
                print("--------------------")
                
                choice = input("Enter your choice :")
                
                if choice == "1":
                    self.Table_dashboard()
                
                elif choice == "2":
                    self.order_dashboard()
                
                elif choice == "3":
                    self.view_menu()
                
                elif choice == "4":
                    self.view_inventory()
                
                elif choice == "5":
                    generate_bill()
                
                elif choice == "6":
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