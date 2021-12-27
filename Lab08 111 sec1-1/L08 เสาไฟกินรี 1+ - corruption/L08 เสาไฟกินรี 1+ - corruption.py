fn = input("Filename : ")
with open(fn) as df:
    data = df.readlines()[1:]
    data = [i.strip().split("\n") for i in data]
    data = [data[i][0].split(",") for i in range(len(data))]
    data = list(zip(*data))
tuujarit = []
for i in range(len(data[0])):
    if (int(data[1][i]) <= 1 and int(data[2][i]) <= 1000):
        continue
    elif (1 < int(data[1][i]) <= 4 and int(data[2][i]) <= 5000):
        continue
    elif (4 < int(data[1][i]) <= 8 and int(data[2][i]) <= 30000):
        continue
    elif (int(data[1][i]) > 8 and int(data[2][i]) <= 75000):
        continue
    tuujarit.append(int(data[0][i]))
if len(tuujarit) == 0:
    print("No")
else:
    tuujarit.sort()
    print("Yes")
    for i in tuujarit:
        print(i)