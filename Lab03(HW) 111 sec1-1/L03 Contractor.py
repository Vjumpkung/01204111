pie = 3.141592653589793
def calculatePrice(v) :
    much = int(input("Price(Bath) per 1 cubic meter: "))
    print(f"The price is {v*much:.2f} Baht.")
def inputShape():
    i_s = int(input("Input Shape: "))
    return i_s
# sh == 1
def calculateSphere():
    rd = int(input("Input radius(meter): "))
    print(f"The volume is {(4/3)*(pie)*(rd**3):.2f} cubic meter.")
    x = (4/3)*(pie)*(rd**3)
    return(x)
# sh == 2
def calculateCone():
    rd = int(input("Input radius(meter): "))
    hi = int(input("Input height(meter): "))
    print(f"The volume is {(1/3)*(pie)*(rd**2)*(hi):.2f} cubic meter.")
    x = (1/3)*(pie)*(rd**2)*(hi)
    return(x)
# sh == 3
def calculateCylinder():
    rd = int(input("Input radius(meter): "))
    hi = int(input("Input height(meter): "))
    print(f"The volume is {(pie)*(rd**2)*(hi):.2f} cubic meter.")
    x = (pie)*(rd**2)*(hi)
    return(x)
# sh == 4
def calculatePrism():
    w = int(input("Input width(meter): "))
    y = int(input("Input length(meter): "))
    h = int(input("Input height(meter): "))
    print(f"The volume is {w*y*h:.2f} cubic meter.")
    x = w*y*h
    return(x)
# sh == 5
def calculatePyramid():
    w = int(input("Input width(meter): "))
    y = int(input("Input length(meter): "))
    h = int(input("Input height(meter): "))
    area = w * y * h / 3
    print(f"The volume is {area:.2f} cubic meter.")
    x = area
    return(x)
#-----------------------------------------------------------------------------
sh = inputShape()
if sh == 1:
    v = calculateSphere()
elif sh == 2:
    v = calculateCone()
elif sh == 3:
    v = calculateCylinder()
elif sh == 4:
    v = calculatePrism()
elif sh == 5:
    v = calculatePyramid()
calculatePrice(v)
