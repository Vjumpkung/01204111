keyy,valuee = [],[]
for k in range(int(input("Number of inputs: "))):
  x = input()
  y = x.split()
  keyy.append(y[0])
  valuee.append(int(y[1]))
dictt = dict(zip(keyy,valuee))
while True:
  stu = input("student: ")
  if stu is "":
    print("End")
    break
  print(f"{stu}'s score is {dictt[stu]}")