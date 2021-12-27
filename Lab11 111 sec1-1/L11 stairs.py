def all_possible_stairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return all_possible_stairs(n-1)+all_possible_stairs(n-2)+all_possible_stairs(n-3)
nen = int(input("n : "))
print(all_possible_stairs(nen))