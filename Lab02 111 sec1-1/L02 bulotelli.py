injured = str(input("Is Bulotelli injured?(y/n) "))
if injured == "n":
    late = str(input("Is Bulotelli late for the training?(y/n) "))
    if late == "n":
        print("Starter")
    else:
        selected = str(input("Did Bulotelli perform well in training?(y/n) "))
        if selected == "y":
            print("Substitute")
        else:
            print("Not selected")
else:
    print("Not available")