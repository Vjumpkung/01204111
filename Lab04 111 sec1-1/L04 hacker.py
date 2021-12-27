p = []
x = input()
for i in range(len(x)):
    p.append(x[i])
for i in range(len(x)):
    if int(input()) == int(p[i]):    
        if int(p[i]) == int(p[-1]):
            print("Succeed!!")
            break    
        continue
    else:
        print("Fail!!")
        break