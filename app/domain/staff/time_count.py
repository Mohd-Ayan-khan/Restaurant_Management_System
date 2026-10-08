from app.validations.validation_log import Error_log
import json
import datetime

def update_table_status():
    try:
        with open("app/database/booking.json", "r") as file:
            bookings = json.load(file)

        with open("app/database/table.json", "r") as file:
            tables = json.load(file)

        current_time = datetime.datetime.now()

        for booking in bookings:
            if booking["status"] == "Booked":

                end_time = datetime.datetime.strptime(booking["end_time"],"%d-%m-%Y %I:%M:%S %p")

                if current_time >= end_time:
                    
                    for table_id in booking["table_ids"]:
                        for table in tables:

                            if table["table_id"] == table_id:
                                table["status"] = "Available"
                                break

                    booking["status"] = "Completed"

        with open("app/database/table.json", "w") as file:
            json.dump(tables, file, indent=4)

        with open("app/database/booking.json", "w") as file:
            json.dump(bookings, file, indent=4)

    except Exception as f:
        Error_log(str(f))
        print("-----------------------------")
        print("Something went wrong")
        print("-----------------------------")