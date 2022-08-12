#CS50's Introduction to Programming with Python
#Rishi Patel
#April 22, 2022
#Project: Einstein

options = input("Which variable do you have? Mass or Energy? ").lower()
speed_light =  300000000

if options == "mass":
    mass = eval(input("Enter the mass: "))
    energy = mass * (speed_light * speed_light)
    print("E: ", energy)


elif options == "energy":
    energy = eval(input("Enter the energy: "))
    mass = energy / (speed_light * speed_light)
    print("m: ", mass)
    
