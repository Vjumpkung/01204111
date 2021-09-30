from pprint import pprint
import numpy as np
import time
import random
def printmat(mat):
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      print(mat[i][j], end = " ")
    print()
M = int(input("M: "))
N = int(input("N: "))
# lst = [[3,3,1,1],
#        [2,2,1,2],
#        [1,1,1,2]]
#lst = [[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6]]
# lst = [[4,7,8,2,6],
#        [5,10,9,3,1]]
# lst = [[7,7,3],
#        [8,4,2],
#        [3,1,9]]
#pprint(np.array(lst))
while True:
    time.sleep(3)
    lst = [[random.randint(1,11) for j in range(N)] for i in range(M)]
    #lst = [list(map(int,input().split())) for i in range(M)]
    print('---before---')
    print(np.array(lst))
    if len(lst) == len(lst[0]):
        lst = list(map(list,zip(*lst)))[::-1]
    else:
        lst = [i[::-1] for i in lst]
    kkk = []
    for ind,val in enumerate(lst):
        for j,x in enumerate(val):
            kkk.append((ind,j))
    #print(sorted(kkk , key = lambda x : sum(x) , reverse=True),end="\n\n")
    ind_pos = 0
    kkk = sorted(kkk , key = lambda x : sum(x) , reverse=True)
    #print(kkk)
    get_current_i = 0
    for i in range(min([len(lst),len(lst[0])])):
        #print('loop 1 ')
        #print((ind_pos,ind_pos+i+1))
        #print(kkk[ind_pos:ind_pos+i+1])
        templst = []
        #print(i+1 , kkk[ind_pos:ind_pos+i+1])
        for p in kkk[ind_pos:ind_pos+i+1]:
            #print(p)
            #print(lst[x][y])
            templst.append(lst[p[0]][p[1]])
        templst.sort()
        for x,y in enumerate(kkk[ind_pos:ind_pos+i+1]):
            #print(x,y)
            lst[y[0]][y[1]] = templst[x]
            pass
        #print()
        ind_pos += 1+i
        get_current_i = i
    #print("lastest pos is",ind_pos,"and i is",get_current_i)
    iii = get_current_i
    for k in range(ind_pos,1+(len(kkk)-1)//2):
        #print('loop 2 ')
        #print(iii+1 , kkk[ind_pos:ind_pos+iii+1])
        templst = []
        for p in kkk[ind_pos:ind_pos+iii+1]:
            templst.append(lst[p[0]][p[1]])
        templst.sort()
        for x,y in enumerate(kkk[ind_pos:ind_pos+iii+1]):
            lst[y[0]][y[1]] = templst[x]
            pass
        ind_pos += 1+iii
    #print((min([len(lst),len(lst[0])])-(min([len(lst),len(lst[0])])//2)))

    if len(lst) == len(lst[0]) == 3:
        for j in range(1,-2,-1):
            #print('loop 2.5')
            templst = []
            #print(j+1 , kkk[ind_pos:ind_pos+j+1])
            for p in kkk[ind_pos:ind_pos+j+1]:
                #print(p)
                #print(lst[x][y])
                templst.append(lst[p[0]][p[1]])
            templst.sort()
            for x,y in enumerate(kkk[ind_pos:ind_pos+j+1]):
                #print(x,y)
                lst[y[0]][y[1]] = templst[x]
                pass
            #print()
            ind_pos += 1+j
    else:
        for j in range(min([len(lst),len(lst[0])])-(min([len(lst),len(lst[0])])//2),-1,-1):
            #print('loop 3 ')
            #print((ind_pos,ind_pos+j+1))
            #print(kkk[ind_pos:ind_pos+j+1])
            templst = []
            #print(j+1 , kkk[ind_pos:ind_pos+j+1])
            for p in kkk[ind_pos:ind_pos+j+1]:
                #print(p)
                #print(lst[x][y])
                templst.append(lst[p[0]][p[1]])
            templst.sort()
            for x,y in enumerate(kkk[ind_pos:ind_pos+j+1]):
                #print(x,y)
                lst[y[0]][y[1]] = templst[x]
                pass
            #print()
            ind_pos += 1+j
    #printmat(lst[::-1])
    print('sorted matrix is:')
    print(np.array([i[::-1] for i in lst]))
    #printmat([i[::-1] for i in lst])