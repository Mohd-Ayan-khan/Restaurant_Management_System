import json
import datetime
import datetime
from app.validations.validation_log import Error_log
from app.validations.validator import validator_functions


class Table:
    
    def view_All_table(self):
        
        with open("app/database/table.json",'r') as file:
            tables = json.load(file)
        
        print("\n———————————————————————————————————————————————————————————————————————")
        print("‖    table ID     ‖   Table Size    ‖   Capacity  ‖   Status   ‖")
        print("———————————————————————————————————————————————————————————————————————")
        
        
        for table in tables:
            print(
                    f"|\t {table['table_id']:<8} "
                    f"|\t {table['table_size']:<10} "
                    f"|\t {table['capacity']:<8} "
                    f"| {table['status']:<10} |"
                )
    
    def View_available_table(self):
        with open("app/database/table.json",'r') as file:
            tables = json.load(file)
        
        found = False
        print("\n———————————————————————————————————————————————————————————————————————")
        print("‖    table ID     ‖   Table Size    ‖   Capacity  ‖   Status   ‖")
        print("———————————————————————————————————————————————————————————————————————")
        for table in tables:
            if table["status"] == "Available":
                found = True
                print(
                        f"|\t {table['table_id']:<8} "
                        f"|\t {table['table_size']:<10} "
                        f"|\t {table['capacity']:<8} "
                        f"| {table['status']:<10} |"
                    )
                
        if found == False:
            print("————————————————————————————————")
            print("No Table Available in Resturant")
            print("————————————————————————————————")


    def view_booked_table(self):
        with open("app/database/table.json",'r') as file:
            tables = json.load(file)
        
        found = False
        print("\n———————————————————————————————————————————————————————————————————————")
        print("‖    table ID     ‖   Table Size    ‖   Capacity  ‖   Status   ‖")
        print("———————————————————————————————————————————————————————————————————————")
        for table in tables:
            if table["status"] == "Booked":
                found = True
                print(
                        f"|\t {table['table_id']:<8} "
                        f"|\t {table['table_size']:<10} "
                        f"|\t {table['capacity']:<8} "
                        f"| {table['status']:<10} |"
                    )
        
        if found == False:
            print("————————————————————————————————")
            print("No Booked Table in Resturant")
            print("————————————————————————————————")


    def cancel_table(self):
        try:
            with open("app/database/booking.json", "r") as file:
                bookings = json.load(file)

            with open("app/database/table.json", "r") as file:
                tables = json.load(file)

            booking_id = input("Enter Booking ID : ").strip()

            for booking in bookings:

                if booking["booking_id"] == booking_id:

                    if booking["status"] == "Cancelled":
                        print("-----------------------------")
                        print("Booking already cancelled")
                        print("-----------------------------")
                        return

                    for table_id in booking["table_ids"]:

                        for table in tables:

                            if table["table_id"] == table_id:
                                table["status"] = "Available"

                    booking["status"] = "Cancelled"

                    with open("app/database/table.json", "w") as file:
                        json.dump(tables, file, indent=4)

                    with open("app/database/booking.json", "w") as file:
                        json.dump(bookings, file, indent=4)

                    print("-----------------------------")
                    print("Booking cancelled successfully")
                    print("-----------------------------")
                    return

            print("-----------------------------")
            print("Booking ID not found")
            print("-----------------------------")

        except Exception as f:
            Error_log(str(f))
            print("---------------------")
            print("Something went wrong ")
            print("---------------------")

                 
    def book_table(self):
        try:
            
            obj = validator_functions()

            with open("app/database/table.json", "r") as file:
                tables = json.load(file)

            name = input("Enter Table Booker Name : ")
            phone = input("Enter your Phone Number : ")
            quantity = input("Enter Person Quantity : ")
            duration = input("Enter Table Booking Duration : ")

            name = obj.name_validate(name)
            phone = obj.phone_validate(phone)
            quantity = obj.quantity_validate(quantity)
            duration = obj.duration_validate(duration)

            quantity = int(quantity)

            available_tables = []

            for table in tables:

                if table["status"] == "Available":

                    table["table_id"] = table["table_id"]
                    table["capacity"] = table["capacity"]

                    available_tables.append(table)

            if len(available_tables) == 0:
                print("————————————————————————————————")
                print("No Table Available")
                print("————————————————————————————————")
                return

            total_available_capacity = 0

            for table in available_tables:
                total_available_capacity += table["capacity"]

            if total_available_capacity < quantity:
                print("————————————————————————————————")
                print("Not enough table capacity available")
                print("————————————————————————————————")
                return

            suitable_tables = []

            for table in available_tables:
                if table["capacity"] >= quantity:

                    suitable_tables.append(table)

            print("\n———————————————————————————————————————————————————————————————————————")
            print("                         SUITABLE TABLES")
            print("———————————————————————————————————————————————————————————————————————")
            print("‖    Table ID     ‖   Table Size    ‖   Capacity  ‖   Status   ‖")
            print("———————————————————————————————————————————————————————————————————————")

            if len(suitable_tables) > 0:

                for table in suitable_tables:

                    print(
                        f"‖ {table['table_id']:<15}"
                        f"‖ {table['table_size']:<15}"
                        f"‖ {table['capacity']:<11}"
                        f"‖ {table['status']:<10} ‖"
                    )

            else:

                print("No single table can suitable  all persons.")

            print("———————————————————————————————————————————————————————————————————————")

            recommended_tables = []
            recommended_capacity = 0

            if len(suitable_tables) > 0:

                best_table = suitable_tables[0]

                for table in suitable_tables:

                    if table["capacity"] < best_table["capacity"]:

                        best_table = table

                recommended_tables.append(best_table)
                recommended_capacity = best_table["capacity"]

            else:
                for table in available_tables:

                    if recommended_capacity < quantity:
                        recommended_tables.append(table)
                        recommended_capacity += table["capacity"]

            print("\n————————————————————————————————")
            print("Recommended Table(s)")
            print("————————————————————————————————")

            for table in recommended_tables:
                print(
                    "Table ID :", table["table_id"],
                    "| Size :", table["table_size"],
                    "| Capacity :", table["capacity"]
                )

            print("Total Capacity :", recommended_capacity)
            print("Required Capacity :", quantity)
            print("————————————————————————————————")

            choice = input("Do you want to book recommended table(s)? (yes/no) : ")

            selected_tables = []

            if choice.lower() == "yes":
                for table in recommended_tables:

                    selected_tables.append(table)

            elif choice.lower() == "no":
                while True:

                    print("\n————————————————————————————————")
                    print("Available Tables")
                    print("————————————————————————————————")

                    for table in available_tables:
                        already_selected = False

                        for selected in selected_tables:
                            if selected["table_id"] == table["table_id"]:

                                already_selected = True
                                break

                        if already_selected == False:

                            print(
                                "Table ID :", table["table_id"],
                                "| Size :", table["table_size"],
                                "| Capacity :", table["capacity"]
                            )

                    print("————————————————————————————————")

                    table_id = input("Enter Table ID to book : ").strip()

                    selected_table = None

                    for table in available_tables:

                        if str(table["table_id"]) == str(table_id):
                            already_selected = False

                            for selected in selected_tables:

                                if selected["table_id"] == table_id:

                                    already_selected = True
                                    break

                            if already_selected == False:
                                selected_table = table

                            break

                    if selected_table is None:
                        print("————————————————————————————————")
                        print("Invalid or already selected Table ID")
                        print("————————————————————————————————")
                        continue

                    selected_tables.append(selected_table)

                    total_selected_capacity = 0

                    for table in selected_tables:

                        total_selected_capacity += table["capacity"]

                    print("————————————————————————————————")
                    print("Table Added :", selected_table["table_id"])
                    print("Total Capacity :", total_selected_capacity)
                    print("Required Capacity :", quantity)
                    print("————————————————————————————————")

                    if total_selected_capacity >= quantity:
                        break

                    more = input("Capacity is not enough. ""Do you want to book another table? (yes/no) : ")

                    if more.lower() != "yes":
                        print("————————————————————————————————")
                        print("Booking Cancelled")
                        print("————————————————————————————————")
                        return

            else:
                print("————————————————————————————————")
                print("Please enter yes or no")
                print("————————————————————————————————")
                return

            total_selected_capacity = 0

            for table in selected_tables:

                total_selected_capacity += table["capacity"]

            if total_selected_capacity < quantity:
                print("————————————————————————————————")
                print("Selected tables capacity is not enough")
                print("————————————————————————————————")
                return

            print("\n————————————————————————————————")
            print("Selected Tables")
            print("————————————————————————————————")

            for table in selected_tables:

                print("Table ID :", table["table_id"],"| Size :", table["table_size"],"| Capacity :", table["capacity"])

            print("————————————————————————————————")
            print("Total Capacity :", total_selected_capacity)
            print("Person Quantity :", quantity)
            print("Duration :", duration, "Hours")
            print("————————————————————————————————")

            confirm = input("Do you want to confirm this booking? (yes/no) : ")

            if confirm.lower() != "yes":
                print("————————————————————————————————")
                print("Booking Cancelled")
                print("————————————————————————————————")
                return

            for selected_table in selected_tables:

                for table in tables:

                    if table["table_id"] == selected_table["table_id"]:

                        if table["status"] != "Available":

                            print("————————————————————————————————")
                            print("Table",table["table_id"],"is no longer available")
                            print("————————————————————————————————")
                            return

                        break

            try:
                with open("app/database/booking.json", "r") as file:
                    bookings = json.load(file)

            except FileNotFoundError:

                bookings = []

            if len(bookings) == 0:
                booking_id = "1"

            else:
                max_id = 0

                for booking in bookings:
                    if "booking_id" in booking:

                        try:
                            current_id = int(booking["booking_id"])
                            if current_id > max_id:
                                max_id = current_id

                        except ValueError:
                            pass

                booking_id = max_id + 1

            table_ids = []

            for table in selected_tables:

                table_ids.append(str(table["table_id"]))

            booking_time = datetime.datetime.now()
            time = datetime.timedelta(hours=duration)
            end_time = booking_time + time

            booking = {
                "booking_id": booking_id,
                "name": name,
                "phone": phone,
                "quantity": quantity,
                "table_ids": table_ids,
                "duration": duration,
                "booking_time": booking_time.strftime("%d-%m-%Y %I:%M:%S %p"),
                "end_time": end_time.strftime("%d-%m-%Y %I:%M:%S %p"),
                "status": "Booked"
            }

            bookings.append(booking)

            for selected_table in selected_tables:

                for table in tables:

                    if table["table_id"] == selected_table["table_id"]:
                        table["status"] = "Booked"
                        break

            with open("app/database/booking.json", "w") as file:
                json.dump(bookings,file,indent=4)

            with open("app/database/table.json", "w") as file:
                json.dump(tables,file,indent=4)

            print("\n————————————————————————————————")
            print("       Table Booked Successfully")
            print("————————————————————————————————")
            print("Booking ID :", booking_id)
            print("Name :", name)
            print("Phone :", phone)
            print("Person Quantity :", quantity)
            print("Table IDs :", ", ".join(table_ids))
            print("Total Capacity :", total_selected_capacity)
            print("Duration :", duration, "Hours")
            print("Booking Time :", booking["booking_time"])
            print("End Time :", booking["end_time"])
            print("Status : Booked")
            print("————————————————————————————————")

        except Exception as f:
            Error_log(str(f))
            print("————————————————————————————————")
            print("Something went wrong :", str(f))
            print("————————————————————————————————")
    
    