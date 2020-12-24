"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=(self.window.width - ball_radius * 2) / 2,
                          y=(self.window.height - ball_radius * 2) / 2)
        self.ball.filled = True
        self.window.add(self.ball)
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window.width - paddle_width) / 2,
                            y=self.window.height - paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)
        self.life_1 = GRect(10, 20, x=self.window.width - 10 - brick_spacing, y=self.window.height - 20 - brick_spacing)
        self.life_1.filled = True
        self.life_1.fill_color = 'blue'
        self.window.add(self.life_1)
        self.life_2 = GRect(10, 20, x=self.window.width - (10 + brick_spacing) * 2,
                            y=self.window.height - 20 - brick_spacing)
        self.life_2.filled = True
        self.life_2.fill_color = 'blue'
        self.window.add(self.life_2)
        self.life_3 = GRect(10, 20, x=self.window.width - (10 + brick_spacing) * 3,
                            y=self.window.height - 20 - brick_spacing)
        self.life_3.filled = True
        self.life_3.fill_color = 'blue'
        self.window.add(self.life_3)
        self.score = 0
        self.switch = 0
        self.label = GLabel(f'Score:{self.score}', 0, self.window.height)
        self.label.font = "-20"
        self.window.add(self.label)
        self.label_e = GLabel(f'【Game Over】', x=(self.window.width - 180) / 2, y=(self.window.height - 20) / 2)
        self.label_e.font = "-20"
        self.label_Game_S = GLabel(f'【Click For Game Start】', x=(self.window.width - 260) / 2, y=(self.window.height - 20) / 2)
        self.label_Game_S.font = "-20"
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                self.brick = GRect(brick_width, brick_height, x=(brick_width + brick_spacing) * i,
                                   y=brick_offset + (brick_height + brick_spacing) * j)
                self.brick.filled = True
                if j == 0 or j == 1:
                    self.brick.fill_color = 'cyan'
                    self.brick.color = 'pink'
                if j == 2 or j == 3:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'pink'
                if j == 4 or j == 5:
                    self.brick.fill_color = 'purple'
                    self.brick.color = 'pink'
                if j == 6 or j == 7:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'pink'
                if j == 8 or j == 9:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'pink'

                self.window.add(self.brick)

        self.__dx = 0
        self.__dy = 0
        onmousemoved(self.paddle_move)
        onmouseclicked(self.start)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def reset_dx(self):
        self.__dx = 0

    def reset_dy(self):
        self.__dy = 0

    def change_dx(self):
        self.__dx = -self.__dx

    def change_dy(self):
        self.__dy = -self.__dy

    # Start the game
    def start(self, event):
        if self.switch == 0:
            self.set_v()
            self.switch = 1

    def brick_or_paddle(self):
        obj = self.object()
        if obj is self.paddle:
            self.__dy = -self.__dy

        if obj is not self.paddle and obj.y < self.paddle.y:
            self.window.remove(obj)
            self.__dy = -self.__dy
            self.score += 100
            self.window.remove(self.label)
            self.label = GLabel(f'Score:{self.score}', 0, self.window.height)
            self.label.font = "-20"
            self.window.add(self.label)

    def object(self):
        obj1 = self.window.get_object_at(self.ball.x, self.ball.y)
        obj2 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        obj3 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        obj4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        obj = obj1 or obj2 or obj3 or obj4
        return obj

    def reset_ball(self):
        self.ball = GOval(self.ball.width, self.ball.height, x=(self.window.width - self.ball.width) / 2, y=(self.window.height - self.ball.height) / 2)
        self.ball.filled = True
        self.window.add(self.ball)

    def set_v(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if (random.random()) > 0.5:
            self.__dx = -self.__dx
        if (random.random()) < 0.5:
            self.__dx = -2 * self.__dx

    def paddle_move(self, event):
        if self.paddle.width / 2 >= event.x:
            self.paddle.x = 0
            self.paddle.y = self.paddle.y

        elif event.x >= self.window.width - self.paddle.width / 2:
            self.paddle.x = self.window.width - self.paddle.width
            self.paddle.y = self.paddle.y
        else:
            self.paddle.x = event.x - self.paddle.width / 2
            self.paddle.y = self.paddle.y
