circle = int(input())
i = 1
j = 1
while i <= circle:
    print(" "*((1+(circle//2))-j),end="")
    print("O"*(i),end="")
    print("\r")
    j = j + 1
    i = i + 2
k = 1
l = 1
while k <= circle - 1:
    print(" "*(k),end="")
    print("O"*(circle - 1 - l),end="")
    print("\r")
    k = k + 1
    l = l + 2