keyyyyy = []
valueeeee = []
for _ in iter(int,1):
    valuee = int(input("Student ID : "))
    if valuee == 0:
        break
    keyy = int(input("years : "))
    valueeeee.append(valuee)
    keyyyyy.append(keyy)
#college = {4: [1], 1: [2, 4], 2: [3]}
#print(college)
seperate = int(input("Separate year: "))
newcollege = list(zip(keyyyyy,valueeeee))
#print(newcollege)
for i in range(len(newcollege)):
    if newcollege[i][0] >= seperate:
        print(newcollege[i][1])