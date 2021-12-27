#sibling
family = {}
tries = int(input())
for i in range((tries)):
    inp = input().split()
    if not inp[0]+","+inp[2] in list(family.keys()):
        if inp[2] not in ["girfriend","boyfriend","wife"]:
            family.setdefault(inp[0]+","+inp[2],[inp[-1]])
    else:
        family[inp[0]+","+inp[2]].append(inp[-1])
question = input().split()
question = [question[1],question[3]]
if (question in list(family.values())) or (question[::-1] in list(family.values())):
    print("Yes")
else:
    print("No")