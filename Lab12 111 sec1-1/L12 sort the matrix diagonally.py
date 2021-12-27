M = int(input("M: "))
N = int(input("N: "))
lst = [list(map(int,input().split())) for i in range(M)]
lst = [i[::-1] for i in lst]
kkk = []
for ind,val in enumerate(lst):
    for j,x in enumerate(val):
        kkk.append((ind,j))
ind_pos = 0
kkk = sorted(kkk , key = lambda x : sum(x) , reverse=True)
mat = lst[::-1]
diag = []
for offset in range(len(mat[0])-1,-len(mat),-1):
    diag.append([row[i+offset] for i,row in enumerate(mat) if 0 <= i+offset < len(row)])
diag = list(map(sorted,diag))
pos = 0
for i in diag:
    for j in i:
        mat[kkk[pos][0]][kkk[pos][1]] = j
        pos += 1
print('sorted matrix is:')
for p in [i[::-1] for i in lst][::-1]:
    print(' '.join(map(str,p)))