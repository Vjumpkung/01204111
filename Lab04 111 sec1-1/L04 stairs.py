def draw(m):
    for i in range(len(m)):
        print(m[i]*(i+1))
while True:
    p = input()
    m = p.split()
    if str(m[-1]) == '0':
        print("Good Bye.")
        break
    draw(m)