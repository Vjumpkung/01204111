import numpy as np
def transpose_matrix(A):
    return (np.transpose(A)).tolist()
def plus_matrix(A,B):
    return (np.add(A,B)).tolist()
def minus_matrix(A,B):
    return (np.subtract(A,B)).tolist()
def mul_matrix(A,B):
    return (np.matmul(A,B)).tolist()
def power_matrix(A,c):
    return (np.linalg.matrix_power(A,c)).tolist()
def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^6}', end = ' ')
        print("\r")
A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
D = [[100,50],[20,70]]
c = 2
print_matrix(mul_matrix(plus_matrix((A),transpose_matrix(B)),minus_matrix(power_matrix(C,2),D)))