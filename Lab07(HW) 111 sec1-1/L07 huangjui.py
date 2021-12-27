def new_prachan_buy(gid):
    want_to = []
    for i in range(len(gid)):
        for j in range(len(gid[0])):
            if i >= 0 and j >= 0 and i+1 < len(gid) and j+1 < len(gid[0]):
                want_to.append(gid[i][j] + gid[i][j+1]*1.1 + gid[i+1][j+1]*1.1 + gid[i+1][j]*1.1**2)
                gid = gid[::-1]
            if i >= 0 and j >= 0 and i+1 < len(gid) and j+1 < len(gid[0]):
                want_to.append(gid[i][j] + gid[i][j+1]*1.1 + gid[i+1][j+1]*1.1 + gid[i+1][j]*1.1**2)
                gid = gid[::-1]
    return want_to
col = []
while True:
    row = []
    x = input() 
    if x == "": break 
    row = list(map(int,x.split()))
    col.append(row)
if len(new_prachan_buy(col)) > 0:
    print(f"{min(new_prachan_buy(col)):.2f}")
else:
    print("Can't Buy")