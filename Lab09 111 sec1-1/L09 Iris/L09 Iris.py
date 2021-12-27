import json,statistics
data = json.load(open(input("Filename : ")))
typ = input("type : ")
edok = {}
for i in data:
    if i["species"] not in edok:
        edok.setdefault(i["species"],[i[typ]])
    else:
        edok[i["species"]].append(i[typ])
for i in edok:
    print(f"{i} = {statistics.mean(edok[i]):.2f}")