def What(str):
    if str.islower():
        return "Album"
    else:
        return "Photobook"
def SStatus():
    if What(product) == "Album" : return "Album"
    else : return "Photobook"
def RReal(str):
    if ord(str[0]) + 1 == ord(str[-1]):
        return True
    else:
        return False
product = input()
print(What(product))
print(RReal(product))