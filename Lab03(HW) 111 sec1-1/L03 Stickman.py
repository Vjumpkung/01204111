def Head(n):
    m = n//2
    i = 1
    print(" "+"o"*n+" ")
    while i <= ((n//2)-1):
        print(" "+"o"+" "*(2*m-2)+"o")
        i = i+1
    print(" "+"o"*n+" ")
def Body(n):
    if n == 2:
        print("-||-")
    else:
        m = n//2
        i = 1
        while i <= m-1:
            print(" "*m + "||")
            i = i+1
        i = 1
        print("-"*m + "||" + "-"*m)
        while i <= m-1:
            print(" "*m + "||")
            i = i+1
def Leg(n):
    m = n//2
    i = 0
    while True:
        print(" "*(m-i) + "/" + " "*(2*i) + "\\" )
        if m-i-1 == 0:
            break
        else:
            i += 1
def StickMan(x):
    Head(x)
    Body(x)
    Leg(x)
def debugging():
    print("\n\n-----------------\n\n")
    StickMan(2)
    print("\n\n-----------------\n\n")
    StickMan(4)
    print("\n\n-----------------\n\n")
    StickMan(6)
    print("\n\n-----------------\n\n")
number = int(input())
StickMan(number)
#debugging()