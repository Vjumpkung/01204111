A = [[1,2],[3,4],[5,6]]
c = 2
def mul_const(A,c):
    for i in range(len(A)):
      for j in range(len(A[0])):
        A[i][j] = c*A[i][j]
    return A
mul_const(A,c)

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^6}', end = ' ')
        print("\r")

print_matrix(A)