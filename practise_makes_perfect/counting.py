N , K = map(int,input().split())
i,j = 1,0
arr = [*range(1,N+1,1)]
newarr = []
while True:
    if len(arr) == len(newarr):
        break
    if i != 0:
        if i % K == 0 and arr[j] != 0:
            if arr[j] != 0:
                newarr.append(arr[j])
            arr[j] = 0
            i = 0
        elif arr[j] == 0:
            i = i - 1
    j = j+1
    if len(arr) == j:
        j = 0
    i = i+1
for i in range(len(newarr)):
    print(newarr[i])
    