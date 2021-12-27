from itertools import combinations
N = int(input('N : '))
lst = []
for i in range(N):
    dick = {}
    t,n = input().split()
    n = int(n)
    dick.setdefault(n,t)
    lst.append(dick)
XX = int(input('XX : '))
for i in range(N):
    for j in (combinations(lst,i+1)):
        sam = 0
        current = []
        for k in j:
            #print(k,end=" ")
            sam += list(k.keys())[0]
            current += k.values()
        if sam == XX:
            print(" ".join(current))
            break