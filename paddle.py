from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.color("white")
        self.goto(position)

    def up(self):
        if self.ycor() != 260:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() != -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)



