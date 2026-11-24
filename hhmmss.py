from datetime import datetime

def getTimes():
    def ask_time(prompt):
        while True:
            value = input(prompt)
            try:
                datetime.strptime(value, "%H:%M:%S")
                return value
            except valueError:
                print("Invalid time, Use HH:MM:SS, with valid hours, minutes and seconds.")

    while True:
        startTime = ask_time("Enter the start time (HH:MM:SS): ")
        endTime = ask_time("Enter the end time (HH:MM:SS): ")
        
         