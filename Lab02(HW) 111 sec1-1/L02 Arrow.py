number_arrow = int(input())
Arrow = input("Arrow : ")
Stick = input("Stick : ")
i = 1
while i <= number_arrow:
    print(" "*(number_arrow - (i-1)),end="")
    print(Arrow*(2*i-1),end="")
    print(" "*(i-1),end="")
    print("\r")
    i = i+1
j = 1
while j <= number_arrow:
    print(" "*number_arrow+Stick)
    j = j+1