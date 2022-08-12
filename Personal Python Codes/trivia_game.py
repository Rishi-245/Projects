#Trivia Game

import time
import sys
import random

#CHECK FOR DESIRED NUMBER OF PLAYERS AND QUESTIONS
holder1 = True
holder2 = True

print("Reminder: If you're playing with 3 Players the only available choice is 3 questions.")

while holder1 == True:
    num_questions = eval(input("How many questions do you want? 3, 5 or 7?\n"))
    if num_questions == 3 or num_questions == 5 or num_questions == 7:
        holder1 = False
    else:
        print("Please select the number of questions from the given list. 3, 5, or 7.")
        holder1 = True

while holder2 == True:
    players = eval(input("How many players are going to play the game? Max = 3\n"))

    if players>3 or players <=0:
        print("Please select a the number of players between 1 and 3.")
        holder2 = True
    else:
        holder2 = False

if players == 3 and num_questions != 3:
    print("Reminder: If you're playing with 3 Players the only available choice is 3 questions.")
    sys.exit()

#THE QUESTIONS & ANSWERS
question_1 = "How many goals did Cristiano Ronaldo score in his life?" 
answer_1 = "807"

question_2 = "What is the capital city of Australia?" 
answer_2 = "canberra"

question_3 = "What year did WWI start?" 
answer_3 = "1914"

question_4 = "If your 12 and your brother is half your age. When your 36, how old is your brother?" 
answer_4 = "30"

question_5 = "What has a neck but no head?"
answer_5 = "shirt"

question_6 = "Which bow cannot be tied?" 
answer_6 = "rainbow"

question_7 = "What is dirty when it is white?" 
answer_7 = "blackboard"

#GAME INSTRUCTIONS
print("Before we begin the game, here are a rules to take note of.")
time.sleep(3)
print("Make sure to check grammar before entering your answer. All answers are one word answers. ")
time.sleep(3)
print("Now that you know the rules, lets begin with our first question!")
time.sleep(3)

#GAME CODE

#1 PLAYER GAME CODE - FOR 3, 5, AND 7 QUESTIONS
if players == 1:
    p1 = 0
    if num_questions == 3:

        print("",question_1, sep = "\n")
        q1 = input("Answer: ").lower()
        if q1 == answer_1:
            p1 += 1
            print("Correct!")
        else:
            print("Incorrect.")

        time.sleep(2)
        
        print("",question_2, sep = "\n")
        q2 = input("Answer: ").lower()
        if q2 == answer_2:
            p1 += 1
            print("Correct!")
        else:
            print("Incorrect.")

        time.sleep(2)

        print("",question_3, sep = "\n")
        q3 = input("Answer: ").lower()
        if q3 == answer_3:
            p1 += 1
            print("Correct!")
        else:
            print("Incorrect.")

        print("\nYou scored",p1,"out of",num_questions)
        print("Your score: ","{:.0%}".format(p1/num_questions))

    elif num_questions == 5:

        print("",question_1, sep = "\n")
        q1 = input("Answer: ").lower()
        if q1 == answer_1:
            p1 += 1
            print("Correct!")
        else:
            print("Incorrect.")

        time.sleep(2)
        
        print("",question_2, sep = "\n")
        q2 = input("Answer: ").lower()
        if q2 == answer_2:
            p1 += 1
            print("Correct!")
        else:
            print("Incorrect.")

        time.sleep(2)

        print("",question_3, sep = "\n")
        q3 = input("Answer: ").lower()
        if q3 == answer_3:
            p1 += 1
            print("Correct!")
        else:
            print("Incorrect.")

        time.sleep(2)

        print("",question_4, sep = "\n")
        q4 = input("Answer: ").lower()
        if q4 == answer_4:
            p1 += 1
            print("Correct!")
        else:
            print("Incorrect.")

        time.sleep(2)

        print("",question_5, sep = "\n")
        q5 = input("Answer: ").lower()
        if q5 == answer_5:
            p1 += 1
            print("Correct!")
        else:
            print("Incorrect.")
            
        print("\nYou scored",p1,"out of",num_questions)
        print("Your score: ","{:.0%}".format(p1/num_questions))

    elif num_questions == 7:

        print("",question_1, sep = "\n")
        q1 = input("Answer: ").lower()
        if q1 == answer_1:
            p1 += 1
            print("Correct!")
        else:
            print("Incorrect.")

        time.sleep(2)
        
        print("",question_2, sep = "\n")
        q2 = input("Answer: ").lower()
        if q2 == answer_2:
            p1 += 1
            print("Correct!")
        else:
            print("Incorrect.")

        time.sleep(2)

        print("",question_3, sep = "\n")
        q3 = input("Answer: ").lower()
        if q3 == answer_3:
            p1 += 1
            print("Correct!")
        else:
            print("Incorrect.")

        time.sleep(2)

        print("",question_4, sep = "\n")
        q4 = input("Answer: ").lower()
        if q4 == answer_4:
            p1 += 1
            print("Correct!")
        else:
            print("Incorrect.")

        time.sleep(2)

        print("",question_5, sep = "\n")
        q5 = input("Answer: ").lower()
        if q5 == answer_5:
            p1 += 1
            print("Correct!")
        else:
            print("Incorrect.")

        time.sleep(2)

        print("",question_6, sep = "\n")
        q6 = input("Answer: ").lower()
        if q6 == answer_6:
            p1 += 1
            print("Correct!")
        else:
            print("Incorrect.")

        time.sleep(2)

        print("",question_7, sep = "\n")
        q7 = input("Answer: ").lower()
        if q7 == answer_7:
            p1 += 1
            print("Correct!")
        else:
            print("Incorrect.")
            
        print("\nYou scored",p1,"out of",num_questions)
        print("Your score: ","{:.0%}".format(p1/num_questions))

