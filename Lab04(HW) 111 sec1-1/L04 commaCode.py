def commaCode(myList):
    ls = myList
    try:
        if not len(ls) == 0 and len(ls) != 1:
            for i in range(len(ls)-1):
                print(f"{ls[i]}, ",end="")
            print(f"and {ls[-1]}")
        else:
            print(f"{ls[-1]}")
    except IndexError:
        print("")
try: 
    ls = [str(x) for x in input("Input: ").split()]
except TypeError:
    print("")
commaCode(ls)
