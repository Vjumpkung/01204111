circle = int(input())
i = 1
j = 1
while i <= circle:
    print(" "*((1+(circle//2))-j),end="")
    print("O"*(i),end="")
    print("\r")
    j += 1
    i = i + 2