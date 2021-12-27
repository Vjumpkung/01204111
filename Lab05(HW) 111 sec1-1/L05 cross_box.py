num = int(input())
def draw(n):
  print("."*n)
  j = n-4
  for i in range(0,n//2-1):
    print(".",end="")
    print(" "*i,end="")
    print(".",end="")
    print(" "*((n-4) - 2*i),end="")
    print(".",end="")
    print(" "*(i) + ".")
    m = i
    nnn = (n-4) - 2*i
  print("."+" "*(n//2-1) + "." +" "*(n//2-1)+".")
  i = 0
  for i in range(0,n//2-1):
    print(".",end="")
    print(" "*(m-i),end="")
    print(".",end="")
    print(" "*(i),end="")
    print(" ",end="")
    print(" "*(i) + ".",end="")
    print(" "*(n//2-2-i),end="")
    print(".")
  print("."*n)
draw(num)