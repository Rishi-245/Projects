## Factorial Code


factorial = eval(input("Enter your number for factorial: "))
factor = 1

while factorial != 0:
    factor = factorial * factor
    factorial -= 1

print(factor)
