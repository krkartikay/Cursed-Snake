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
        self.grid = [[" " for x in range(width)]
                          for y in range(height)]
        self.timeout = 1000-100*(level-1)
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
        self.setGrid(self.snakeHead, 'O')
        cur_pt = self.snakeHead
        for i in range(5):
            cur_pt = movept(cur_pt, reverse_direction(self.direction))
            self.setGrid(cur_pt, '=')

    def setGrid(self, pt, value):
        # TODO: improve this fxn, use self.mode
        x,y = pt
        try:
            self.grid[y][x] = value
        except IndexError as e:
            self.running = False
            # TODO: print "game over"

    def tick(self, evt):
        self.snakeHead = movept(self.snakeHead, self.direction)
        self.setGrid(self.snakeHead, 'O')
        cur_pt = self.snakeHead
        for i in range(5):
            cur_pt = movept(cur_pt, reverse_direction(self.direction))
            self.setGrid(cur_pt, '=')
        cur_pt = movept(cur_pt, reverse_direction(self.direction))
        self.setGrid(cur_pt, ' ')

    def movefwd():
        pass
