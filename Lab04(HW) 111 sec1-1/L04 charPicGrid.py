vertical_grid =    [['a11','a12','a13','a14','a15','a16'],
                    ['a21','a22','a23','a24','a25','a26'],
                    ['a31','a32','a33','a34','a35','a36'],
                    ['a41','a42','a43','a44','a45','a46'],
                    ['a51','a52','a53','a54','a55','a56'],
                    ['a61','a62','a63','a64','a65','a66'],
                    ['a71','a72','a73','a74','a75','a76'],
                    ['a81','a82','a83','a84','a85','a86'],
                    ['a91','a92','a93','a94','a95','a96']]

horizontal_grid = [['a11','a12','a13','a14','a15','a16','a17','a18','a19'],
                   ['a21','a22','a23','a24','a25','a26','a27','a28','a29'],
                   ['a31','a32','a33','a34','a35','a36','a37','a38','a39'],
                   ['a41','a42','a43','a44','a45','a46','a47','a48','a49'],
                   ['a51','a52','a53','a54','a55','a56','a57','a58','a59'],
                   ['a61','a62','a63','a64','a65','a66','a67','a68','a69']]

vertical_grid_2 =  [['a11','a12','a13','a14','a15','a16','a17'],
                    ['a21','a22','a23','a24','a25','a26','a27'],
                    ['a31','a32','a33','a34','a35','a36','a37'],
                    ['a41','a42','a43','a44','a45','a46','a47'],
                    ['a51','a52','a53','a54','a55','a56','a57'],
                    ['a61','a62','a63','a64','a65','a66','a67'],
                    ['a71','a72','a73','a74','a75','a76','a77'],
                    ['a81','a82','a83','a84','a85','a86','a87'],
                    ['a91','a92','a93','a94','a95','a96','a97']]

horizontal_grid_2 = [['a11','a12','a13','a14','a15','a16','a17','a18','a19'],
                     ['a21','a22','a23','a24','a25','a26','a27','a28','a29'],
                     ['a31','a32','a33','a34','a35','a36','a37','a38','a39'],
                     ['a41','a42','a43','a44','a45','a46','a47','a48','a49'],
                     ['a51','a52','a53','a54','a55','a56','a57','a58','a59'],
                     ['a61','a62','a63','a64','a65','a66','a67','a68','a69'],
                     ['a71','a72','a73','a74','a75','a76','a77','a78','a79']]

grid1 = [['.','.','.','.','.','.'],
         ['.','o','o','.','.','.'],
         ['o','o','o','o','.','.'],
         ['o','o','o','o','o','.'],
         ['.','o','o','o','o','o'],
         ['o','o','o','o','o','.'],
         ['o','o','o','o','.','.'],
         ['.','o','o','.','.','.'],
         ['.','.','.','.','.','.']]

grid2 = [['.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.'],
         ['.','.','.','.','o','.','o'],
         ['o','o','.','o','.','o','.'],
         ['o','o','o','o','o','.','.'],
         ['o','o','.','o','.','o','.'],
         ['.','.','.','.','o','.','o'],
         ['.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.']]

def rotate_left(grid):
    b = list(map(list, zip(*grid)))[::-1]
    return(b)

def rotate_right(grid):
    grid1_check = False
    grid2_check = False
    if len(grid) == 6 : grid1_check = True
    elif len(grid) == 7 : grid2_check = True
    if len(grid[0]) == len(vertical_grid[0]):
        grid1_check = True
        #print("case1")
        a = grid
        b = horizontal_grid
        for i in range(len(horizontal_grid)):
            #print(f" i = {i}")
            for j in range(len(vertical_grid)):
                b[i][j] = a[j][i]

    elif len(grid[0]) == len(vertical_grid_2[0]):
        grid2_check = True
        #print("case2")
        a = grid
        b = horizontal_grid_2
        for i in range(len(horizontal_grid_2)):
            #print(f" i = {i}")
            for j in range(len(vertical_grid_2)):
                b[i][j] = a[j][i]

    elif len(grid[0]) == len(horizontal_grid[0]) and grid1_check == True:
        #print("case3")
        a = grid
        b = vertical_grid
        for i in range(len(vertical_grid)):
            #print(f" i = {i}")
            for j in range(len(horizontal_grid)):
                #print(f" j = {j}")
                b[i][j] = a[j][i]
        for k1 in range(len(b)):
            b[k1].reverse()

    elif len(grid[0]) == len(horizontal_grid_2[0]) and grid2_check == True:
        #print("case4")
        a = grid
        b = vertical_grid_2
        for i in range(len(vertical_grid_2)):
            #print(f" i = {i}")
            for j in range(len(horizontal_grid_2)):
                b[i][j] = a[j][i]
        for k1 in range(len(b)):
            b[k1].reverse()
    return(b)

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j],end="")
        print("\r")
