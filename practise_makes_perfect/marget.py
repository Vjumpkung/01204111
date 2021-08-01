from itertools import combinations
n,m,s,k = int(input()),[],1,0
for i in range(n):
    m.append([int(item) for item in input().split()])
deltaa = []
row = 0
for t in range(n):
    cc = list(combinations(m,t+1))
    for ii in range(len(cc)):
        for jj in range(len(cc[0])):
            s = cc[ii][jj][0]*s
            k = cc[ii][jj][1]+k
        deltaa.append(abs(s-k))
        s,k = 1,0
print(str(min(deltaa)))