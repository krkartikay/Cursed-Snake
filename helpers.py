# CONSTANTS
UP,DOWN,LEFT,RIGHT = 1,2,3,4
directions = [UP,DOWN,LEFT,RIGHT,'w','a','s','d']
MODE_TORODIAL = 5
MODE_BLOCKING = 6

def log(message):
    with open("log.txt","a") as f:
        f.write(message+"\n")

def direction(dirn):
    if dirn=="UP" or dirn=='w':
        return UP
    if dirn=="DOWN" or dirn=='s':
        return DOWN
    if dirn=="LEFT" or dirn=='a':
        return LEFT
    if dirn=="RIGHT" or dirn=='d':
        return RIGHT

def reverse_direction(dirn):
    rev_directions = [DOWN,UP,RIGHT,LEFT,'s','d','w','a']
    return rev_directions[directions.index(dirn)]

def movept(pt,dirn):
    x,y = pt
    if dirn==UP or dirn=='w':
        return (x,y-1)
    if dirn==DOWN or dirn=='s':
        return (x,y+1)
    if dirn==LEFT or dirn=='a':
        return (x-1,y)
    if dirn==RIGHT or dirn=='d':
        return (x+1,y)
