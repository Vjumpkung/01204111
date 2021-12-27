def create_matrix(x,y):
    matrix=[] 
    row=[]
    for i in range(x):
        row=[]
        for j in range(y): 
            row.append(0)
        matrix.append(row)
    return (matrix)

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^6}', end = ' ')
        print("\r")

def mul_matrix(A,B):
    #check matrix size
    C = create_matrix(len(A),len(B[0]))
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]  
B = [[22,13,23],
     [54,43,21],
     [23,78,71]]

print_matrix(mul_matrix(A,B))
mul_matrix(A,B)