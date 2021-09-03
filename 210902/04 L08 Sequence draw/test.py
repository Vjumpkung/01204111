fn = input('File name: ')
d,decoy={},[]
with open(fn) as df:
    x = df.readlines()
    s=[i.strip('\n') for i in x]
    n=int(s[0])
    for i in s:
        if i == s[0]:continue
        if i in '0123456789':
            d[int(n)]=decoy
            n=i
            decoy=[]
            continue
        decoy.append(i)
d=dict(sorted(d.items()))
for i,v in d.items():
    for j in v:
        print(j)