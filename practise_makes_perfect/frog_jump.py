import math
a , b = map(int,input().split())
if a < b:
    print(math.ceil(b/a))
else:
    print(2)