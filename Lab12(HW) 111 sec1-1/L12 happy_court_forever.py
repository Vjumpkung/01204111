L = int(input("Length: "))
W = int(input("Width: "))
court = [list(map(int,input().split())) for i in range(L)]
one_fourtwo = [[1 for i in range(2)] for i in range(4)]
possible_lst = []
for i in range(len(court)):
    for j in range(len(court[0])):
        wait = []
        if len(court[i:i+4]) > 3:
            for row in court[i:i+4]:
                if len(row[j:j+2]) > 1:
                    wait.append(row[j:j+2])
            if not len(wait) == 0:
                u = [x[:] for x in court]
                if (one_fourtwo == wait) and (i != 0 and i+4 != len(u) and j != 0 and j+2 != len(u[0])):
                    for p in range(i,i+4):
                        for q in range(j,j+2):
                            u[p][q] = 'x'
                    possible_lst.append(u)
print(f'{len(possible_lst)} possible court(s)')
for i in possible_lst:
    for p in range(len(i)):
        for q in range(len(i[p])):
            print(i[p][q],end=" ")
        print()
    print()