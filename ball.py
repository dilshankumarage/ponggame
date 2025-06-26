from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.y_move = 10
        self.x_move = 10

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor,y_cor)
    def hit_wall(self):
        self.y_move *= -1
    def hit_paddle(self):
        self.x_move *= -1
    def reset(self):
        self.goto(0,0)
        self.hit_paddle() #changing direction


