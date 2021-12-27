hight = int(input("hight of electric poles : "))
num_electric = int(input("number of electric poles : "))
i = 1
electric = []
while i <= num_electric:
    input_electric = int(input())
    electric.append(input_electric)
    i = i+1
electric.sort()
if int(max(electric)/int(electric[-2])) >= 3:
    mean1 = int((sum(electric)-max(electric))/(len(electric)-1))
    mean2 = int((max(electric))/(int((max(electric))/(int(electric[-2])))))
    mean = int(mean1 + mean2)
    print(f"Avg : {mean}")
    if hight <= 1 and mean <= 3000:
        print("NO")
    elif 1 < hight <= 4 and mean <= 10000:
        print("NO") 
    elif 4 < hight <= 8 and mean <= 50000:
        print("NO")
    elif 8 < hight and mean <= 100000:
        print("NO")
    else:
        if 10000 > mean >= 3000:
            print("YES "+ str(mean - 3000))
        elif 50000 > mean >= 10000:
            print("YES "+ str(mean - 10000))
        elif 100000 > mean >= 50000:
            print("YES "+ str(mean - 50000))
        elif mean >= 100000:
            print("YES "+ str(mean - 100000))
else:
    mean = int(sum(electric)/len(electric))
    print(f"Avg : {mean}")
    if hight <= 1 and mean <= 1000:
        print("NO")
    elif 1 < hight <= 4 and mean <= 5000:
        print("NO") 
    elif 4 < hight <= 8 and mean <= 30000:
        print("NO")
    elif 8 < hight and mean <= 75000:
        print("NO")
    else:
        if 5000 > mean >= 1000:
            print("YES "+ str(mean - 1000))
        elif 30000 > mean >= 5000:
            print("YES "+ str(mean - 5000))
        elif 75000 > mean >= 30000:
            print("YES "+ str(mean - 30000))
        elif mean >= 75000:
            print("YES "+ str(mean - 75000))