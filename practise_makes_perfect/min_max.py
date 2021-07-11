while True:
    counter = int(input())
    if 1 <= counter <= 1000:
        break
    else:
        continue
i = 1
arr = [] 
while i <= counter:
    input_num = int(input())
    if -2000000000 <= input_num <= 2000000000 :
        arr.append(input_num)
    else:
        continue
    i += 1
m = min(arr)
M = max(arr)
print(m)
print(M)