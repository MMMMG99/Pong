from turtle import Turtle
MOVEMENT_PACE = 20

class Padle:
    def __init__(self, coordonate):
        self.bucata = []
        self.create_padle()
        self.padle = self.bucata[0]
        self.padle.goto(coordonate)

    def create_padle(self):
        padle = Turtle("square")
        padle.color('white')
        padle.penup()
        padle.shapesize(stretch_wid=5, stretch_len=1)
        self.bucata.append(padle)

    def up(self):
        x_nou = self.padle.xcor()
        y_nou = self.padle.ycor()
        self.padle.goto(x_nou, y_nou + MOVEMENT_PACE)

    def down(self):
        x_nou = self.padle.xcor()
        y_nou = self.padle.ycor()
        self.padle.goto(x_nou, y_nou - MOVEMENT_PACE)