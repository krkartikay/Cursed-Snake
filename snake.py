"""
This file will define the logic of the snake game
by providing a SnakeGame() class
"""

import random
from helpers import *

class SnakeGame():
    """Logic of SnakeGame"""
    def __init__(self, level, width, height):
        self.status_left = "LEVEL = %d"%level
        self.status_right = "Hello, Player!"
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
        init_len = 6
        # start somewhere near in the center ...
        # snake shouldn't be too close to the edge
        cur_pt = (random.choice(range(2*init_len,width-2*init_len)),
                          random.choice(range(2*init_len,height-2*init_len)))
        self.food = (random.choice(range(width)),
                     random.choice(range(height)))
        for i in range(init_len):
            cur_pt = movept(cur_pt, self.direction)
            self.snake.insert(0,cur_pt)
        self.snakeHead = cur_pt
        self.cleargrid()
        self.drawGrid()

    def setGrid(self, pt, value):
        # TODO: improve this fxn, use self.mode
        x,y = pt
        max_y = len(self.grid)
        max_x = len(self.grid[0])
        self.grid[y%max_y][x%max_x] = value

    def cleargrid(self):
        self.grid = [[" " for x in range(self.width)]
                          for y in range(self.height)]

    def drawGrid(self):
        for pt in self.snake:
            self.setGrid(pt, '=')
        self.setGrid(self.snakeHead, 'O')

    def tick(self, evt):
        if evt == "SKIP":
            self.snake.pop()
            self.snakeHead = movept(self.snakeHead,self.direction)
            self.snake.insert(0,self.snakeHead)
            self.cleargrid()
            self.drawGrid()
        elif direction(evt) is not None:
            dirn = direction(evt)
            self.direction = dirn
            self.snake.pop()
            self.snakeHead = movept(self.snakeHead,self.direction)
            self.snake.insert(0,self.snakeHead)
            self.cleargrid()
            self.drawGrid()
