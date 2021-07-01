wife_count = int(input("โอชามีเมียกี่คน : ")) 
totalprice = 0
price = []
i = 1
while i <= wife_count:
  askprice = int(input("ค่าอาหารของเมียคนที่ " + str(i) +" : "))
  price.append(askprice)
  i = i+1
print(sum(price))