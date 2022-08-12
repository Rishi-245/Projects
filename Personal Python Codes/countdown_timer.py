#Countdown Timer

import time
import sys
repeat = True

while repeat == True:
    def countdown(t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
      
        print("Time's Up!")
        user = input("Do you want to use the timer again? y or n?")
        if user == "y" or user == "yes" or user == "Y":
            repeat = True
        else:
            sys.exit()
  
    t = input("Enter the time in seconds: ")
    countdown(int(t))