#2 PLAYER GAME CODE - FOR 3, 5, AND 7 QUESTIONS
elif players == 2:
    p1 = 0
    p2 = 0

    if num_questions == 3:

        print("",question_1, sep = "\n")
        q1_1 = input("Player 1's Answer: ").lower()
        q1_2 = input("Player 2's Answer: ").lower()
        if q1_1 == answer_1:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q1_2 == answer_1:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")
            
        time.sleep(2)

        print("",question_2, sep = "\n")
        q2_1 = input("Player 1's Answer: ").lower()
        q2_2 = input("Player 2's Answer: ").lower()
        if q2_1 == answer_2:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q2_2 == answer_2:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")

        time.sleep(2)

        print("",question_3, sep = "\n")
        q3_1 = input("Player 1's Answer: ").lower()
        q3_2 = input("Player 2's Answer: ").lower()
        if q3_1 == answer_3:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q3_2 == answer_3:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")

        print("\nPlayer 1 scored",p1,"out of",num_questions)
        print("Player 1 score: ","{:.0%}".format(p1/num_questions))

        print("\nPlayer 2 scored",p2,"out of",num_questions)
        print("Player 2: ","{:.0%}".format(p2/num_questions))

        if p1 == p2:
            print("\n You tied!")
        elif p1 > p2:
            print("\nPlayer 1 Wins!")
        elif p1 < p2:
            print("\nPlayer 2 Wins!")

    elif num_questions == 5:

        print("",question_1, sep = "\n")
        q1_1 = input("Player 1's Answer: ").lower()
        q1_2 = input("Player 2's Answer: ").lower()
        if q1_1 == answer_1:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q1_2 == answer_1:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")
            
        time.sleep(2)

        print("",question_2, sep = "\n")
        q2_1 = input("Player 1's Answer: ").lower()
        q2_2 = input("Player 2's Answer: ").lower()
        if q2_1 == answer_2:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q2_2 == answer_2:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")

        time.sleep(2)

        print("",question_3, sep = "\n")
        q3_1 = input("Player 1's Answer: ").lower()
        q3_2 = input("Player 2's Answer: ").lower()
        if q3_1 == answer_3:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q3_2 == answer_3:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")

        time.sleep(2)

        print("",question_4, sep = "\n")
        q4_1 = input("Player 1's Answer: ").lower()
        q4_2 = input("Player 2's Answer: ").lower()
        if q4_1 == answer_4:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q4_2 == answer_4:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")

        time.sleep(2)

        print("",question_5, sep = "\n")
        q5_1 = input("Player 1's Answer: ").lower()
        q5_2 = input("Player 2's Answer: ").lower()
        if q5_1 == answer_5:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q5_2 == answer_5:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")
            
        print("\nPlayer 1 scored",p1,"out of",num_questions)
        print("Player 1 score: ","{:.0%}".format(p1/num_questions))

        print("\nPlayer 2 scored",p2,"out of",num_questions)
        print("Player 2: ","{:.0%}".format(p2/num_questions))

        if p1 == p2:
            print("\n You tied!")
        elif p1 > p2:
            print("\nPlayer 1 Wins!")
        elif p1 < p2:
            print("\nPlayer 2 Wins!")

    elif num_questions == 7:

        print("",question_1, sep = "\n")
        q1_1 = input("Player 1's Answer: ").lower()
        q1_2 = input("Player 2's Answer: ").lower()
        if q1_1 == answer_1:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q1_2 == answer_1:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")
            
        time.sleep(2)

        print("",question_2, sep = "\n")
        q2_1 = input("Player 1's Answer: ").lower()
        q2_2 = input("Player 2's Answer: ").lower()
        if q2_1 == answer_2:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q2_2 == answer_2:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")

        time.sleep(2)

        print("",question_3, sep = "\n")
        q3_1 = input("Player 1's Answer: ").lower()
        q3_2 = input("Player 2's Answer: ").lower()
        if q3_1 == answer_3:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q3_2 == answer_3:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")

        time.sleep(2)

        print("",question_4, sep = "\n")
        q4_1 = input("Player 1's Answer: ").lower()
        q4_2 = input("Player 2's Answer: ").lower()
        if q4_1 == answer_4:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q4_2 == answer_4:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")

        time.sleep(2)

        print("",question_5, sep = "\n")
        q5_1 = input("Player 1's Answer: ").lower()
        q5_2 = input("Player 2's Answer: ").lower()
        if q5_1 == answer_5:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q5_2 == answer_5:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")

        time.sleep(2)

        print("",question_6, sep = "\n")
        q6_1 = input("Player 1's Answer: ").lower()
        q6_2 = input("Player 2's Answer: ").lower()
        if q6_1 == answer_6:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q6_2 == answer_6:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")

        time.sleep(2)

        print("",question_7, sep = "\n")
        q7_1 = input("Player 1's Answer: ").lower()
        q7_2 = input("Player 2's Answer: ").lower()
        if q7_1 == answer_7:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q7_2 == answer_7:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")

         
        print("\nPlayer 1 scored",p1,"out of",num_questions)
        print("Player 1 score: ","{:.0%}".format(p1/num_questions))

        print("\nPlayer 2 scored",p2,"out of",num_questions)
        print("Player 2 score: ","{:.0%}".format(p2/num_questions))

        if p1 == p2:
            print("\n You tied!")
        elif p1 > p2:
            print("\nPlayer 1 Wins!")
        elif p1 < p2:
            print("\nPlayer 2 Wins!")

