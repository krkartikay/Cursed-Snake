import cursebox
import snake

def main():
    level = int(raw_input("Level? [1-10] "))
    with cursebox.Cursebox() as cb:
        # TODO: ask level within curses
        game = snake.SnakeGame(level, cb.width,cb.height)
        cb.timeout(game.timeout)
        keypress = ""
        while keypress!="CTRL+C" and game.running:
            game.tick(keypress)
            drawscreen(game, cb)
            keypress = str(cb.poll_event())
    # TODO: Maintain highscore list here
    pass

def drawscreen(game, cb):
    pass

main()
