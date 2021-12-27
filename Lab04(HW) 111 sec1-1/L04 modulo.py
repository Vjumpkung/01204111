my_list = []
N = int(input("N: "))
M = int(input("M: "))
for i in range(N):
    
    my_input = int(input(f"Input number {i+1}: "))
    my_list.append(my_input)
my_list.sort()
def sameNum (x):
    for j in range(len(x)):
        try:
            if (x[j] == x[j+1]):
                x.pop(j+1)
        except IndexError:
            break
    return x
#print(my_list)
my_list = sameNum(my_list)
mod_ls = []
for i in range(len(my_list)):
    get_mod_ls = my_list[i] % M
    mod_ls.append(get_mod_ls)
mod_ls.sort()
mod_ls = sameNum(mod_ls)
#print(mod_ls)
print(len(set(mod_ls)))