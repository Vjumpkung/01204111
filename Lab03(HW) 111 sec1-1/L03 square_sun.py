def draw(n):
    head(n)
    body(n)
    leg(n)
def head(n):
    cham_nuan_chant = n - 1
    i = 1
    j = n + 2*cham_nuan_chant
    while i <= cham_nuan_chant:
        print(" "*(i-1) + "*" + " "*(j-2) +"*")
        i = i + 1
        j = j - 2

def body(n):
    print(" "*(n-1)+"*"*n)
    i = 1
    cham_nuan_chant = n - 2
    while i <= cham_nuan_chant:
        print(" "*(n-1)+"*"+" "*(n-2)+"*")
        i = i+1
    print(" "*(n-1)+"*"*n)

def leg(n):
    cham_nuan_chant = n - 1
    i = 1
    j = n//2
    if n ==2:
        print("*  *")
    elif n >= 5 and n < 7:
        while i <= cham_nuan_chant:
            print(" "*(j+1) + "*" + " "*(n) +"*")
            n = n+2
            j = j-1
            i = i+1
    elif n >= 7:
        while i <= cham_nuan_chant:
            print(" "*(j+2) + "*" + " "*(n) +"*")
            n = n+2
            j = j-1
            i = i+1   
    else:
        while i <= cham_nuan_chant:
            print(" "*(j) + "*" + " "*(n) +"*")
            n = n+2
            j = j-1
            i = i+1
n = int(input())
draw(n)
