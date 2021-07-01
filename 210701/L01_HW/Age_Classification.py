EnterYourAge = int(input("Enter your age : "))
if 0 <= EnterYourAge <= 12 :
    print("You are Child.")
elif 13 <= EnterYourAge <= 18 :
    print("You are Adolescence.")
elif 19 <= EnterYourAge <= 59 :
    print("You are Adult.")
else:
    print("You are Senior Adult.")
