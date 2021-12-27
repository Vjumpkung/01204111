def union(a,b):
    Y = []
    X = a+b
    P = [Y.append(i) for i in X if i not in Y]
    return sorted(Y)
A = list(map(int,input("Input set A: ").split()))
B = list(map(int,input("Input set B: ").split()))
X = union(A,B)
if X == []:
    print("A union B: empty set")
else:
    print(f"A union B: {X}")