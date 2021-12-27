import re
#fn = "case3.txt"
fn = input("File name: ")
with open(fn) as df:
    txt = df.read()
draw = [i[1:len(i)-1] for i in re.findall(r"[^0-9]+[^0-9]",txt)]
num = re.findall(r"[0-9]",txt)
summary = sorted(list(zip(num,draw)),key=lambda x : x[0])
for d in summary:
    print(d[1])