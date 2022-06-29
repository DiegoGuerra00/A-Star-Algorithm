from random import randint

# dimensions of the grid
cols, rows = 100, 100

# class defining the cells on the grid
class Spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.previous = None
        self.wall = False

        if(randint(0, 100) > 70):
            self.wall = True
            
    def add_neighbors(self, grid):
        # add sides
        if(self.x < cols - 1 and not(grid[self.x+1][self.y].wall)):
            self.neighbors.append(grid[self.x+1][self.y])
        if(self.x > 0 and not(grid[self.x-1][self.y].wall)):
            self.neighbors.append(grid[self.x-1][self.y])
        if(self.y < rows - 1 and not(grid[self.x][self.y+1].wall)):
            self.neighbors.append(grid[self.x][self.y+1])
        if(self.y > 0 and not(grid[self.x][self.y-1].wall)):
            self.neighbors.append(grid[self.x][self.y-1])
