import json
from app.validations.validation_log import Error_log

def generate_bill():
    try:
        with open("app/database/order.json", "r") as file:
            orders = json.load(file)

        order_id = input("Enter Order ID : ").strip()

        for order in orders:
            if order["order_id"] == order_id:

                if order["status"] == "Cancelled":
                    print("-----------------------------")
                    print("Cancelled order cannot generate bill")
                    print("-----------------------------")
                    return

                total = 0

                print("\n==================================================")
                print("              RESTAURANT BILL")
                print("==================================================")
                print("Order ID :", order["order_id"])
                print("Table ID :", order["table_id"])
                print("Order Time :", order["order_time"])
                print("--------------------------------------------------")
                print("Item                  Qty    Price       Amount")
                print("--------------------------------------------------")

                for item in order["items"]:
                    amount = item["price"] * item["quantity"]
                    total = total + amount

                    print(item["name"],"x",item["quantity"],"₹",item["price"],"Amount : ₹",amount)

                print("--------------------------------------------------")

                print("Subtotal :", total)

                discount = input("Enter Discount (%) : ")

                if discount == "":
                    discount = 0
                else:
                    discount = float(discount)

                discount_amount = total * discount / 100
                taxable_amount = total - discount_amount

                gst_rate = 5

                gst = taxable_amount * gst_rate / 100

                final_total = taxable_amount + gst

                print("Discount :", discount, "%")
                print("Discount Amount : ₹", discount_amount)

                print("--------------------------------------------------")

                print("Taxable Amount : ₹", taxable_amount)
                print("GST (5%) : ₹", gst)

                print("--------------------------------------------------")

                print("GRAND TOTAL : ₹", final_total)

                print("==================================================")
                print("                 THANK YOU!")
                print("==================================================")
                return

        print("-----------------------------")
        print("Order ID not found")
        print("-----------------------------")

    except Exception as f:
        Error_log(str(f))
        print("-----------------------------")
        print("Something went wrong")
        print("-----------------------------")

def payment():
    try:
        with open("app/database/order.json", "r") as file:
            orders = json.load(file)

        order_id = input("Enter Order ID : ").strip()

        for order in orders:

            if order["order_id"] == order_id:

                if order["status"] == "Cancelled":
                    print("-----------------------------------")
                    print("Cancelled order cannot make payment")
                    print("-----------------------------------")
                    return

                if order["status"] == "Completed":
                    print("-----------------------------")
                    print("Payment already completed")
                    print("-----------------------------")
                    return

                subtotal = 0

                for item in order["items"]:
                    amount = item["price"] * item["quantity"]
                    subtotal = subtotal + amount

                discount = input("Enter Discount (%) : ")

                if discount == "":
                    discount = 0
                else:
                    discount = float(discount)

                discount_amount = subtotal * discount / 100

                taxable_amount = subtotal - discount_amount

                gst_rate = 5

                gst = taxable_amount * gst_rate / 100

                final_total = taxable_amount + gst

                print("\n========================================")
                print("              PAYMENT")
                print("========================================")
                print("Order ID :", order["order_id"])
                print("Table ID :", order["table_id"])
                print("Subtotal : ₹", subtotal)
                print("Discount : ₹", discount_amount)
                print("GST : ₹", gst)
                print("Final Amount : ₹", final_total)
                print("========================================")

                print("1. Cash")
                print("2. UPI")
                print("3. Card")

                choice = input("Enter Payment Method : ")

                if choice == "1":
                    payment_method = "Cash"

                elif choice == "2":
                    payment_method = "UPI"

                elif choice == "3":
                    payment_method = "Card"

                else:
                    print("-----------------------------")
                    print("Invalid Payment Method")
                    print("-----------------------------")
                    return

                print("-----------------------------")
                print("Processing Payment...")
                print("-----------------------------")

                payment = input("Confirm Payment? (yes/no) : ").lower()

                if payment == "yes":

                    order["status"] = "Completed"
                    order["payment_method"] = payment_method
                    order["payment_status"] = "Paid"
                    order["total_amount"] = final_total

                    with open("app/database/order.json", "w") as file:
                        json.dump(orders, file, indent=4)

                    print("\n========================================")
                    print("         PAYMENT SUCCESSFUL")
                    print("========================================")
                    print("Order ID :", order["order_id"])
                    print("Payment Method :", payment_method)
                    print("Amount Paid : ₹", final_total)
                    print("Payment Status : Paid")
                    print("Order Status : Completed")
                    print("========================================")

                else:
                    print("-----------------------------")
                    print("Payment cancelled")
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