#3 PLAYER GAME CODE - FOR 3, 5 AND 7 QUESTIONS
elif players == 3:
    p1 = 0
    p2 = 0
    p3 = 0

    if num_questions == 3:

        print("",question_1, sep = "\n")
        q1_1 = input("Player 1's Answer: ").lower()
        q1_2 = input("Player 2's Answer: ").lower()
        q1_3 = input("Player 3's Answer: ").lower()
        if q1_1 == answer_1:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q1_2 == answer_1:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")

        if q1_3 == answer_1:
            p3 += 1
            print("Player 3 Correct!")
        else:
            print("Player 3 Incorrect.")
            
        time.sleep(2)

        print("",question_2, sep = "\n")
        q2_1 = input("Player 1's Answer: ").lower()
        q2_2 = input("Player 2's Answer: ").lower()
        q2_3 = input("Player 3's Answer: ").lower()
        if q2_1 == answer_2:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q2_2 == answer_2:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")

        if q2_3 == answer_2:
            p3 += 1
            print("Player 3 Correct!")
        else:
            print("Player 3 Incorrect.")

        time.sleep(2)

        print("",question_3, sep = "\n")
        q3_1 = input("Player 1's Answer: ").lower()
        q3_2 = input("Player 2's Answer: ").lower()
        q3_3 = input("Player 3's Answer: ").lower()
        if q3_1 == answer_3:
            p1 += 1
            print("Player 1 Correct!")
        else:
            print("Player 1 Incorrect.")

        if q3_2 == answer_3:
            p2 += 1
            print("Player 2 Correct!")
        else:
            print("Player 2 Incorrect.")

        if q3_3 == answer_3:
            p3 += 1
            print("Player 3 Correct!")
        else:
            print("Player 3 Incorrect.")

        print("\nPlayer 1 scored",p1,"out of",num_questions)
        print("Player 1 score: ","{:.0%}".format(p1/num_questions))

        print("\nPlayer 2 scored",p2,"out of",num_questions)
        print("Player 2 score: ","{:.0%}".format(p2/num_questions))

        print("\nPlayer 3 scored",p3,"out of",num_questions)
        print("Player 2 score: ","{:.0%}".format(p3/num_questions))

time.sleep(1)
print("Thank you for playing. If you would like new questions, you can change the questions by rewritting the questions under the questions code tab.")
