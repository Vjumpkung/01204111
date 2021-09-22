import time
inp = input('File name: ')
with open(inp) as fp:
  data = fp.readlines()
  data_nohead = data[1:]
  data_nohead = [data_nohead[i].strip().split(",") for i in range(len(data_nohead))]
  data = [data[i].strip().split(",") for i in range(len(data))]
  data_nohead = list(map(list,zip(*data_nohead)))
  data = list(zip(*data))
datanum = [list(map(int,i)) for i in data_nohead[:len(data_nohead)-1]]
t1 = time.time()
for num in range(1,11):
    if num == 1:
        print(len(data[0]))
    elif num == 2:
        maxdata = [max(i) for i in datanum]
        print(data[maxdata.index(max(maxdata))][0])
    elif num == 3:
        top3 = sorted(datanum[5],reverse=True)[0:3]
        print(*top3)
    elif num == 4:
        axis_1 = list(map(list,zip(*datanum)))
        sum_axis_1 = [sum(axis_1[i]) for i in range(len(axis_1))]
        print(data_nohead[-1][sum_axis_1.index(max(sum_axis_1))],max(sum_axis_1))
    elif num == 5:
        print(data_nohead[-1][datanum[0].index(max(datanum[0]))],max(datanum[0]))
    elif num == 6:
        print(len([datanum[17][i] for i in range(len(datanum[17])) if datanum[17][i] > 500]))
    elif num == 7:
        print(sum([1 if datanum[7][i] > datanum[4][i] else 0 for i in range(len(datanum[0]))]))
    elif num == 8:
        axis_1 = list(map(list,zip(*datanum)))
        sum_axis_1 = [sum(axis_1[i]) for i in range(len(axis_1))]
        radio = [100*(datanum[26][i]/sum_axis_1[i]) for i in range(len(datanum[0]))]
        print(data_nohead[-1][radio.index(max(radio))])
    elif num == 9:
        axis_1 = list(map(list,zip(*datanum)))
        sum_axis_1 = [sum(axis_1[i]) for i in range(len(axis_1))]
        print(len([i for i in sorted([100*sum(sorted(axis_1[i],reverse=True)[0:2])/sum_axis_1[i] for i in range(len(axis_1))],reverse=True) if i > 70]))
    elif num == 10:
        print(len([i for i in range(len(datanum[-1])) if datanum[-1][i] == 0]))
    else:
        pass
t2 = time.time()
print(t2-t1)