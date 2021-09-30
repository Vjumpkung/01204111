import numpy as np
n = int(input("Input the maze's size (only 1 to 9): "))
t = int(input("Input the type of maze (only 1 to 2): "))

def printmat(n):
    for i in range(len(n)):
        for j in range(len(n[0])):
            print(n[i][j] , end=" ")
        print()

full_ls = []
koo = [2*i+2 for i in range(n//2)]
k = n - n//2
kee = [2*p+1 for p in range(k)]
if t == 2:
    for ooo,u in enumerate(reversed(koo+kee)):
        size = 2*(ooo)+1
        full_ls.append(np.full((size,size),u))
elif t == 1:
    for ooo,u in enumerate(reversed(kee+koo)):
        size = 2*(ooo)+1
        full_ls.append(np.full((size,size),u))
full_ls = full_ls[::-1]
for i,j in enumerate(full_ls):
    #print(i,j)
    full_ls[0][i:len(full_ls[0])-i,i:len(full_ls[0])-i] = full_ls[i]
printmat(full_ls[0])