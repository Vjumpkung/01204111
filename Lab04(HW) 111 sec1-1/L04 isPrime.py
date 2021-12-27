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

ls = []
while True:
    x = int(input())
    if x == 0:
        break
    else:
        ls.append(x)
        continue

count = 1
i = 0
while i < len(ls):
    if count <= 10:
        if prime_check(ls[i]) == True:
            print(str(ls[i]),end="") 
            print(" ",end="")
            count = count + 1
    else:
        print("\r")
        count = 0
        if prime_check(ls[i]) == True:
            print(str(ls[i]),end=" ")
    i = i + 1