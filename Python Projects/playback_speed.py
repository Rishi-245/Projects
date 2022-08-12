#CS50's Introduction to Programming with Python
#Rishi Patel
#April 22, 2022
#Project: Playback Speed

string = input("Enter a sentence: ")
string_1 = ""

for i in range(len(string)):
    if string[i] == " ":
        string_1 += "..."
    else:
        string_1 += string[i]


print(string_1)
