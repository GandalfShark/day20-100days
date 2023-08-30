from turtle import Turtle
from random import randint
# screen is 600 by 600 so values are 300 to -300 in increments of 20


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        # make the food a yellow 10 by 10 circle
        self.speed("fastest")
        self.spawn_food()

    def spawn_food(self):
        self.goto(randint(-280, 280), randint(-280, 280))


