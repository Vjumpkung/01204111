import copy
def prachan_buy(gid):
    buyls = []
    nesw_m = [-1,1,0,0]
    nesw_n = [0,0,1,-1]
    clockwise_m = [0,0,1,1]
    clockwise_n = [0,1,1,0]
    counter_m = [0,0,-1,-1]
    counter_n = [0,1,1,0]
    Counter_clockwise = False
    grid = copy.deepcopy(gid)
    for m in range(len(grid)):
        for n in range(len(grid[0])):
            for k in range(2):
                want_to = []
                grid = copy.deepcopy(gid)
                if Counter_clockwise == False:
                    Counter_clockwise = True
                    try:
                        for pos in range(4):
                            if (m + clockwise_m[pos]) >= 0 and (n + clockwise_n[pos]) >= 0:
                                want_to.append(grid[m + clockwise_m[pos]][n + clockwise_n[pos]]) 
                                for direct in range(4):
                                    try:
                                        if (m + clockwise_m[pos] + nesw_m[direct] >= 0 ) and (n + clockwise_n[pos] + nesw_n[direct] >= 0):
                                            grid[m + clockwise_m[pos] + nesw_m[direct]][n + clockwise_n[pos] + nesw_n[direct]] *= 1.1
                                    except IndexError:
                                        pass
                        if len(want_to) == 4:            
                            buyls.append(sum(want_to))  
                    except IndexError:
                        continue
                else:
                    Counter_clockwise = False
                    try:
                        for pos in range(4):
                            if m + counter_m[pos] >= 0 and n + counter_n[pos] >= 0:
                                want_to.append(grid[m + counter_m[pos]][n + counter_n[pos]]) 
                                for direct in range(4):
                                    try:
                                        if (m + counter_m[pos] + nesw_m[direct] >= 0) and (n + counter_n[pos] + nesw_n[direct] >= 0):
                                            grid[m + counter_m[pos] + nesw_m[direct]][n + counter_n[pos] + nesw_n[direct]] *= 1.1
                                    except IndexError:
                                        pass
                        if len(want_to) == 4:            
                            buyls.append(sum(want_to))       
                    except IndexError:
                        continue
    return buyls
'''col = []
while True:
    row = []
    x = input() 
    if x == "": break 
    row = list(map(int,x.split()))
    col.append(row)'''
def check_answer(col):
    if not len(col[0]) != len(col[1]):
        print(f"{min(prachan_buy(col)):.2f}")
    else:
        print("Can't Buy")
col1 = [[10, 12, 50], [50, 40, 20]]
col2 = [[90, 31, 14, 67, 84],
 [71, 25, 43, 60, 64],
 [11, 97, 13, 92, 28],
 [73, 30, 47, 56, 54],
 [23, 55, 20, 58, 16],
 [33, 49, 95, 90, 22],
 [42, 55, 38, 52, 36]]
col3 = [[1,2,3,4,5,6,7,8,9,10],
 [11,12,13,14,15,16,17,18,19,20],
 [21,22,23,24,25,26,27,28,29,30],
 [31,32,33,34,35,36,37,38,39,40],
 [41,42,43,44,45,46,47,48,49,50],
 [51,52,53,54,55,56,57,58,59,60]]
check_answer(col1)
check_answer(col2)
check_answer(col3)