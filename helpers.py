# CONSTANTS
UP,DOWN,LEFT,RIGHT = 1,2,3,4
directions = [UP,DOWN,LEFT,RIGHT]
MODE_TORODIAL = 5
MODE_BLOCKING = 6

def direction(dirn):
    if dirn=="UP":
        return UP
    if dirn=="DOWN":
        return DOWN
    if dirn=="LEFT":
        return LEFT
    if dirn=="RIGHT":
        return RIGHT

def reverse_direction(dirn):
    rev_directions = [DOWN,UP,RIGHT,LEFT]
    return rev_directions[directions.index(dirn)]

def movept(pt,dirn):
    x,y = pt
    if dirn==UP:
        return (x,y-1)
    if dirn==DOWN:
        return (x,y+1)
    if dirn==LEFT:
        return (x-1,y)
    if dirn==RIGHT:
        return (x+1,y)
