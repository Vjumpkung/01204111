import numpy as np
def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^6}', end = ' ')
        print("\r")
def power_matrix(A,c):
    return (np.linalg.matrix_power(A,c).tolist())
A = [[1,2,3],[4,5,6],[7,8,9]]
c = 2
print_matrix(power_matrix(A,c))