def even_check(num):
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
def prime_check(num):
        if num in [2,3,5,7]:
            print("The number is prime")
        elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num == 1:
            print("The number is not prime")
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
Number = int(input("Number : "))
even_check(Number)
prime_check(Number)