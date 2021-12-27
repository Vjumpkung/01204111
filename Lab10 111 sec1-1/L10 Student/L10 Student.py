import csv
maxx = -1
minn = 1e9

def read_csv(filename):
    with open(filename) as f:
        global maxx , minn
        datas = csv.reader(f)
        data = [ i for i in datas]
        for i in range(1,len(data)) :
            maxx = max(maxx,int(data[i][6]))
            minn = min(minn,int(data[i][7]))
    return data
class Std(object):
    
    def __init__(self, *args):
        self.id, self.gender, self.race, self.parental, self.lunch, self.test, self.math, self.reading, self.writing = args
        
    def show_data(self):
        print(f'''gender : {self.gender}
race/ethnicity : {self.race}
parental level of education : {self.parental}
lunch : {self.lunch}
test preparation course : {self.test}
math score : {self.math}
reading score : {self.reading}
writing score : {self.writing}''')
    def less_from_max_math_score(self):
        print(f"less than max : {maxx - int(self.math)}")
    def more_from_min_reading_score(self):
        print(f"more than min : {int(self.reading) - minn}")
    def can_pass(self):
        if (int(self.math)+ int(self.reading)+ int(self.writing)) > 240:
            print(f"Pass")
        else:
            print(f"Can't pass")
    def __repr__(self):
        return f"math score : {self.math}, reading score : {self.reading}, writing score : {self.writing}"
    
filename = input("Filename : ")
datas = read_csv(filename)
classes = list()
for i in range(1,len(datas)) :
    data = Std(datas[i][0],datas[i][1],datas[i][2],datas[i][3],datas[i][4],datas[i][5],datas[i][6],datas[i][7],datas[i][8])
    classes.append(data)


menu = int(input("Menu : "))
id = input("ID : ")
for i in classes :
    if i.id == id :
        if menu == 1 : # show data
            i.show_data()
        elif menu == 2 : # less_from_max_math_score
            i.less_from_max_math_score()
        elif menu == 3 : # more_from_min_reading_score
            i.more_from_min_reading_score()
        elif menu == 4: # can_pass
            i.can_pass()
        elif menu == 5: # print
            print(i)
        break