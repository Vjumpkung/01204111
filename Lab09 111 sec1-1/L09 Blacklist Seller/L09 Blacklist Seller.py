import json
inp = input("Filename : ")
data = input("Data : ")
df = json.load(open(inp))
lst = []
for i in df[0]:
    wait = []
    for j in df:
        wait.append(j[i])
    lst.append(wait)
if len([1 for i in list(zip(*lst)) if data in i]) == 1:
    print("Found in blacklist")
    for i in df:
        if data in i.values():
            for j in i:
                print(j,":",i[j])
else:
    print("Not found in blacklist")