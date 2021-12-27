a = input("Input name: ")
b = []
for k in range(len(a)):
    b.append(a[k])
for i in range(len(b)):
    for j in range(len(b)):
        b[i] = b[i].upper()
        print(f"{b[j]}",end="")
        b[i] = b[i].lower()
    print("\r")