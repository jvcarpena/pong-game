from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Welcome to the Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-360, 0))
pong_ball = Ball()
score_board = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(pong_ball.movement_speed)
    pong_ball.move()

    # Detect collision with wall in terms of y
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce()

    # Detect collision with paddle
    if (pong_ball.distance(right_paddle) < 50 and pong_ball.xcor() > 330 or pong_ball.distance(left_paddle) < 50
            and pong_ball.xcor() < -340):
        pong_ball.paddle_bounce()

    # Detect R paddle misses
    if pong_ball.xcor() > 380:
        pong_ball.reset_move()
        score_board.l_add_score()

    # Detect L paddle misses
    if pong_ball.xcor() < -380:
        pong_ball.reset_move()
        score_board.r_add_score()

    # Detect score exceeds 5 and exit the game
    if score_board.r_score == 5 or score_board.l_score == 5:
        game_is_on = False
        score_board.game_over()

screen.exitonclick()
