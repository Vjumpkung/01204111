import json
inp = input("Enter json filename : ")
df = json.load(open(inp))
products = df["products"]
products = dict([list(i.values()) for i in products])
custo = df["customers"]
custo = sorted(custo,key=lambda x : x["customer_name"])
def cal_product(sinkar,chamnuan):
    if sinkar in products:
        return int(products[sinkar])*chamnuan 
    return 0
def change(total_price, pay):
    bank_notes = (1000,500,100,50,20,10,5,2,1)
    thorn = pay - total_price
    #print(f"Customer's change: {thorn}")
    for i in range(len(bank_notes)):
        if thorn//bank_notes[i] > 0:
            print(f"{bank_notes[i]} : {thorn//bank_notes[i]}")
        else:
            pass
        thorn = thorn - (thorn//bank_notes[i])*bank_notes[i]
for j,i in enumerate(custo):
    print(i["customer_name"])
    total = 0
    example1 = list(custo[j]['order'].items())
    for k in example1:
        total += cal_product(k[0],k[1])
    if custo[j]["money"]-total == 0:
        print("no change")
    else:
        #print(f"must thorn {custo[j]['money']-total}")
        change(total,custo[j]["money"])
    print()