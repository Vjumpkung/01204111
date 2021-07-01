import numpy as np
collect_j = []
def sequence_1 (n):
    for i in range (0,n):
        collect_j.append(i+1)
sequence_1(1000)
def raise_myself(x):
    return(x**x)
collect_j = list(map(raise_myself,collect_j))
def last_ten_digit(x):
    x = str(x)
    return (x[len(x)-10:len(x)])
print(last_ten_digit(int(sum(collect_j))))

        
