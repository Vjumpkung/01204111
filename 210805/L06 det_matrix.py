import numpy as np
a1,a2,a3 = map(int,input("Row 1 : ").split())
a4,a5,a6 = map(int,input("Row 2 : ").split())
a7,a8,a9 = map(int,input("Row 3 : ").split())
A = np.array([[a1,a2,a3],[a4,a5,a6],[a7,a8,a9]])
def det_matrix(A):
    return np.linalg.det(A)
print(int(det_matrix(A)))
