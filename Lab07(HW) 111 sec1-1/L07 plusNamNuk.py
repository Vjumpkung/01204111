#plusNamNuk
N = int(input("N : "))
st_rage = dict([input().split() for i in range(N)])
#st_rage = {'aaa': '5', 'bbb': '4', 'ddd': '3', 'ccc': '2', 'eee': '1'}
for i in st_rage:
    try:
        st_rage[i] = int(st_rage[i])
    except ValueError:
        continue
total = input().replace(" ","").split("+")
ans = 0
for i in total:
    ans += st_rage[i]
print(ans)