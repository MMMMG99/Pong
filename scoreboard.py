from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0, 250)
        self.color('white')
        self.penup()
        self.scor = [0, 0]
        self.actualizare_scor()
        self.hideturtle()

    def actualizare_scor(self):
        self.write(f'{self.scor[0]} : {self.scor[1]}', move=False, align='center', font=('Arial', 20, 'bold'))

    def marire_scor_jucator_drepta(self):
        self.scor[1] += 1
        self.clear()
        self.actualizare_scor()

    def marire_scor_jucator_stanga(self):
        self.scor[0] += 1
        self.clear()
        self.actualizare_scor()