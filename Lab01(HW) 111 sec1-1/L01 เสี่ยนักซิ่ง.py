speedA = int(input("A : "))
speedB = int(input("B : "))
distanceX = int(input("X : "))
print("Wait : " + str(int(((distanceX/speedA) - (distanceX/speedB)) * 3600)) + " sec")