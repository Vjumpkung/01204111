import json
inp = input("Filename : ")
data = json.load(open(inp))
cas = int(input("Case : "))
chara = input("Character : ")
def case_one(c):
    dic = data
    c=c.split(',')
    for i in dic.values():
        if str(i["id"]) in c:
            print(f'{i["id"]}\t---\t{i["name"]}\t---\t{i["title"]}')
def case_two(chara):
    wait = []
    for i in chara.split(","):
        for j in data:
            if data[j]["name"][0] == i:
                wait.append(j)
    wait = sorted(wait,key=lambda x : int(x))
    for j in wait:
        print(f"{data[j]['id']}\t---\t{data[j]['name']}\t---\t{data[j]['title']}")
def case_three(chara):
    wait = []
    for i in chara.split(","):
        for j in data:
            if data[j]["title"].strip("the").strip("The").strip()[0] == i:
                wait.append(j)
    wait = sorted(wait,key=lambda x : int(x))
    for j in wait:
        print(f"{data[j]['id']}\t---\t{data[j]['name']}\t---\t{data[j]['title']}")
if cas == 0: case_one(chara)
elif cas == 1: case_two(chara)
elif cas == 2: case_three(chara)