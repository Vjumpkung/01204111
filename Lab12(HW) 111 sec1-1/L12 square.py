R = int(input("R: "))
C = int(input("C: "))
def find_square(N,M):
    return ((M*(N-M)*(M+1))//2)+((M)*(M+1)*(2*M+1)//6)
print(find_square(R,C))