import time
import datetime

def countdown(h, m, s):
    total_seconds = h * 3600 + m * 60 + s

    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)

        print(timer, end="\r")

        time.sleep(1)

        total_seconds -= 1

    print("The countdown is at zero dude")

h = input("Enter the time in hours dude: ")
m = input("Enter the time in minutes now dude: ")
s = input("Enter the time in seconds please dude: ")
countdown(int(h), int(m), int(s))

