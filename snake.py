"""
This file will define the logic of the snake game
by providing a SnakeGame() class
"""

import random

# CONSTANTS
UP,DOWN,LEFT,RIGHT = 1,2,3,4

class SnakeGame():
    """Logic of SnakeGame"""
    def __init__(self, level, cursebox):
        self.cb = cursebox
        self.W = self.cb.width
        self.H = self.cb.height
        self.snake = [] # list of positions in which snake exists
        self.snakeHead = (0,0)
        self.direction = RIGHT
        self.snakelen = 0
        self.grid = [[0 for x in range(width)]
                        for y in range(height)]
        self.timeout = 1000-100*(level-1)
        self.cb.screen.timeout(self.timeout)
        # level 1 : timeout : 1   sec
        # level 10: timeout : 0.1 sec
        # TODO: Initialise the snake
    def refreshScreen(self, evt):
        pass
    def movefwd():
        pass
