def maximum(x):
    while len(x) > 1:
        if x[0] >= x[-1]:
            x.pop(-1)
        else:
            x.pop(0)
    return(x[0])
def top_3(x):
    nen = len(x)
    third = -99999
    second = -99999
    first = -99999
    for i in range(0,nen):
        if (x[i] > first):
            third = second
            second = first
            first = x[i]
        elif (x[i] > second):
            third = second
            second = x[i]
        elif (x[i] > third):
            third = x[i]
    return(first, second, third)
def summ(A):
    total = 0
    for i in A:
        total = total + i
    return total
def create_matrix(m,n):
    mat = []
    for i in range(m):
        col = []
        for j in range(n):
            col.append(0)
        mat.append(col)
    return mat
def sort_data(A):
    n = len(A)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
    return A
def convert_data(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = int(A[i][j])
    return A
def zipped(A):
    trans_mat = create_matrix(len(A[0]),len(A))
    for i in range(len(trans_mat)):
        for j in range(len(trans_mat[0])):
            trans_mat[i][j] = A[j][i]
    return trans_mat
fna = input("File name: ")
#nen = int(input("enter number: "))
with open(fna) as fp:
    rawdata = fp.readlines()
    headdata = rawdata[0]
    data = rawdata[1:]
    for i in range(len(data)):
        data[i] = data[i].strip().split("\n")
    data_split = []
    for i in range(len(data)):
        data_split.append(data[i][0].split(","))
newdata = zipped(data_split)
datanum = convert_data(newdata[:len(newdata)-1])
def find_data(num):
    if num == 1:
        print(len(newdata[0])+1)
    elif num == 2:
        maxdata = []
        kor2_1 = datanum.copy()
        for i in range(len(kor2_1)):
            maxdata.append(sort_data(kor2_1)[-1])
        kor2 = maximum(maxdata)
        print(rawdata[0].strip().split(",")[maxdata.index(kor2)])
    elif num == 3:
        top3 = top_3(datanum[5].copy())
        print(*top3)
    elif num == 4 :
        kore4_1 = datanum.copy()
        axis_1 = zipped(kore4_1)
        sum_axis_1 = []
        for i in range(len(axis_1)):
            sum_axis_1.append(summ(axis_1[i]))
        kor4 = maximum(sum_axis_1)
        print(newdata[-1][sum_axis_1.index(kor4)],kor4)
    elif num == 5:
        zero = datanum[0].copy()
        max_data_num = maximum(zero)
        print(newdata[-1][datanum[0].index(max_data_num)],max_data_num)
    elif num == 6:
        more_than_500 = []
        for i in datanum[17]:
            if i > 500:
                more_than_500.append(i)
        print(len(more_than_500))
    elif num == 7:
        kor7 = []
        for i in range(len(datanum[0])):
            if datanum[7][i] > datanum[4][i]:
                kor7.append("A")
            else:
                pass
        print(len(kor7))
    elif num == 8:
        sumnao = datanum.copy()
        axis_1 = zipped(sumnao)
        sum_axis_1 = []
        for i in range(len(axis_1)):
            sum_axis_1.append(summ(axis_1[i]))
        radio = []
        for i in range(len(sumnao[0])):
            radio.append(100*sumnao[26][i]/sum_axis_1[i])
        newradio = radio.copy()
        newradio = maximum(newradio)
        print(newdata[-1][radio.index(newradio)])
    elif num == 9:
        sumnao2 = datanum.copy()
        axis_1 = zipped(sumnao2)
        sum_axis_1 = []
        for i in range(len(axis_1)):
            sum_axis_1.append(summ(axis_1[i]))
        srt = []
        for i in range(len(axis_1)):
            wait = sort_data(axis_1[i])[::-1]
            srt.append(100*summ(wait[0:2])/sum_axis_1[i])
        k = []
        for i in srt:
            if i > 70:
                k.append(i)
        print(len(k))
    elif num == 10:
        u = []
        for i in range(len(datanum[-1])):
            if datanum[-1][i] == 0:
                u.append(i)
        print(len(u))
import time
t1 = time.time()
for x in range(1,11):
    find_data(x)
t2 = time.time()
print(t2-t1)