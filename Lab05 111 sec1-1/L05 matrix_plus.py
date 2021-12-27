A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[22,13,23],
     [54,43,21],
     [23,78,71]]

def create_matrix(x,y):
    matrix=[] 
    row=[]
    for i in range(x):
        row=[]
        for j in range(y): 
            row.append(0)
        matrix.append(row)
    return (matrix)

def plus_matrix(A,B):
    C = create_matrix(len(A),len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j]
    return C

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^6}', end = ' ')
        print("\r")

C = plus_matrix(A,B)
print_matrix(C)