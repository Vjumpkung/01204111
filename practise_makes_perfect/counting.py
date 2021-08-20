N , K = map(int,input().split())
#N = 8
#K = 10000
i = 1
j = 0
current_num = 0
arr = list(range(1,N+1))
newarr = [0 for i in range(N)]
isReducerr = False
def Reducerr (x):
    if K // (len(arr) + 1) == 0:
        return x
    else:
        x = (K//(len(arr)+1))*(len(arr)+1)
        return x
for _ in iter(int,1):
    if len(arr) == 1:
        print(arr[0])
        break
    current_num = arr[j]
    if isReducerr == False and i == 1:
        #i = Reducerr(i)
        isReducerr = True
    if i != 0:
        if i == K:
            if arr[j] != 0:
                #print(arr[j])
                #newarr.append(arr[j])
                arr.pop(j)
                j = j - 1
            i = 0
            isReducerr = False
    j = j+1
    #reset index pointer
    i = i+1
    if len(arr) == j:
        j = 0
#[print(newarr[i]) for i in range(len(newarr))]