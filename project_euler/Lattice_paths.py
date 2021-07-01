import math
def TotalRoute(x,y):
    route = int(math.factorial(x*y))/((int(math.factorial(x))*int(math.factorial(y))))
    return (route)
print(TotalRoute(2,2))

