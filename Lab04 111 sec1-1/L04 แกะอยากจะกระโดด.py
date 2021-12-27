x,y = map(int,input('Grass : ').split())
j = 0
ar = [int(x) for x in input().split()]
for i in range(len(ar)):
    if ar[i] > y:
        j = j + 1
print(j)