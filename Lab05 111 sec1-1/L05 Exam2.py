#Exam2
namecount = []
keyy,valuee = [],[]
for k in range(int(input("Number of inputs: "))):
  x = input("Input name: ")
  y = float(input("Input score: "))
  namecount.append(x)
  if x in keyy:
    getindex = keyy.index(x)
    valuee[getindex] = (y+valuee[getindex])
  else:
    keyy.append(x)
    valuee.append(float(y))
  #print(keyy)
  #print(valuee)
#print(namecount)
for i in range(len(keyy)):
  #print(namecount.count(keyy[i]))
  valuee[i] = valuee[i]/(namecount.count(keyy[i]))
#print(valuee)
print(f"Top score is {keyy[valuee.index(max(valuee))]}: {max(valuee):.2f}")