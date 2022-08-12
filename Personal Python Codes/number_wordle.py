# Wordle ~ For Numbers

import random
import sys

num_range=eval(input("Enter the range in a list. Ex: [1,100]\n"))
types=type(num_range)

if type(num_range) != list:
    print("Error. Please Enter a Valid List Input.")
    sys.exit()
    
lowest=num_range[0]
highest=num_range[1]
rand_num=random.randint(lowest,highest)
repeat = True

while repeat == True:
    if type(num_range) == list:
        guess=eval(input("Guess a Number Inside of the Range\n"))

        if guess == rand_num:
            print("You win! The number was", rand_num)
            repeat = False
        
        elif guess < rand_num:
            print("Your guess was smaller. Guess again.")

        elif guess > rand_num:
            print("Your guess was greater. Guess again.")
               
    else:
        print("Error. Please Enter a Valid List Input.")
        break
