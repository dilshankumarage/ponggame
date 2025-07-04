import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
r_score = Scoreboard((-200,290))
l_score = Scoreboard((+200,290))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.hit_wall()

    if (ball.distance(r_paddle.paddle) < 50 and ball.xcor() > 320) or \
            (ball.distance(l_paddle.paddle) < 50 and ball.xcor() < -320):
        ball.hit_paddle()

    if ball.xcor() > 380:
        ball.reset()
        r_score.increase_score()  # Left player scores a point

    if ball.xcor() < -380:
        ball.reset()
        l_score.increase_score()  # Right player scores a point




screen.exitonclick()