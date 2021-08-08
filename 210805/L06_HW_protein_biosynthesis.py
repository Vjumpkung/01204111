import math
DNA = input("DNA: ")
RNA = [DNA[i] for i in range(0, len(DNA))]
for i in range(len(RNA)):
    if RNA[i] == "A":
        RNA[i] = "U"
    elif RNA[i] == "C":
        RNA[i] = "G"
    elif RNA[i] == "G":
        RNA[i] = "C"
    elif RNA[i] == "T":
        RNA[i] = "A"
newRNA = ""
for i in range(len(RNA)):
    newRNA = newRNA + RNA[i]
newRNA = newRNA.replace("AUG","*AUG",1)
if "UAA" in newRNA:
    newRNA = newRNA.replace("UAA" , "*UAA" ,1)
if "UGA" in newRNA:
    newRNA = newRNA.replace("UGA" , "*UGA" ,1)
if "UAG" in newRNA:
    newRNA = newRNA.replace("UAG" , "*UAG" ,1)
newerRNA = newRNA.split("*")
#print(newRNA)
countProTEEN = len(newerRNA[1])//3
if len(newerRNA[1])%3 != 0:
    countProTEEN = math.floor(len(newerRNA[1])/3 + countProTEEN)
#print(newerRNA)
print(f"{countProTEEN} Amino acid(s)")