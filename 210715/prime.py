myprime = list(range(1,10000))
def even_check(num):
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
def prime_check(num):
        if num in [2,3,5,7]:
            print("The number is prime")
            return True
        elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num == 1:
            print("The number is not prime")
            return False
        else:
            i = 8
            while True:
                if num % 1 == 0 and num % i == 0:
                    if num == i :
                        print("The number is prime")
                        break
                    else:
                        print("The number is not prime")
                        break
                else:
                    i = i + 1
            return True
import time
prime_counter = 0
not_prime_counter = 0
for i in range(len(myprime)):
    print(f"This number is {myprime[i]}")
    prime_check(myprime[i])
    prime_counter += 1
    if prime_check(myprime[i]) == False:
        not_prime_counter += 1
print(f"not prime counter : {not_prime_counter}")