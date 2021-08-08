#L06 ลุงเล็กอยากไปเที่ยวจัง 2
N = int(input("N = "))
M = int(input("M = "))
cod = []
possible_M = []
"""N=6
M=2"""
#cod = [4,2,2,3,4,2]
for i in range(N):
    cod.append(int(input(f"cost of day {i+1} = ")))
cursor = 0
for _ in iter(int,1):
    try:
        possible_M.append(sum(cod[cursor:cursor+M]))
        cursor += 1
        if cursor+M > len(cod):
            break
    except IndexError:
        break
print(f"Min cost of {M} days = {min(possible_M)}")