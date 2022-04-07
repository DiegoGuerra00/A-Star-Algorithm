from tkinter import messagebox
import math
import time
from window import Window
from spot import Spot

# array for the grid and the sets used in the a*
cols, rows = 100, 100
grid = [[0 for x in range(cols)] for y in range(rows)]
open_set = []
closed_set = []
path = []


def create_maze(rows, cols):
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = Spot(i, j)

    for i in range(rows):
        for j in range(cols):
            grid[j][i].add_neighbors(grid)


def calculate_heuristic(a, b):
    return (math.pow((a.x - b.x), 2) + math.pow((a.y - b.y), 2))


def a_star(start, end):
    create_maze(rows, cols)
    start_time = time.time()
    found_path = False
    window = Window()
    window.on_init()
    window.on_render(grid, open_set, closed_set, path)
    start = grid[start[0]][start[1]]
    end = grid[end[0]][end[1]]
    start.wall = False
    end.wall = False
    open_set.append(start)

    def get_min_f(open_set):
        index = 0
        for i in range(len(open_set)):
            if(open_set[i].f < open_set[index].f):
                index = i
        return index

    while(len(open_set) > 0):
        window.on_render(grid, open_set, closed_set, path)
        current = open_set[get_min_f(open_set)]
        open_set.remove(current)
        closed_set.append(current)

        if(current.x == end.x and current.y == end.y):
            found_path = True
            temp = current
            while(temp.previous):
                path.append(temp.previous)
                temp = temp.previous
            path.reverse()
            path.append(end)
            window.render_path(grid, path)
            while(not(messagebox.showinfo(message='Path found in ' + str(time.time() - start_time).format(':.2f') + ' seconds'))):
                window.on_cleanup()
            break

        neighbors = current.neighbors
        for i in range(len(neighbors)):
            neighbor = neighbors[i]

            if(not(neighbor in closed_set)):
                temp_g = current.g + 1

                new_path = False
                if(neighbor in open_set):
                    if(temp_g < neighbor.g):
                        neighbor.g = temp_g
                        new_path = True
                elif(not(neighbor in open_set)):
                    neighbor.g = temp_g
                    new_path = True
                    open_set.append(neighbor)

                if(new_path):
                    neighbor.h = calculate_heuristic(neighbor, end)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.previous = current
        neighbors.clear()

    if(not(found_path)):
        messagebox.showinfo(message='No path found')

def main():
    start = (0, 0)
    end = (cols-1, rows-1)  
    a_star(start, end)


if __name__ == "__main__":
    main()
