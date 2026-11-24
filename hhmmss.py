from datetime import datetime

def getTimes():
    def ask_time(prompt):
        while True:
            value = input(prompt)
            try:
                datetime.strptime(value, "%H:%M:%S")
                return value
            except ValueError:
                print("Invalid time, Use HH:MM:SS, with valid hours, minutes and seconds.")

    while True:
        startTime = ask_time("Enter the start time (HH:MM:SS): ")
        endTime = ask_time("Enter the end time (HH:MM:SS): ")

        startSeconds = sum(
            int(part) * factor
            for part, factor in zip(startTime.split(":"), (3600, 60, 1))
        )

        endSeconds = sum(
            int(part) * factor
            for part, factor in zip(endTime.split(":"), (3600, 60, 1))
        )

        if endSeconds > startSeconds:
            return startSeconds, endSeconds

        print("The end time must be later than the start time.")


