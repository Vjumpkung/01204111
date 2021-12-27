import re
import numpy as np
with open(input("File name: ")) as m:
    txt = m.read()
d = re.findall(r"[^\+\*]+[^\+\*]",txt)
o = re.findall(r"[\+\*]",txt)
d = [i.strip().split("\n") for i in d]
all_mat = [[list(map(int,d[i][j].split())) for j in range(len(d[i]))] for i in range(len(d))]
res = (np.matmul(all_mat[0],all_mat[1])+all_mat[2]).tolist()
for i in range(len(res)):
    for j in range(len(res[0])):
        print(f"{res[i][j]:^5}",end=" ")
    print()