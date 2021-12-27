fn = input("File name: ")
with open(fn) as df:
    data = df.read()
y = data.split("\n")
if y.index("List") != 0:
    y.insert(y.index("List")," ")
    price = y[y.index("Price")+1:y.index("List")-1]
    lst = y[y.index("List")+1:len(y)]
else:
    y.insert(y.index("Price")," ")
    price = y[y.index("List")+1:y.index("Price")-1]
    lst = y[y.index("Price")+1:len(y)]
price = [price[i].split() for i in range(len(price))]
price = dict(zip(*list(zip(*price))))
for i in price:
    price[i] = int(price[i])
lst = [lst[i].split() for i in range(len(lst))]
lst = dict(zip(*list(zip(*lst))))
#print(lst)
for i in lst:
    lst[i] = int(lst[i])
total = 0
for i in data.split("\n"):
    print(i)
for i in lst:
    try:
     total += lst[i]*price[i]
    except:
     continue
print(f"Total price: {total}")