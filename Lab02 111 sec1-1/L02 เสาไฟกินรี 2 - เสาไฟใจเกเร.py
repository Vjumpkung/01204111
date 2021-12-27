while True:
    input_pole = int(input("number of electric poles : "))
    if input_pole > 1:
        break
    else:
        continue
i = 1
pricelist = []
while i <= input_pole:
    get_price = int(input())
    pricelist.append(get_price)
    i = i+1
pricelist.sort()
if max(pricelist) > int(pricelist[-2])*3:
    print("YES")
    print(max(pricelist))
else:
    print("NO")
