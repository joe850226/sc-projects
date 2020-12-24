"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.filled = True
ball.fill_color = 'cyan'


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball, START_X, START_Y)
    # if ball.x == START_X and ball.y == START_Y:
    onmouseclicked(start_bouncing)



def start_bouncing(mouse):
    """
    This function lets the ball start bouncing when the user click first time.
    Besides, when the ball bounces out of the window, the ball would return
    to the beginning position.
    """
    clicked_to_start = window.get_object_at(mouse.x, mouse.y)
    if clicked_to_start is None or clicked_to_start is not None:
        VY = 0
        while True:
            ball.move(VX, VY)
            VY = VY + GRAVITY
            if ball.y >= 500:
                VY = -VY * REDUCE
            pause(DELAY)
            # if clicked_to_start is None or clicked_to_start is not None:
            #     pass
            if ball.x >= window.width:
                break
        window.add(ball, START_X, START_Y)



if __name__ == "__main__":
    main()
