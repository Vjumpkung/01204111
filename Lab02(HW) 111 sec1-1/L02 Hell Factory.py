A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
while True:
    if (A == 0 and B == 0) or (A == 0 and C == 0) or (B == 0 and C == 0):
        break
    elif A >= B >= C:
        A = A - 1
        B = B - 1
        C = C + 1
    elif A >= C >= B:
        A = A - 1
        C = C - 1
        B = B + 1
    elif B >= A >= C:
        B = B - 1
        A = A - 1
        C = C + 1
    elif B >= C >= A:
        B = B - 1
        C = C - 1
        A = A + 1
    elif C >= A >= B:
        C = C - 1
        A = A - 1
        B = B + 1
    elif C >= B >= A:
        C = C - 1
        B = B - 1
        A = A + 1
if A != 0:
    print("A")
elif B != 0:
    print("B")
elif C != 0:
    print("C")