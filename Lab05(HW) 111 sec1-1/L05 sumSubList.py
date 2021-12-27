#sumSubList
x_xx = list(map(int,input().split()))
xx = x_xx
while True:
  x,y=map(int,input().split())
  #print(f"addition from {xx.index(xx[x])} to {xx.index(xx[y])}")
  if (x < -len(xx) or x > len(xx) - 1) and (-len(xx) <= y <= len(xx) - 1):
    print("x Bad Input")
  elif (y < -len(xx) or y > len(xx) - 1) and (-len(xx) <= x <= len(xx) - 1):
    print("y Bad Input")
  elif (x < -len(xx) or x > len(xx) - 1) and (y < -len(xx) or y > len(xx) - 1):
    print("x and y Bad Input")
  elif x % len(xx) > y % len(xx) :
    break
  else:
    x %= len(xx)
    y %= len(xx) 
    from1 = x
    to1 = y
    print(sum(xx[from1:to1 + 1]))