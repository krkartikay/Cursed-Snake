import cursebox
import snake

def main():
    level = int(raw_input("Level? [1-10] "))
    with cursebox.Cursebox() as cb:
        # TODO: ask level within curses
        game = snake.SnakeGame(level, cb.width, cb.height-1)
        cb.screen.timeout(game.timeout)
        keypress = ""
        escapekeys = ["CTRL+C","q","ESC"]
        while keypress not in escapekeys and game.running:
            game.tick(keypress)
            drawscreen(game, cb)
            keypress = str(cb.poll_event())
    # TODO: Maintain highscore list here
    pass

def drawscreen(game, cb):
    cb.clear()
    for y in range(game.height):
        for x in range(game.width):
            cb.put(x,y, str(game.grid[y][x]),
                fg = cursebox.colors.white,
                bg = cursebox.colors.black)
            # TODO: perform some checks here on the output
            # string and select colors accordingly
            pass

main()
