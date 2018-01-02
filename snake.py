"""
This file will define the logic of the snake game
by providing a SnakeGame() class
"""

import random
from helpers import *

class SnakeGame():
    """Logic of SnakeGame"""
    def __init__(self, width, height):
        self.inserting = 0
        level = 1
        self.level = level
        self.status_left = "LEVEL = %d"%level
        self.status_right = "Hello, Player!"
        self.width = width
        self.height = height
        self.snake = [] # list of positions in which snake exists
        self.food = (0,0)
        self.cleargrid()
        self.timeout =  (100-10*(self.level-1))/10
        self.running = True
        # Initialise Snake
        self.direction = random.choice(directions)
        self.mode = MODE_BLOCKING
        init_len = 6
        # start somewhere near in the center ...
        # snake shouldn't be too close to the edge
        cur_pt = (random.choice(range(1*init_len,width-1*init_len)),
                          random.choice(range(1*init_len,height-1*init_len)))
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
        self.setGrid(self.food, '#')

    def cmppts(self,pt1,pt2):
        x1,y1 = pt1
        x2,y2 = pt2
        if (x1-x2)%self.width==0 and (y1-y2)%self.height==0:
            return True
        else:
            return False

    def tick(self, evt):
        if evt == "SKIP":
            pass
        elif direction(evt) is not None:
            dirn = direction(evt)
            if reverse_direction(self.direction) != dirn:
                self.direction = dirn
        if self.running:
            self.snakeHead = movept(self.snakeHead,self.direction)
            if self.snakeHead in self.snake:
                self.running = False
                self.status_right = "Game Over!"
            if self.cmppts(self.snakeHead, self.food):
                self.inserting = 15
                if self.level==10:
                    self.status_right = "You Win"
                    self.running = False
                self.level += 1
                self.status_left = "LEVEL = %d"%self.level
                self.food = (random.choice(range(self.width)),
                             random.choice(range(self.height)))
                if self.level<8:
                    self.timeout = (100-10*(self.level-1))/10
                else:
                    self.timeout = 0
            if self.inserting>0:
                self.inserting -= 1
            else:
                self.snake.pop()
            self.snake.insert(0,self.snakeHead)
            self.cleargrid()
            self.drawGrid()
