"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause

window = GWindow()


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    while True:
        onmouseclicked(ckicked1)
        pause(500)
        onmouseclicked(clicked2)
        pause(500)


def ckicked1(mouse):
    """
    This function can create a circle when the mouse is clicked at odd times.
    """
    global x0, y0, circle
    circle = GOval(50, 50, x=mouse.x - 25, y=mouse.y - 25)
    circle.filled = True
    circle.fill_color = 'turquoise'
    window.add(circle)
    x0 = mouse.x
    y0 = mouse.y


def clicked2(e):
    """
    This function can draw a line and remove the circle when the mouse is clicked at even times.
    """
    line = GLine(x0, y0, e.x, e.y)
    line.color = 'black'
    window.add(line)
    window.remove(circle)


if __name__ == "__main__":
    main()
