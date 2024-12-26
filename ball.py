from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.forward(20)
        self.x_move = 1
        self.y_move = 1
        self.movement_speed = 0.006

    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def reset_move(self):
        self.goto(0, 0)
        self.movement_speed = 0.006
        self.paddle_bounce()

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.movement_speed *= 0.9

