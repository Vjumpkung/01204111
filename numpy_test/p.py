import numpy as np
n = int(input())
def printmat(n):
    for i in range(len(n)):
        for j in range(len(n[0])):
            print(n[i][j] , end=" ")
        print()
full_ls = []
for ooo in range(1,n+1):
    full_ls.append(np.array([[ooo for i in range(2*(ooo-1)+1)] for j in range(2*(ooo-1)+1)]))
full_ls = full_ls[::-1]
for i,j in enumerate(full_ls):
    full_ls[0][i:len(full_ls[0])-i,i:len(full_ls[0])-i] = j
printmat(full_ls[0])