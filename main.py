import turtle 
from constants import screensize
from Grid import Grid
import math
import random

t = turtle.Turtle()
t.ht()
t.screen.addshape('assets/Cell_tile.gif')
t.screen.tracer(0)

paused = True

def toggle_pause(x, y):
    global paused
    paused = not paused
    
def init_game():
    global t
    t.screen.setup(screensize[0], screensize[1])
    t.screen.onscreenclick(toggle_pause, 1)

    render_tick()

    t.screen.onkeypress(grid.up, 'w')
    t.screen.onkeypress(grid.down, 's')
    t.screen.onkeypress(grid.left, 'a')
    t.screen.onkeypress(grid.right, 'd')
    
    t.pen(speed=0, shown=False)

def render_tick():
    global t, paused

    if not paused:
        grid.render_tick()

    t.screen.update()
    
    turtle.ontimer(render_tick, 100)


grid = Grid()
init_game()

t.screen.listen()
t.screen.mainloop()
