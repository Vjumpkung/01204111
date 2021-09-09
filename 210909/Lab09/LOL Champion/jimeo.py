import json

y=''
file = input('Filename : ')
case = int(input('Case : '))
c = input('Character : ')
with open (file,'r') as f:
    y=f.read()
dic=json.loads(y)
if case == 1:
    c=c.split(',')
    for i in dic.values():
        if str(i["name"][0]) in c:
            print(f'{i["id"]}\t---\t{i["name"]}\t---\t{i["title"]}')
elif case == 2:
    c=c.split(',')
    for i in dic.values():
        if str(i["title"].strip('the').strip('The').strip()[0]) in c:
            print(f'{i["id"]}\t---\t{i["name"]}\t---\t{i["title"]}')
else:
    c=c.split(',')
    for i in dic.values():
        if str(i["id"]) in c:
            print(f'{i["id"]}\t---\t{i["name"]}\t---\t{i["title"]}')