from app.validations.validation_log import Error_log
from app.validations.validator import validator_functions
import json
import datetime

class order:
     
    def view_menu(self):
        try:
            with open("app/database/menu.json", "r") as file:
                menu = json.load(file)

            category = ""

            for item in menu:

                if item["category"] != category:
                    category = item["category"]

                    print("\n====================")
                    print(category)
                    print("====================")

                print(item["id"], item["name"], "₹", item["price"])
        
        except Exception as f:
            Error_log(str(f))
            print("-------------------")
            print("somthing went wrong")
            print("-------------------")
    
    
    def place_order(self):
        try:
            with open("app/database/table.json", "r") as file:
                tables = json.load(file)

            table_id = input("Enter Table ID : ").strip()
            table_found = False

            for table in tables:
                if table["table_id"] == table_id:

                    table_found = True

                    if table["status"] != "Booked":
                        print("-----------------------------")
                        print("Please book the table first")
                        print("-----------------------------")
                        return

                    break

            if table_found == False:
                print("-----------------------------")
                print("Table ID not found")
                print("-----------------------------")
                return

            with open("app/database/menu.json", "r") as file:
                menu = json.load(file)

            
            with open("app/database/order.json", "r") as file:
                orders = json.load(file)


            order_id = len(orders) + 1

            items = []

            while True:
                self.view_menu()

                item_id = input("\nEnter Item ID : ").strip()

                found = False

                for item in menu:

                    if item["id"] == item_id and item["isAvailable"] == True:

                        found = True

                        quantity = input("Enter Quantity : ")
                        quantity = validator_functions().quantity_validate(quantity)

                        order_item = {
                            "item_id": item["id"],
                            "name": item["name"],
                            "price": item["price"],
                            "category":item["category"],
                            "quantity": quantity
                        }

                        items.append(order_item)
                        print("-----------------------------")
                        print("Item added successfully")
                        print("-----------------------------")
                        break

                if found == False:
                    print("-----------------------------")
                    print("Invalid Item ID")
                    print("-----------------------------")
                    continue

                choice = input("Do you want to add another item? (yes/no) : ").lower()

                if choice == "no":
                    break

            order_time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

            order_data = {
                "order_id": order_id,
                "table_id": table_id,
                "items": items,
                "status": "Pending",
                "order_time": order_time
            }

            orders.append(order_data)

            print("—————————————————————————————")
            print("Order placed successfully")
            print("—————————————————————————————")
            print("Order ID :", order_id)
            print("Table ID :", table_id)
            print("order items :")
            for item in items:
                print(item["name"], "x" , item["quantity"])
            print("—————————————————————————————")
            
            
            with open("app/database/order.json", "w") as file:
                json.dump(orders, file, indent=4)

        except Exception as f:
            Error_log(str(f))
            print("-----------------------")
            print("Something went wrong ")
            print("-----------------------")
    
    
    def update_order(self):
        try:
            with open("app/database/order.json", "r") as file:
                orders = json.load(file)

            order_id = input("Enter Order ID : ").strip()

            for order in orders:
                if order["order_id"] == order_id:

                    if order["status"] == "Cancelled":
                        print("-----------------------------")
                        print("Cancelled order cannot be updated")
                        print("-----------------------------")
                        return

                    print("\n-----------------------------")
                    print("Order ID :", order["order_id"])
                    print("Table ID :", order["table_id"])
                    print("Status :", order["status"])
                    print("-----------------------------")

                    for item in order["items"]:
                        print(
                            "Item ID :", item["item_id"],
                            "|", item["name"],
                            "| Quantity :", item["quantity"]
                        )
                    print("-----------------------------")

                    item_id = input("Enter Item ID to update : ").strip()

                    for item in order["items"]:

                        if item["item_id"] == item_id:

                            quantity = input("Enter New Quantity : ")
                            quantity = validator_functions().quantity_validate(quantity)
                            item["quantity"] = quantity

                            with open("app/database/order.json", "w") as file:
                                json.dump(orders, file, indent=4)

                            print("-----------------------------")
                            print("Order updated successfully")
                            print("-----------------------------")
                            return

                    print("-----------------------------")
                    print("Item ID not found")
                    print("-----------------------------")
                    return

            print("-----------------------------")
            print("Order ID not found")
            print("-----------------------------")

        except Exception as f:
            Error_log(str(f))
            print("-----------------------------")
            print("Something went wrong")
            print("-----------------------------")
    
    
    def delete_order(self):
        try:
            with open("app/database/order.json", "r") as file:
                orders = json.load(file)

            order_id = input("Enter Order ID : ").strip()

            for order in orders:
                if order["order_id"] == order_id:

                    orders.remove(order)

                    with open("app/database/order.json", "w") as file:
                        json.dump(orders, file, indent=4)

                    print("-----------------------------")
                    print("Order deleted successfully")
                    print("-----------------------------")
                    return

            print("-----------------------------")
            print("Order ID not found")
            print("-----------------------------")

        except Exception as f:
            Error_log(str(f))
            print("-----------------------------")
            print("Something went wrong")
            print("-----------------------------")