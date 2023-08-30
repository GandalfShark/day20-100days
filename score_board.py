import turtle
from turtle import Turtle
FONT = ("Courier", 15, "normal")
BIGFONT = ("Courier", 35, "normal")
ALIGN = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("red")
        self.goto(0, 230)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f"FEED THE SNAKE!\nYour Score is {self.score}", font=FONT, align=ALIGN)

    def update_score(self):
        self.score += 1
        self.display_score()

    def game_over_man(self):
        self.goto(0,0)
        self.write(arg="GAME OVER!", font=BIGFONT, align=ALIGN)

