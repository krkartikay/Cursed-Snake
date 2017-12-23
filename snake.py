"""
This file will define the logic of the snake game
by providing a SnakeGame() class
"""

import random
from helpers import *

class SnakeGame():
    """Logic of SnakeGame"""
    def __init__(self, level, width, height):
        self.width = width
        self.height = height
        self.snake = [] # list of positions in which snake exists
        self.food = (0,0)
        self.cleargrid()
        self.timeout = 100-10*(level-1)
        self.running = True
        # Initialise Snake
        self.direction = random.choice(directions)
        self.mode = MODE_BLOCKING
        init_len = 5
        self.snakelen = init_len
        # start somewhere near in the center ...
        # snake shouldn't be too close to the edge
        self.snakeHead = (random.choice(range(2*init_len,width-2*init_len)),
                          random.choice(range(2*init_len,height-2*init_len)))
        self.food = (random.choice(range(width)),
                     random.choice(range(height)))
        self.cleargrid()
        self.drawGrid()

    def setGrid(self, pt, value):
        # TODO: improve this fxn, use self.mode
        x,y = pt
        max_y = len(self.grid)
        max_x = len(self.grid[0])
        self.grid[y%max_y][x%max_x] = value

    def cleargrid():
        self.grid = [[" " for x in range(width)]
                          for y in range(height)]

    def drawGrid():
        cur_pt = self.snakeHead
        for i in range(5):
            cur_pt = movept(cur_pt, reverse_direction(self.direction))
            self.setGrid(cur_pt, '=')
        cur_pt = movept(cur_pt, reverse_direction(self.direction))
        self.setGrid(cur_pt, ' ')

    def tick(self, evt):
        self.snakeHead = movept(self.snakeHead, self.direction)
        self.setGrid(self.snakeHead, 'O')
        self.cleargrid()
        self.drawGrid()

    def movefwd():
        pass
