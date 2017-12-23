"""
This file will define the logic of the snake game
by providing a SnakeGame() class
"""

import random

# CONSTANTS
UP,DOWN,LEFT,RIGHT = 1,2,3,4

class SnakeGame():
    """Logic of SnakeGame"""
    def __init__(self, level, width, height):
        self.width = width
        self.height = height
        self.snake = [] # list of positions in which snake exists
        self.snakeHead = (0,0)
        self.direction = RIGHT
        self.snakelen = 0
        self.grid = [[0 for x in range(width)]
                        for y in range(height)]
        self.timeout = 1000-100*(level-1)
        self.running = True
        # level 1 : timeout : 1   sec
        # level 10: timeout : 0.1 sec
        # TODO: Initialise the snake
    def tick(self, evt):
        pass
    def movefwd():
        pass
