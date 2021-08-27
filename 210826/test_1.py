# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
coffee_data ={
    "Latte" : 40,
    "Espresso" : 45,
    "Americano" : 50,
    "Mocca" : 55,
    "Cappuccino" : 60
}


# %%
def print_menu():
    print('''Coffee Menu
0. Finish
1. Latte = 40
2. Espresso = 45
3. Americano = 50
4. Mocca = 55
5. Cappuccino = 60''')


# %%
def order_coffee():
    reciept = {}
    menu_ls = [0,"Latte","Espresso","Americano","Mocca","Cappuccino"]
    while True:
        coffee_type = int(input("Coffee type: "))
        if coffee_type == 0: break
        amount_of = int(input(f"Amount of {menu_ls[coffee_type]}: "))
        if not menu_ls[coffee_type] in reciept:
            reciept.setdefault(menu_ls[coffee_type],amount_of)
        else:
            reciept[menu_ls[coffee_type]] += amount_of
    total_price = sum([reciept[i]*coffee_data[i] for i in reciept])
    order_dict = reciept
    print(f"Total price: {total_price}")
    return order_dict,total_price


# %%
def change(total_price, pay):
    bank_notes = (1000,500,100,50,20,10,5,1)
    thorn = pay - total_price
    print(f"Customer's change: {thorn}")
    for i in range(len(bank_notes)):
        if thorn//bank_notes[i] > 0:
            print(f"Change {bank_notes[i]}: {thorn//bank_notes[i]}")
        else:
            pass
        thorn = thorn - (thorn//bank_notes[i])*bank_notes[i]


# %%
def print_receipt(orders_dict, customer_name, total_price):
    print("--------- receipt ---------")
    print("CPE35 COFFEE SHOP")
    print(f"Customer name: {customer_name}")
    x = [f"{i} {orders_dict[i]}" for i in orders_dict][0]
    print(f"{x}, {total_price} baht")
    print("Thank you")
    print("---------------------------")


# %%
def print_report(sales_dict):
    if not sales_dict == {}:
        print("---- Daily Sale Report ----")
        x = [print(f"{i} {sales_dict[i]} baht") for i in sales_dict][0]
        y = [sales_dict[i] for i in sales_dict]
        print(f"Total sale: {sum(y)} baht")
        print("---------------------------")
    else:
        print('''---- Daily Sale Report ----
Total sale: 0 baht
---------------------------''')


# %%
## main begins here
sales_dict = {}
while True:
    print_menu()
    customer_name = input("Customer name: ")
    if customer_name == "end day":
        break
    orders_dict, total_price = order_coffee()
    if customer_name not in sales_dict:
        sales_dict[customer_name] = total_price
    else:
        sales_dict[customer_name] += total_price

    pay = int(input("Customer pay: "))
    change(total_price,pay)
    print_receipt(orders_dict, customer_name, total_price)

print_report(sales_dict)


