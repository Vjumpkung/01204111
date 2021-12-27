how_many = int(input("How many food you have : "))
k = 0
total = 0
def plus(total,value):
    return total+value

def minus(total,value):
    return total-value

for i in range(how_many):
    my_input = input()
    x = my_input.split()
    if x[1] == "1":
        k = plus(int(x[0]),int(x[1]))
        
    else:
        k = minus(int(x[0]),int(x[1]))
    l = int(x[0])*int(x[1])
    total = total + l
print(total)