from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.x_misca = 10
        self.y_misca = 20

    def move_up_right(self):
        x_nou = self.xcor()
        y_nou = self.ycor()
        self.goto(x_nou + self.x_misca, y_nou + self.y_misca)

    def lovitura(self):
        self.y_misca *= -1

    def lovitura_jucator(self):
        self.x_misca *= -1

    def inapoi(self):
        self.goto(0, 0)