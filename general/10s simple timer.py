#create a def for a 10s timer
import time

def timer():
    secs = 10
    while secs > 0:
        print(f"{secs:02d}", end='\r')
        time.sleep(1)
        secs -= 1

    return print("Time's up!")

timer()

