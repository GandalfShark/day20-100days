
from turtle import Turtle
MOVE_DIST = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 360
# these are constants

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            # this makes the 3 parts of the snake based on start coordinates

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    # adds a new segment to the snake

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DIST)
        # iterate through the segments, move each one to the position of the one in front of it
        # finally move the head forward the MOVE_DIST value

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
    # Methods for snake movement where the front of the snake is rotated

