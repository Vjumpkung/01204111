def addNum(x):
    A.append(x)
def showPrint(x):
    print(A[x])
def rem_ove(x):
    A.pop(x)
A = list(map(int,input().split()))
while True:
    menu,x = input().split()
    x = int(x)
    if (menu == "E" and x == 0):
        break
    elif (menu == "A"):
        addNum(x)
    elif (menu == "S"):
        showPrint(x)
    elif (menu == "R"):
        rem_ove(x)
for i in range(len(A)):
    print(A[i],end=" ")