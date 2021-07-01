# This program says hello and asks for my name.

print("Hello, world")
myName = input("What us your name? ")
print("It\'s good to meet you, " + myName)
print("The length of your name is: ")
print(len(myName))
myAge = input("What is your age? ")
print("You\'ll be " + str(int(myAge) + 1) + " in a year." )