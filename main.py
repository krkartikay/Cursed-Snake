import cursebox
import snake
from copy import deepcopy as cp

oldscreen = []
log = []

def main():
    global oldscreen
    with cursebox.Cursebox() as cb:
        # TODO: ask level within curses
        game = snake.SnakeGame(cb.width, cb.height-1)
        cb.screen.timeout(game.timeout)
        keypress = ""
        escapekeys = ["CTRL+C","q","ESC"]
        i = 0
        oldscreen = [[0 for x in range(cb.width)] for y in range(cb.height-1)]
        while keypress not in escapekeys: # and game.running:
            game.tick(keypress)
            drawscreen(game, cb)
            drawstatus(game.status_left,game.status_right,cb)
            cb.screen.timeout(game.timeout)
            keypress = str(cb.poll_event())
    # TODO: Maintain highscore list here
    pass

def drawscreen(game, cb):
    #cb.clear()
    global oldscreen
    log.append("Hello")
    for y in range(game.height):
        for x in range(game.width):
            if game.grid[y][x] != oldscreen[y][x]:
                cb.put(x,y, str(game.grid[y][x]),
                    fg = cursebox.colors.white,
                    bg = cursebox.colors.black)
    oldscreen=cp(game.grid)
    # TODO: perform some checks here on the output
    # string and select colors accordingly
    pass

def drawstatus(st_l,st_r,cb):
    y = cb.height
    spaces = cb.width - len(st_r)-len(st_l)
    s = st_l+" "*spaces+st_r
    cb.put(0,y-1,s,cursebox.colors.white,cursebox.colors.black)

if __name__=="__main__":
    main()
