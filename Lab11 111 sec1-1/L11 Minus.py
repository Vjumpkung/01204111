minus = lambda a,b : [i for i in a if i not in b]
A = list(map(int,input("Input set A: ").split()))
B = list(map(int,input("Input set B: ").split()))
X = minus(A,B)
if X == []:
    print("A minus B: empty set")
else:
    print(f"A minus B: {X}")