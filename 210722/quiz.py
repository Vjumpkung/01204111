#optimized one
def optimized_code_01():
    def sum_price():
        cf_price,s,coffee = [0,40,45,50,55,60],0,1
        print("Menu\n0. Finish\n1. Latte = 40\n2. Espresso = 45\n3. Americano = 50\n4. Mocca = 55\n5. Cappuccino = 60")
        while not coffee == 0:
            coffee = int(input("coffee : "))
            if coffee == 0:
                break
            amount = int(input("amount : "))
            s = s + cf_price[coffee]*amount
        print(f"total price : {s}")   
        return s
    def change(total_price,pay):
        thorn = pay - total_price
        print(f"customer's change : {thorn}")
        bank_notes = [1000,500,100,50,20,10,5,1]
        for i in range(len(bank_notes)):
            if thorn//bank_notes[i] > 0:
                t = thorn//bank_notes[i]
                print(f"change {bank_notes[i]} : {int(t)}")
                thorn = thorn - t*bank_notes[i]
    change(sum_price(),int(input("customer pay : ")))
#submitted this one    
def unoptimized_code_01():
    x = 0
    y = 0
    def sum_price():
        cf_price = [0,40,45,50,55,60]
        s = 0
        print("Menu\n0. Finish\n1. Latte = 40\n2. Espresso = 45\n3. Americano = 50\n4. Mocca = 55\n5. Cappuccino = 60")
        while True:
            coffee = int(input("coffee : "))
            if coffee == 0:
                break
            elif coffee != 0:
                amount = int(input("amount : "))
                s = s + cf_price[coffee]*amount
        print(f"total price : {s}")   
        x = s
        return x
    def change(total_price,pay):
        thorn = pay - total_price
        print(f"customer's change : {thorn}")
        pun,ha_roi,roi,ha_sib,yee_sib,sib,ha,one = 0,0,0,0,0,0,0,0
        pun = thorn // 1000
        ha_roi = (thorn - pun * 1000)//500
        roi = (thorn - pun * 1000 - ha_roi * 500)//100
        ha_sib = (thorn - pun * 1000 - ha_roi * 500 - roi * 100)//50
        yee_sib = (thorn - pun * 1000 - ha_roi * 500 - roi * 100 - ha_sib * 50)//20
        sib = (thorn - pun * 1000 - ha_roi * 500 - roi * 100 - ha_sib * 50 - yee_sib * 20)//10
        ha = (thorn - pun * 1000 - ha_roi * 500 - roi * 100 - ha_sib * 50 - yee_sib * 20 - sib * 10)//5
        one = (thorn - pun * 1000 - ha_roi * 500 - roi * 100 - ha_sib * 50 - yee_sib * 20 - sib * 10 - ha * 5)//1
        if not pun == 0:
            print(f"change 1000 : {pun}")
        if not ha_roi == 0:
            print(f"change 500 : {ha_roi}")
        if not roi == 0:
            print(f"change 100 : {roi}")
        if not ha_sib == 0:
            print(f"change 50 : {ha_sib}")
        if not yee_sib == 0:
            print(f"change 20 : {yee_sib}")
        if not sib == 0:
            print(f"change 10 : {sib}")
        if not ha == 0:
            print(f"change 5 : {ha}")
        if not one == 0:
            print(f"change 1 : {one}")
    x = sum_price()
    y = int(input("customer pay : "))
    change(x,y)
optimized_code_01()