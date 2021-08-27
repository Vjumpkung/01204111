# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def get_data():
    with open('midTermScore_grp01.csv', 'r') as fp:
        data = fp.readlines()[1:68]
        data = [data[i].strip().split(",") for i in range(len(data))]
        data = list(zip(*data))
    return data
data = get_data()


# %%
def total_student ():
    return data[0].count("01204111 Midterm Examination 2564-1")


# %%
def mymean():
    return sum(map(int,data[7]))/total_student()


# %%
def standard_derivation():
    xbar = mymean()
    sd = sum([(int(data[7][i]) - xbar)**2 for i in range(len(data[7]))])/total_student()
    return sd


# %%
def resultss():
    maximum = max(data[7])
    mean = mymean()
    sd = standard_derivation()
    minimum = min(data[7])
    mean = f"{mean:.2f}"
    sd = f"{sd:.2f}"
    return maximum,mean,sd,minimum


# %%
def gradecal():
    grade_result = {
        "A" : 0,
        "B+" : 0,
        "B" : 0,
        "C+" : 0,
        "C" : 0,
        "D+" : 0,
        "D" : 0,
        "F" : 0
    }
    for i in range(len(data[8])):
        if float(data[8][i]) > 85:
            grade_result["A"] += 1
        elif float(data[8][i]) > 79:
            grade_result["B+"] += 1
        elif float(data[8][i]) > 73:
            grade_result["B+"] += 1
        elif float(data[8][i]) > 67:
            grade_result["B+"] += 1
        elif float(data[8][i]) > 60:
            grade_result["B+"] += 1
        elif float(data[8][i]) > 50:
            grade_result["B+"] += 1
        elif float(data[8][i]) > 40:
            grade_result["B+"] += 1
        else:
            grade_result["F"] += 1
    return grade_result


# %%
def main():
    print(total_student())
    print(*resultss())
    Grade = [print(f"{i}: {gradecal()[i]}") for i in gradecal()][0]
main()


