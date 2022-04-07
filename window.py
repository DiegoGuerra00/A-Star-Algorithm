from tkinter import Grid
import pygame

# some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# dimensions of the spots on the grid
MARGIN = 1
WIDTH = 8
HEIGHT = 8

# dimensions of the Grid
cols, rows = 100, 100

# class to draw the maze
class Window:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 900, 900

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_render(self, grid, open_set, closed_set, path):
        pygame.display.flip()
        self._display_surf.fill(BLACK)
        for row in range(rows):
            for col in range(cols):
                color = GREY
                if(grid[col][row].wall):
                    color = BLACK
                elif(grid[col][row] in open_set):
                    color = GREEN
                elif(grid[col][row] in closed_set):
                    color = WHITE
                pygame.draw.rect(self._display_surf, color, [(MARGIN + WIDTH) * col + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
                

    def render_path(self, grid, path):
        #draw the path
        for row in range(rows):
            for col in range(cols):
                if(grid[col][row] in path):
                    pygame.draw.rect(self._display_surf, BLUE, [(MARGIN + WIDTH) * col + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
                    pygame.display.flip()
                    

    def on_cleanup(self):
        pygame.quit()