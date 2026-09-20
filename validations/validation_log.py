import datetime
import os

def validation_log(message):

    time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    path = os.getcwd()

    with open("logs/validation.txt", "a") as file:
        file.write("==================================================\n")
        file.write("TIME  : " + time + "\n")
        file.write("PATH  : " + path + "\n")
        file.write("ERROR : " + message + "\n")
        file.write("==================================================\n\n")

def Error_log(message):
    
    time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    path = os.getcwd()
    
    with open("logs/error.txt", "a") as file:
        file.write("==================================================\n")
        file.write("TIME  : " + time + "\n")
        file.write("PATH  : " + path + "\n")
        file.write("ERROR : " + message + "\n")
        file.write("==================================================\n\n")