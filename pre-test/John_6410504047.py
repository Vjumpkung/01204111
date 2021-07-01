import math
while True:
    #row
    m = int(input("row : "))
    if not 1 <= m <= 1000:
        print("row can accept from 1 to 1000")
    else: 
        break
while True:
    #col
    n = int(input("col : "))
    if not 1 <= m <= 1000:
        print("col can accept from 1 to 1000")
    else: 
        break
matrix = []
for i in range(m):
    row=[]
    for j in range(n):
        while True:
            get_price = int(input("price row no. " + str(i+1) + " col no. " + str(j+1) +" : "))
            if not 0 <= get_price <= 100000:
                print("price can accept from 1 to 100000")
            elif get_price == "":
                print("no input detected please input again")
            else:
                break
        row.append(get_price)
    matrix.append(row)
print(matrix)
#หากาฝาก
#row loop
totalnum = []
kafaklist = []
for k1 in range(m):
    #col loop
    for k2 in range(n):
        if 0 == matrix[k1][k2]:
            print("----------------------------------------")
            print("row " + str(k1+1) + " col " + str(k2+1) + " is 0 ")
            #check matrix first
            try:
                north = matrix[k1-1][k2]
                if k1-1 < 0 or k2 < 0:
                    north = 0
            except IndexError:
                north = 0
            print("north = " + str(north))
            if north != 0:
                totalnum.append(north)
            try:
                south = matrix[k1+1][k2]
                if k1+1 < 0 or k2 < 0:
                    south = 0
            except IndexError:
                south = 0
            print("south = " + str(south))
            if south != 0:
                totalnum.append(south)
            try:
                east  = matrix[k1][k2+1]
                if k1 < 0 or k2+1 < 0:
                    east = 0
            except IndexError:
                east = 0
            print("east = "  + str(east))
            if east != 0:
                totalnum.append(east)
            try:
                west  = matrix[k1][k2-1]
                if k1 < 0 or k2-1 < 0:
                    west = 0
            except IndexError:           
                west = 0
            print("west = " + str(west))
            if west != 0:
                totalnum.append(west)
            totalrange = len(totalnum)
            print("total range : "+str(totalrange))
            if not totalrange == 0:
                kafakprice = math.floor((north + east + south + west)/totalrange)
            else: 
                kafakprice = 0
            print("กาฝากมีมูลค่า : " + str(kafakprice))
            kafaklist.append(kafakprice)
            north = 0
            south = 0
            east = 0
            west = 0
            totalnum = []
            print("----------------------------------------")
        #else:
            #print("ไม่มีกาฝาก")
print("มูลค่าเฉลี่ยของกาฝาก : " + str(kafaklist))

#แทนที่ 0 เป็นมูลค่าเฉลี่ยของกาฝาก
y = 0
def kafakcount(x):
    print("replace 0 with " + str(kafaklist[x]))
    return(kafaklist[x])
for p in range(m):
    for q in range(n):
        if 0 == matrix[p][q]:
            matrix[p][q] = kafakcount(y)
            y = y + 1
        
#check min max 
print(matrix)
sortprice = []
sum_of_min = []
sum_of_max = []
for k3 in range(m):
    sum_of_min.append(min(matrix[k3]))
    sum_of_max.append(max(matrix[k3]))
print("min : " + str(sum(sum_of_min)))
print("max : " + str(sum(sum_of_max)))