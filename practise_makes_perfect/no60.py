def f1(b):
    if b > a:
        return b
    else:
        return a*2
def f2(b,a):
    if a+b > 10:
        return(f1(a))
    elif b-a < 0:
        return b
    if a < 0:
        return -a
    return a
a = -3
print(f2(a,f1(f1(a))))
a = -1
print(f2(a,f1(f1(a))))
a = 1
print(f2(a,f1(f1(a))))
a = 5
print(f2(a,f1(f1(a))))
a = 7
print(f2(a,f1(f1(a))))