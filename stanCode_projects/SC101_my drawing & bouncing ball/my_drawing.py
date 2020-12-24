"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLabel, GLine, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    This function make a P助 which is the bird in the 卡納赫拉, and the P助 is holding a flag labeled with SC101.
    """
    window = GWindow(width=500, height=400, title="my_paint")
    face = GOval(250, 300, x=150, y=50)
    face.filled = True
    face.fill_color = 'white'
    window.add(face)
    l_eye = GOval(12, 12, x=240, y=110)
    l_eye.filled = True
    l_eye.fill_color = 'black'
    window.add(l_eye)
    r_eye = GOval(12, 12, x=310, y=110)
    r_eye.filled = True
    r_eye.fill_color = 'black'
    window.add(r_eye)
    mouth_up = GOval(30, 13, x=265, y=110)
    mouth_up.filled = True
    mouth_up.fill_color = 'yellow'
    window.add(mouth_up)
    mouth_down = GOval(24, 15, x=269, y=120)
    mouth_down.filled = True
    mouth_down.fill_color = 'yellow'
    window.add(mouth_down)
    r_blush = GOval(50, 50, x=330, y=135)
    r_blush.filled = True
    r_blush.fill_color = 'pink'
    window.add(r_blush)
    l_blush = GOval(50, 50, x=180, y=135)
    l_blush.filled = True
    l_blush.fill_color = 'pink'
    window.add(l_blush)
    r_hand = GOval(20, 60, x=390, y=170)
    r_hand.filled = True
    r_hand.fill_color = 'white'
    window.add(r_hand)
    l_hand = GOval(60, 20, x=100, y=170)
    l_hand.filled = True
    l_hand.fill_color = 'white'
    window.add(l_hand)
    r_leg = GLine(350, 320, 370, 380)
    r_foot = GLine(370, 380, 380, 380)
    l_leg = GLine(200, 320, 180, 380)
    l_foot = GLine(180, 380, 170, 380)
    window.add(r_leg)
    window.add(r_foot)
    window.add(l_leg)
    window.add(l_foot)
    flag_stick = GLine(130, 170, 130, 140)
    window.add(flag_stick)
    flag = GPolygon()
    flag.add_vertex((130, 140))
    flag.add_vertex((130, 70))
    flag.add_vertex((50, 105))
    flag.filled = True
    flag.fill_color = 'white'
    window.add(flag)
    label = GLabel('SC101')
    label.color = 'tomato'
    label.font = 'Courier-15-italic'
    window.add(label, 70, 115)
    pass


if __name__ == '__main__':
    main()
