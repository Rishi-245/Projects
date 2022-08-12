#Rock Paper Scissors Game

import random
import sys

ans_yes = ["yes", "y", "Y"]
ans_no = ["no", "n", "N"]
repeat = True

while repeat == True:
    
    user=input("Rock, Paper or Scissors?\n").lower()
    choices=["rock", "paper", "scissors"]
    computer=random.choice(choices)
    print("You chose", user, "and the computer chose", computer)

    if user != computer:
        if user == "rock":
            if computer == "scissors":
                print("You Win :) Computer Loses!")
                user = input("Would you like to try again? y or n?")
                if user in ans_yes:
                    repeat = True
                elif user in ans_no:
                    repeat = False
                else:
                    sys.exit()
            else:
                print("You Lose :( Computer Wins!")
                user = input("Would you like to try again? y or n?")
                if user in ans_yes:
                    repeat = True
                elif user in ans_no:
                    repeat = False
                else:
                    sys.exit()
                    
        elif user == "paper":
            if computer == "scissors":
                print("You Lose :( Computer Wins!")
                user = input("Would you like to try again? y or n?")
                if user in ans_yes:
                    repeat = True
                elif user in ans_no:
                    repeat = False
                else:
                    sys.exit()
                    
            else:
                print("You win :) Computer Loses!")
                user = input("Would you like to try again? y or n?")
                if user in ans_yes:
                    repeat = True
                elif user in ans_no:
                    repeat = False
                else:
                    sys.exit()

        elif user == "scissors":
            if computer == "rock":
                print("You lose :( Computer Wins!")
                user = input("Would you like to try again? y or n?")
                if user in ans_yes:
                    repeat = True
                elif user in ans_no:
                    repeat = False
                else:
                    sys.exit()
                    
            else:
                print("You win :) Computer Loses!")
                user = input("Would you like to try again? y or n?")
                if user in ans_yes:
                    repeat = True
                elif user in ans_no:
                    repeat = False
                else:
                    sys.exit

    else:
        print("Tie Game! You both chose",user)
        user = input("Would you like to try again? y or n?")
        if user in ans_yes:
            repeat = True
        elif user in ans_no:
            repeat = False
        else:
            sys.exit()


print("Thank you for playing!")
