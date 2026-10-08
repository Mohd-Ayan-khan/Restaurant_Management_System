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
                    print("\n========================================")
                    print("   Cancelled order cannot generate bill")
                    print("========================================")
                    return

                if order.get("payment_status") == "Paid":
                    print("\n========================================")
                    print("       Payment already completed")
                    print("========================================")
                    return

                total = 0

                print("\n======================================================")
                print("                 RESTAURANT BILL")
                print("======================================================")
                print("Order ID    :", order["order_id"])
                print("Table ID    :", order["table_id"])
                print("Order Time  :", order["order_time"])
                print("------------------------------------------------------")
                print(f"{'Item':<25}{'Qty':>5}{'Price':>12}{'Amount':>15}")
                print("------------------------------------------------------")

                for item in order["items"]:

                    amount = item["price"] * item["quantity"]

                    total = total + amount

                    print(
                        f"{item['name']:<25}"
                        f"{item['quantity']:>5}"
                        f"{'₹' + format(item['price'], '.2f'):>12}"
                        f"{'₹' + format(amount, '.2f'):>15}"
                    )

                print("------------------------------------------------------")

                print(f"{'Subtotal':<45}₹{total:.2f}")

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
                final_total = round(final_total, 2)

                print(f"{'Discount':<45}{discount:.2f}%")
                print(f"{'Discount Amount':<45}₹{discount_amount:.2f}")

                print("------------------------------------------------------")

                print(f"{'Taxable Amount':<45}₹{taxable_amount:.2f}")
                print(f"{'GST (5%)':<45}₹{gst:.2f}")

                print("------------------------------------------------------")

                print(f"{'GRAND TOTAL':<45}₹{final_total:.2f}")

                print("======================================================")
                print("                     PAYMENT")
                print("======================================================")

                print("1. Cash")
                print("2. UPI")
                print("3. Card")

                payment_choice = input("Enter Payment Method : ")

                if payment_choice == "1":
                    payment_method = "Cash"

                elif payment_choice == "2":
                    payment_method = "UPI"

                elif payment_choice == "3":
                    payment_method = "Card"

                else:

                    print("\n========================================")
                    print("       Invalid Payment Method")
                    print("========================================")
                    return

                print(f"\nAmount to Pay : ₹{final_total:.2f}")

                confirm = input("Confirm Payment? (yes/no) : ").lower()

                if confirm == "yes":

                    order["status"] = "Completed"
                    order["payment_status"] = "Paid"
                    order["payment_method"] = payment_method
                    order["total_amount"] = round(final_total, 2)

                    with open("app/database/order.json", "w") as file:
                        json.dump(orders, file, indent=4)

                    print("\n======================================================")
                    print("                 PAYMENT SUCCESSFUL")
                    print("======================================================")

                    print("Order ID       :", order["order_id"])
                    print("Payment Method :", payment_method)
                    print(f"Amount Paid    : ₹{final_total:.2f}")
                    print("Payment Status : Paid")
                    print("Order Status   : Completed")

                    print("======================================================")
                    print("                    THANK YOU!")
                    print("======================================================")

                else:

                    print("\n========================================")
                    print("          Payment cancelled")
                    print("========================================")

                return

        print("\n========================================")
        print("           Order ID not found")
        print("========================================")

    except Exception as f:
        Error_log(str(f))
        print("\n========================================")
        print("          Something went wrong")
        print("========================================")