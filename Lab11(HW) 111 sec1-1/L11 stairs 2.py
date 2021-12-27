n = int(input('n : '))
a,b,c = int(input('a : ')),int(input('b : ')),int(input('c : '))
if (a or b or c) > n:
    print(0)
else:
    def find_possible(n):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        else:
            return find_possible(n-a)+find_possible(n-b)+find_possible(n-c)
    print(find_possible(n))