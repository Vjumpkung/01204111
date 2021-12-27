a = input("Input name: ")
a_ = a[::-1]
for i in range(len(a)):
    print(a.replace(a[i],a[i].upper()) + " " + a_.replace(a_[i],a_[i].upper()))