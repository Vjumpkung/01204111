#Ultra_zigzag
import numpy as np
#print("Enter a sentence or pharse and then press ENTER")
#inputt = input().strip()
#n = int(input("Enter output type (only 1..5:) "))
#inputt = "Put a value v at the top of stack s"
inputt = "ABCDEFGHIJKLM"
n = 1
#inputt = [["ABCD"],["EFGH"],["IJKL"],["M***"]]
if n == 1:
    i = 1
    while True:
        if len(inputt) // i**2 != 0:
            i += 1
        else:
            inputt = inputt + "*"*(i**2 - len(inputt) % i**2)
            break
    matrix_dimension = i
    first_space = "   "
    print(first_space,end="")
    #row
    for ii in range(matrix_dimension):
        print(str(ii+1) + "  ",end="")
    #col
    print()
    kk = 0
    def printcolnum(jj):
        print(" "+str(jj+1),end="")
    printcolnum(0)
    for ijk in range(len(inputt)):
        print(" "+inputt[ijk]+" ",end="")
        if ijk+1 == matrix_dimension**2:
            break
        if (ijk+1)%matrix_dimension == 0:
            print("\r")
            printcolnum((ijk+1)//matrix_dimension)
elif n == 2:
    i = 1
    while True:
        if len(inputt) // i**2 != 0:
            i += 1
        else:
            inputt = inputt + "*"*(i**2 - len(inputt) % i**2)
            break
    matrix_dimension = i
    roww = []
    index_inputt = 0
    for x in range(matrix_dimension):
        coll = []
        for y in range(matrix_dimension):
            coll.append(inputt[index_inputt])
            index_inputt += 1
        roww.append(coll)
    #pp(np.rot90(roww,k=1,axes=(0,1)).tolist()[::-1])
    xxxx = np.rot90(roww,k=1,axes=(0,1)).tolist()[::-1]
    newText = ""
    for i3 in range(len(xxxx)):
        for j3 in range(len(xxxx[0])):
            newText = newText + xxxx[i3][j3]
    inputt = newText
    first_space = "   "
    print(first_space,end="")
    #row
    for ii in range(matrix_dimension):
        print(str(ii+1) + "  ",end="")
    #col
    print()
    kk = 0
    def printcolnum(jj):
        print(" "+str(jj+1),end="")
    printcolnum(0)
    for ijk in range(len(inputt)):
        print(" "+inputt[ijk]+" ",end="")
        if ijk+1 == matrix_dimension**2:
            break
        if (ijk+1)%matrix_dimension == 0:
            print("\r")
            printcolnum((ijk+1)//matrix_dimension)
elif n == 3:
    i = 1
    while True:
        if len(inputt) // i**2 != 0:
            i += 1
        else:
            inputt = inputt + "*"*(i**2 - len(inputt) % i**2)
            break
    matrix_dimension = i
    roww = []
    index_inputt = 0
    for x in range(matrix_dimension):
        coll = []
        for y in range(matrix_dimension):
            coll.append(inputt[index_inputt])
            index_inputt += 1
        roww.append(coll)
    #pp(np.rot90(roww,k=2,axes=(0,1)).tolist())
    xxxx = np.rot90(roww,k=2,axes=(0,1)).tolist()
    newText = ""
    for i3 in range(len(xxxx)):
        for j3 in range(len(xxxx[0])):
            newText = newText + xxxx[i3][j3]
    inputt = newText
    first_space = "   "
    print(first_space,end="")
    #row
    for ii in range(matrix_dimension):
        print(str(ii+1) + "  ",end="")
    #col
    print()
    kk = 0
    def printcolnum(jj):
        print(" "+str(jj+1),end="")
    printcolnum(0)
    for ijk in range(len(inputt)):
        print(" "+inputt[ijk]+" ",end="")
        if ijk+1 == matrix_dimension**2:
            break
        if (ijk+1)%matrix_dimension == 0:
            print("\r")
            printcolnum((ijk+1)//matrix_dimension)
elif n == 4:
    i = 1
    while True:
        if len(inputt) // i**2 != 0:
            i += 1
        else:
            inputt = inputt + "*"*(i**2 - len(inputt) % i**2)
            break
    matrix_dimension = i
    roww = []
    index_inputt = 0
    for x in range(matrix_dimension):
        coll = []
        for y in range(matrix_dimension):
            coll.append(inputt[index_inputt])
            index_inputt += 1
        roww.append(coll)
    #pp(np.rot90(roww[::-1],k=1,axes=(0,1)).tolist())
    xxxx = np.rot90(roww[::-1],k=1,axes=(0,1)).tolist()
    newText = ""
    for i3 in range(len(xxxx)):
        for j3 in range(len(xxxx[0])):
            newText = newText + xxxx[i3][j3]
    inputt = newText
    first_space = "   "
    print(first_space,end="")
    #row
    for ii in range(matrix_dimension):
        print(str(ii+1) + "  ",end="")
    #col
    print()
    kk = 0
    def printcolnum(jj):
        print(" "+str(jj+1),end="")
    printcolnum(0)
    for ijk in range(len(inputt)):
        print(" "+inputt[ijk]+" ",end="")
        if ijk+1 == matrix_dimension**2:
            break
        if (ijk+1)%matrix_dimension == 0:
            print("\r")
            printcolnum((ijk+1)//matrix_dimension)
elif n == 5:
    i = 1
    while True:
        if len(inputt) // i**2 != 0:
            i += 1
        else:
            inputt = inputt + "*"*(i**2 - len(inputt) % i**2)
            break
    matrix_dimension = i
    def sigma_i(n):
        x = n*(n+1)//2
        return x
    nummm = 0
    while True:
        first = sigma_i(nummm)
        last = sigma_i(nummm+1)
        temp_text = inputt[first:last]
        if len(temp_text)%2 != 0:
            inputt = inputt.replace(temp_text,temp_text[::-1])
        if inputt[last] == inputt[-1]:
            break
        nummm += 1
    print(inputt)

        
