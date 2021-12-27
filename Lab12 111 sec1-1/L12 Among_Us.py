import numpy as np
n = int(input('Input n: '))
m = int(input('Input m: '))
field = np.array([list(map(int,input().split())) for i in range(n)])
for i in list(range(np.min(field),np.max(field)+1)):
    finder = np.where(field == i)
    print(f"({finder[0][0]},{finder[1][0]})")
