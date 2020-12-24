"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120
live_number = 3


def main():
    graphics = BreakoutGraphics()
    global live_number
    begin = 0


    while True:
        pause(FRAME_RATE)
        if begin == 0:
            graphics.window.add(graphics.label_Game_S)
            pause(1700)
        begin = 1

        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        if graphics.ball.y >= graphics.window.height:
            live_number -= 1
            if live_number == 2:
                graphics.window.remove(graphics.life_3)
            if live_number == 1:
                graphics.window.remove(graphics.life_2)

            if live_number > 0:
                graphics.reset_ball()
                graphics.reset_dx()
                graphics.reset_dy()
                graphics.switch = 0
            else:
                graphics.window.remove(graphics.life_1)
                graphics.window.add(graphics.label_e)
                break

        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.change_dx()

        if graphics.ball.y <= 0:
            graphics.change_dy()

        obj = graphics.object()
        if obj is not None:
            graphics.brick_or_paddle()


if __name__ == '__main__':
    main()
