import numpy as np
class Matrix:
    def __init__(self,matrix):
        self.mat = matrix
    def det(self):
        a = self.mat
        return (a[0][0] * (a[1][1] * a[2][2] - a[2][1] * a[1][2]) -a[1][0] * (a[0][1] * a[2][2] - a[2][1] * a[0][2]) +a[2][0] * (a[0][1] * a[1][2] - a[1][1] * a[0][2]))
    def plus(self,its):
        A = np.array(self.mat)
        B = np.array(its.mat)
        self.newmat = A + B
        return Matrix(self.newmat)
    def minus(self,its):
        A = np.array(self.mat)
        B = np.array(its.mat)
        self.newmat = A - B
        return Matrix(self.newmat)
    def multiply(self,its):
        A = np.array(self.mat)
        B = np.array(its.mat)
        self.newmat = np.matmul(A,B)
        return Matrix(self.newmat)
    def show(self):
        self.data = (self.mat).tolist()
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                print(f'{self.data[i][j]:^6}', end = ' ') 
            print("\r")
# do not submit this code!!!
def input_matrix():
    data = []
    for i in range(3):
        data.append([int(j) for j in input(f"Row {i+1} : ").split(' ')])
    return data

print("input row of matrix A")
A = Matrix(input_matrix())
print("input row of matrix B")
B = Matrix(input_matrix())

print(f'Det of Matrix(A) = {A.det()}')
print(f'Det of Matrix(B) = {B.det()}')

print("Matrix(A+B) is:")
res = A.plus(B)
res.show()

print("Matrix(A-B) is:")
res = A.minus(B)
res.show()

print("Matrix(A*B) is:")
res = A.multiply(B)
res.show()