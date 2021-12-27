printmat = lambda n : [print(' '.join(map(str,i))) for i in n][0]
n = int(input("Input the maze's size (only 1 to 9): "))
t = int(input("Input the type of maze (only 1 to 2): "))
full_ls = []
koo = [2*i+2 for i in range(n//2)]
kee = [2*p+1 for p in range(n - n//2)]
if t == 1 :
    po = kee+koo
else:
    po = koo+kee
#po = list(range(n,0,-1))
#print(po)
for ooo in po:
    full_ls.append([[ooo for i in range(2*(n-1)+1)] for j in range(2*(n-1)+1)])
for ind,val in enumerate(full_ls):
    for i in range(len(full_ls[0][ind:-ind])):
        for j in range(len(full_ls[0][ind:-ind])):
            full_ls[0][i+ind][j+ind] = po[ind]
printmat(full_ls[0])