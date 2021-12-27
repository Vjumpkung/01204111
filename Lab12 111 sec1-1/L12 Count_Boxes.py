def box_size(A,B,C):
    res = ""
    if B <= 10 and A <= 15 and C <= 8 :
        print("Box size 1 ")
        res = 1
    elif A <= 25 and B <= 15 and C <= 12 :
        print("Box size 2 ")
        res = 2
    elif B <= 40 and A <= 50 and C <= 20 :
        print("Box size 3 ")
        res = 3
    else:
        print("Oversize product")
        res = None
    return res
N = int(input("N: "))
total_box = {1 : 0 , 2 : 0 , 3 : 0}
for i in range(1,N+1):
    try:
        total_box[box_size(int(input(f"Order {i} A: ")),int(input(f"Order {i} B: ")),int(input(f"Order {i} C: ")))] += 1
    except KeyError:
        pass
for i in total_box:
    print(f"Use Box size {i}: {total_box[i]}")