import random
import time

def sigma_i_1(n):
    return int(n*(n+1)/2)

def sigma_i_2(n):
    c = 0
    for i in range(1,n+1):
        c += i
    return c

print("sigma attack")
k = 1000000000
#print(arr)
# Function Call
t1 = time.time()
x = sigma_i_1(k)
print(x)
t2 = time.time()
t3 = time.time()
y = sigma_i_2(k)
print(y)
t4 = time.time()
print(t2-t1)
print(t4-t3)
#print(arr)
