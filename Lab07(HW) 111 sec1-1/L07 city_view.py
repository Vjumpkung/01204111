class city_view():
    def __init__ (self,grid:list = []):
        self.grid = []
        self.tower_count = []
    def tower_counter(self):
        def new_north(grid):
            first_saw = len(grid[0])
            grid = list(zip(*grid))
            more_than_first = []
            for i in range(len(grid)):
                for j in range(1,len(grid[0])):
                    if grid[i][0] < grid[i][j]:
                        try:
                            if grid[i][j-1] < grid[i][j]:
                                more_than_first.append(grid[i][j])
                        except IndexError:
                            continue
            return len(more_than_first) + first_saw
        grid = self.grid
        f_direct = (new_north(grid),new_north(list(zip(*(list(zip(*grid[::-1])))[::-1]))),new_north(list(zip(*grid))[::-1]),new_north(list(zip(*grid[::-1]))))
        nsew = ["N","S","E","W"]
        self.tower_count = list(zip(nsew,f_direct))
    def get_grid(self):
        m,n = map(int,input("City Size: ").split())
        self.grid = [list(map(int,input().split())) for i in range(m)]
    def print_output(self):
        tower_count = self.tower_count
        x = [print(tower_count[i][0],end=" ") for i in range(len(tower_count)) if tower_count[i][1] == max(tower_count)[1]][0]
cv = city_view()
cv.get_grid()
cv.tower_counter()
cv.print_output()