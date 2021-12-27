def prime_check(num):
        if num in [2,3,5,7,31]:
            return True
        elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num == 1:
            return False
        else:
            i = 8
            while True:
                if num % 1 == 0 and num % i == 0:
                    if num == i :
                        return True
                    else:
                        return False
                else:
                    i = i + 1
N = int(input("N: "))
while True:
    if prime_check(N) == True and prime_check(N+2) == True:
        print(f"({N}, {N+2})")
        break
    else:
        N = N + 1