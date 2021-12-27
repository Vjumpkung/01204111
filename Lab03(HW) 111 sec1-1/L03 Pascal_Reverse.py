import math
def ncr(n, r):
    k = n-r
    output = (math.factorial(n))/((math.factorial(k))*(math.factorial(r)))
    return(int(output))
number = int(input())
number = number - 1
j = number 
i = number
r = 0
while number != 0:
    if i < r:
        i = i - 1
        r = 0
        print("\r")
    #print(f"{i} C {r}")
    #print("run NCR")
    print(f"{ncr(i,r)}",end=" ")

    if i == 1:
        print("1")
        break
    else:
        j = j - 1
        r = r + 1
print("1")