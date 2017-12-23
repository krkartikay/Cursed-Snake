import cursebox
import snake

def main():
    level = int(raw_input("Level? [1-10] "))
    with cursebox.Cursebox() as cb:
        # TODO: ask level within curses
        game = snake.SnakeGame(level, cb)
        keypress = ""
        while keypress!="CTRL+C":
            game.refreshScreen()
            keypress = str(cb.poll_event())

main()
