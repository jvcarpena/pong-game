from turtle import Turtle

FONT = ('Courier', 40, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-220, 240)
        self.write(arg=f"{self.l_score}", align="center", font=FONT)
        self.goto(220, 240)
        self.write(arg=f"{self.r_score}", align="center", font=FONT)

    def r_add_score(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def l_add_score(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.teleport(0, 0)
        self.write(arg="GAME OVER!", align="center", font=FONT)
