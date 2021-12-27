N = int(input("N = "))
c = []
f = []
for i in range(N):
    c.append(int(input((f"cost of day {i+1} = "))))
i = 0
while True:
    try:
        f.append(c[i]+c[i+1]+c[i+2])
        i = i + 1
    except IndexError:
        break
print(f"Min cost of 3 days = {min(f)}")