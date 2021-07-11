matrix1 = []
matrix2 = []
row = []
col = []
n_row,n_col = map(int,input().split())
i = 1
k = 1
while k <= 2:
    # print(f"k = {k}")
    while i <= n_row:
        input_num = list(map(int, input().split()))
        row.append(input_num)
        col = []
        i = i + 1
    if k == 1:
        matrix1 = row
        i = 1
        k = k + 1
        row = []
    else:
        matrix2 = row
        break
        
for i in range(n_row):
    for j in range(n_col):
        #print(f"matrix 1 row,col : {i},{j} is {matrix1[i][j]}")
        #print(f"matrix 2 row,col : {i},{j} is {matrix2[i][j]}")
        matrix1[i][j] = matrix1[i][j] + matrix2[i][j]
#print(matrix1)
for i in range(n_row):
    for j in range(n_col):
        print(f"{matrix1[i][j]} ",end="")
    print("\r")