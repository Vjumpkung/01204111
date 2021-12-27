#input
howlong = float(input("Hight : "))
saoprice = float(input("Cost : "))
if howlong <= 1.00 and saoprice <= 1000 :
    print("NO")
elif 1.00 < howlong <= 4.00 and saoprice <= 5000:
    print("NO")
elif 4.00 < howlong <= 8.00 and saoprice <= 30000:
    print("NO")
elif howlong > 8.00 and saoprice <= 75000:
    print("NO")
else:
    print("YES")