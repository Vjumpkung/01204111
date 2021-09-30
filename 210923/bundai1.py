def all_possible_stairs(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return all_possible_stairs(n-1)+all_possible_stairs(n-2)+all_possible_stairs(n-3)
nen = int(input("n : "))
print(all_possible_stairs(nen))