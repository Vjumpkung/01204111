N = int(input())
wait_num = list(range(1,N**2+1))
blank_mat,ind = [[0 for j in range(N)] for i in range(N)],0
LowerLeft,UpperRight,UP,RIGHT = (1,1),(-1,-1),(-1,0),(0,1)

current_pos = [len(blank_mat)-1,0]
blank_mat[current_pos[0]][current_pos[1]],ind = wait_num[ind],1
current_pos[0],current_pos[1] = current_pos[0] + UP[0] , current_pos[1] + UP[1]
isLowerRight,isUpperLeft = True,False

while ind < N**2:
    if isLowerRight:
        while True:
            blank_mat[current_pos[0]][current_pos[1]] = wait_num[ind]
            if (0 <= current_pos[0]+1 < len(blank_mat) and 0 <= current_pos[1]+1 < len(blank_mat)): #predict future
                current_pos[0],current_pos[1] = current_pos[0] + LowerLeft[0] , current_pos[1] + LowerLeft[1]
                isLowerRight,isUpperLeft = False,False
                ind += 1
            else:
                if (0 <= current_pos[0] < len(blank_mat) and 0 <= current_pos[1]+1 < len(blank_mat)): #predict future
                    current_pos[0],current_pos[1] = current_pos[0] + RIGHT[0] , current_pos[1] + RIGHT[1]
                    isLowerRight,isUpperLeft = False,True
                    ind += 1
                else:
                    current_pos[0],current_pos[1] = current_pos[0] + UP[0] , current_pos[1] + UP[1]
                    isLowerRight,isUpperLeft = False,True
                    ind += 1
                break
            
    if isUpperLeft:
        while True:
            blank_mat[current_pos[0]][current_pos[1]] = wait_num[ind]
            if (0 <= current_pos[0]-1 < len(blank_mat) and 0 <= current_pos[1]-1 < len(blank_mat)): #predict future
                current_pos[0],current_pos[1] = current_pos[0] + UpperRight[0] , current_pos[1] + UpperRight[1]
                isLowerRight,isUpperLeft = False,False
                ind += 1
            else:
                if (0 <= current_pos[0]-1 < len(blank_mat) and 0 <= current_pos[1] < len(blank_mat)): #predict future
                    current_pos[0],current_pos[1] = current_pos[0] + UP[0] , current_pos[1] + UP[1]
                    isLowerRight,isUpperLeft = True,False
                    ind += 1
                else:
                    current_pos[0],current_pos[1] = current_pos[0] + RIGHT[0] , current_pos[1] + RIGHT[1]
                    isLowerRight,isUpperLeft = True,False
                    ind+=1
                break
            

for x in blank_mat:
    for y in x:
        print(f'{y:3.0f}',end=' ')
    print()