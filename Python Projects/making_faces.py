#CS50's Introduction to Programming with Python
#Rishi Patel
#April 22, 2022
#Project: Making Faces

string = input("Enter your text: ")
string_1 = ""

for i in range(len(string)-1):
    if string[i] == ":" and string[i+1] == ")":
        string_1 += "🙂"
        break

    elif string[i] == ":" and string[i+1] == "(":
        string_1 += "🙁"
        break

    if string[i] == ":" and string[i+1] == "|":
        string_1 += "😐"
        break

    else:
        string_1 += string[i]

print(string_1)
