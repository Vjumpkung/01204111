# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
class Shopee:
    def __init__(self,args):
        self.ID,self.type,self.price = args
        self.datapack = {"id" : int(self.ID) , "type" : self.type , "price" : int(self.price)}
    def __str__(self):
        return f"{self.datapack}"


# %%
hmy = int(input("How many products are there? : "))
lst = [Shopee(input().split()) for i in range(hmy)]
def main():
    input_id = (input("Id : "))
    while True:
        for i in lst:
            if i.ID == input_id:
                while True:
                    inp = int(input("Q : "))
                    if inp == 0: return False
                    elif inp == 1:
                        print(f"{i.type}")
                    elif inp == 2:
                        print(f"{i.price}")
                    elif inp == 3:
                        return True
        if i.datapack['id'] != input_id:
            print("This id doesn't exist.")
            return True
while True:
    if main() :
        continue
    else:
        break


# %%



