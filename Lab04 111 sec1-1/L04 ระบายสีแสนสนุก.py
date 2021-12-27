N = int(input("N : "))
r = [int(x) for x in input().split()]
i = 0
while True:
    try:
        if r[i] == 0:
            if r[i+1] == 1:
                r[i] = 2
            elif r[i+1] == 2:
                r[i] = 1
            else:
                if r[i-1] == 1:
                    r[i] = 2
                else:
                    r[i] = 1
        i += 1
    except IndexError:
        if r[-1] == 0:
            if r[-2] == 1:
                r[-1] = 2
            else:
                r[-1] = 1
        break
i = 0
while True:
    try:
        if r[i] == r[i+1]:
            print("no")
            break
        i = i + 1
    except IndexError:
        print("yes")
        break