from turtle import Screen
from padle import Padle
from ball import Ball
from scoreboard import Scoreboard
import time

DREAPTA = (350, 0)
STANGA = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

maneta_dreapta = Padle(DREAPTA)
maneta_stanga = Padle(STANGA)
minge = Ball()
scor = Scoreboard()

screen.listen()
screen.onkey(maneta_dreapta.up, 'Up')
screen.onkey(maneta_dreapta.down, 'Down')

screen.onkey(maneta_stanga.up, 'w')
screen.onkey(maneta_stanga.down, 's')

joaca = True
viteza = 0.1
while joaca:
    minge.move_up_right()
    screen.update()
    time.sleep(viteza)
    scor.actualizare_scor()

    if minge.ycor() > 275 or minge.ycor() < -275:
        minge.lovitura()

    if (minge.distance(maneta_stanga.padle) < 50 and minge.xcor() > -340) \
            or (minge.distance(maneta_dreapta.padle) < 50 and minge.xcor() < 340):
        minge.lovitura_jucator()
        viteza -= 0.001

    if minge.xcor() < -370:
        scor.marire_scor_jucator_drepta()
        viteza = 0.1
        minge.inapoi()
        minge.lovitura_jucator()

    if minge.xcor() > 370:
        scor.marire_scor_jucator_stanga()
        viteza = 0.1
        minge.inapoi()
        minge.lovitura_jucator()

screen.exitonclick()