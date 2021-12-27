#Ching Chok
l = input("Enter lucky number : ")
c = input("Enter amount of candidates : ")
max_num = 0
cx = 0
cy = 0
d = []
f = []
g = []
for i in range(int(c)):
    d.append(input(f"Enter ID card number {i+1}: "))
for j in range(len(d)):
    max_num = d[j].count(l)
    f.append(max_num)
for k in range(len(f)):
    try:
        if int(f[k]) == int(f[k+1]) == int(max(f)):
            if int(d[k]) > int(d[k+1]):
                g.append(int(d[k]))
            else:
                g.append(int(d[k+1]))
    except IndexError:
        break
if g == [] :
    print("Winner: " + str(d[f.index(max(f))]))
else:
    print("Winner: " + str(max(g)))