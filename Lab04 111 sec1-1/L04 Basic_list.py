x = []
from statistics import median
while len(x) != 5:
    p = int(input("Enter a positive number: "))
    if p > 0:
        x.append(p)
print(f"sum: {sum(x)}")
print(f"min: {min(x)}")
print(f"max: {max(x)}")
print(f"med: {median(x)}")