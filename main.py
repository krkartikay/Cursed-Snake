from cursebox import *
with Cursebox() as cb:
    greeting = "Hello Curses"
    keypress = None
    while keypress!="CTRL+C":
        width, height = cb.width, cb.height
        # Center text on the screen
        cb.put(x=(width - len(greeting)) / 2,
               y=height / 2, text=greeting,
               fg=colors.black, bg=colors.white)
        # Wait for any keypress
        cb.screen.timeout(200)
        keypress = str(cb.poll_event())
        greeting = str(keypress)
        if greeting=="":
            greeting = "SKIP"
