a,b,c,d = map(int,input().split())
one,two,three,four = 0,0,0,0
if a <= b <= c <= d:
    one = a
    two = b
    three = c
    four = d
elif a <= b <= d <= c:
    one = a
    two = b
    three = d
    four = c
elif a <= d <= b <= c:
    one = a
    two = d
    three = b
    four = c
elif a <= d <= c <= b:
    one = a
    two = d
    three = c
    four = b
elif a <= c <= d <= b:
    one = a
    two = c
    three = d
    four = b
elif a <= c <= b <= d:
    one = a
    two = c
    three = b
    four = d
elif b <= a <= c <= d:
    one = b
    two = a
    three = c
    four = d
elif b <= a <= d <= c:
    one = b
    two = a
    three = d
    four = c
elif b <= c <= a <= d:
    one = b
    two = c
    three = a
    four = d
elif b <= c <= d <= a:
    one = b
    two = c 
    three = d
    four = a
elif b <= d <= c <= a:
    one = b
    two = d
    three = c
    four = a
elif b <= d <= a <= c:
    one = b
    two = d
    three = a
    four = c
elif c <= a <= b <= d:
    one = c
    two = a
    three = b
    four = d
elif c <= a <= d <= b:
    one = c
    two = a
    three = d
    four = b
elif c <= b <= a <= d:
    one = c
    two = b
    three = a
    four = d
elif c <= b <= d <= a:
    one = c
    two = b
    three = d
    four = a
elif c <= d <= a <= b:
    one = c
    two = d
    three = a
    four = b
elif c <= d <=b <=a:
    one = c
    two = d
    three = b
    four = a
elif d <= a <= b <= c:
    one = d
    two = a
    three = b
    four = c
elif d <= a <= c <= b:
    one = d
    two = a
    three = c
    four = b
elif d <= b <= a <= c:
    one = d
    two = b 
    three = a
    four = c
elif d <= b <= c <= a:
    one = d
    two = b
    three = c
    four = a
elif d <= c <= a <= b:
    one = d
    two = c
    three = a
    four = b
elif d <= c <= b <= a:
    one = d
    two = c
    three = b
    four = a
print(f'{one} {two} {three} {four}')