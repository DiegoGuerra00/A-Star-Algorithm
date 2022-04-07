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
            
    
    """ def check_wall(self, neighbor, without_walls):
        for(a,b,c,d) in without_walls:
            if((self.x == a and self.y == b) and (neighbor.x == c and neighbor.y == d)):
                neighbor.wall = False
                return True
            if((self.x == c and self.y == d) and (neighbor.x == a and neighbor.y == b)):
                neighbor.wall = False
                return True
        return False """

    def add_neighbors(self, grid):
        """ if(self.x < cols - 1 and self.check_wall(grid[self.x+1][self.y], without_walls)):
            self.neighbors.append(grid[self.x+1][self.y])
        if(self.x > 0 and self.check_wall(grid[self.x-1][self.y], without_walls)):
            self.neighbors.append(grid[self.x-1][self.y])
        if(self.y < rows - 1 and self.check_wall(grid[self.x][self.y+1], without_walls)):
            self.neighbors.append(grid[self.x][self.y+1])
            
        if(self.x > 0 and self.check_wall(grid[self.x][self.y-1], without_walls)):
            self.neighbors.append(grid[self.x][self.y-1]) """
        # add sides
        if(self.x < cols - 1 and not(grid[self.x+1][self.y].wall)):
            self.neighbors.append(grid[self.x+1][self.y])
        if(self.x > 0 and not(grid[self.x-1][self.y].wall)):
            self.neighbors.append(grid[self.x-1][self.y])
        if(self.y < rows - 1 and not(grid[self.x][self.y+1].wall)):
            self.neighbors.append(grid[self.x][self.y+1])
        if(self.y > 0 and not(grid[self.x][self.y-1].wall)):
            self.neighbors.append(grid[self.x][self.y-1])
        """ # add Diagonals
        if(self.x < cols - 1 and self.y < rows - 1 and not(grid[self.x+1][self.y+1].wall)):
            self.neighbors.append(grid[self.x+1][self.y+1])
        if(self.x < cols - 1 and self.y > 0 and not(grid[self.x+1][self.y-1].wall)):
            self.neighbors.append(grid[self.x+1][self.y-1])
        if(self.x > 0 and self.y < rows - 1 and not(grid[self.x-1][self.y+1].wall)):
            self.neighbors.append(grid[self.x-1][self.y+1])
        if(self.x > 0 and self.y > 0) and not(grid[self.x-1][self.y-1].wall):
            self.neighbors.append(grid[self.x-1][self.y-1]) """