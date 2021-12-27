fn = input("File name: ")
with open(fn) as df:
    data = df.readlines()
    data = [i.strip().split("\n") for i in data]
dick = {}
for i in range(len(data)):
    dick[data[i][0].split()[0]] = sorted(list(map(int,data[i][0].split()[1:])))
for i in dick:
    dick[i] = sum(dick[i][1:-1])
print(max(dick.values()))
[print(i) for i in dick if dick[i] == max(dick.values())][0]