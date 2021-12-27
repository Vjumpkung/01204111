import json
pylist=json.load(open(input("Filename : ")))

class account:
    def __init__(self, name, account_number, money, history):
        self.name = name
        self.account_number = account_number
        self.money = money
        self.history = history

    def show_data(self):
        print(f"Name : {self.name}")
        print(f"Account number : {self.account_number}")
        print(f"Money : {self.money}")
        print(f"History : {self.history}")

    def deposit(self):
        a = int(input("Amount : "))
        self.money += a
        print(f"Current money : {self.money}")
        if self.history == "": self.history = f"Deposit : {a}"
        else : self.history+=f"\nDeposit : {a}"

    def withdraw(self):
        b=int(input("amount : "))
        self.money-=b
        print(f"Current money : {self.money}")
        if self.history == "": 
            self.history = f"Withdraw : {b}"
        else : 
            self.history+=f"\nWithdraw : {b}"
    
    def show_history(self):
        print(self.history)
classes=[]
for item in pylist:
    a=account(item["name"], item["account number"], item["money"], item["history"])
    classes.append(a)

def main():
    accn=input("Account number : ")
    while True:
        for acc in classes:
            if acc.account_number == accn:
                while True:
                    m=int(input("Menu : "))
                    if m == 0: return
                    elif m == 1:
                        acc.show_data()
                    elif m == 2:
                        acc.deposit()
                    elif m == 3:
                        acc.withdraw()
                    elif m == 4:
                        acc.show_history()
                    elif m == 5:
                        accn=input("Account number : ")
                        break

main()