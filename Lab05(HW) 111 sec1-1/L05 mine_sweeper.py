def print_matrix_2(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^1}', end = ' ')
        print("\r")
def create_matrix(x,y):
    matrix=[] 
    row=[]
    for i in range(x):
        row=[]
        for j in range(y): 
            row.append(0)
        matrix.append(row)
    return (matrix)
n1n = input("Grid Size: ").split()
mine = int(input("Number of mine(s): "))
gid = create_matrix(int(n1n[1]),int(n1n[0]))
lcr = [-1,0,1]
for i in range(mine):
  minex = input(f"Mine#{i+1}: ").split()
  gid[int(minex[1])][int(minex[0])] = "X"
for i in range(len(gid)):
  for j in range(len(gid[0])):
    if not gid[i][j] == "X":
      grid = gid
      for x in range(3):
        for y in lcr:
          try: 
            if grid[i+lcr[x]][j+lcr[y]] == "X" and (i+lcr[x]) >= 0 and (j+lcr[y]) >= 0 :
              grid[i][j] = grid[i][j] + 1
          except IndexError:
              pass
print_matrix_2(grid)