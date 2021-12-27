#Zoo
keyy,valuee = [],[]
my = int(input("How many animals are there in the zoo? : "))
for i in range(my):
  x = input()
  y = x.split()
  keyy.append(y[0])
  valuee.append(y[1])
dictt = dict(zip(keyy,valuee))
many = int(input("How many questions do you want to ask? : "))
for i in range(many):
  kkk = input()
  try:
    print(dictt[kkk])
  except KeyError:
    print("Sorry we don't have that animal.")