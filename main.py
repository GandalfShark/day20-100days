"""
Classic Snake game from 100 days of Python
"""
from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score_board import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Feed the Snake")
screen.tracer(0)
# setting up the screen

snake = Snake()
game_on = True
snack = Food()

# setting up the snake and score board
board = ScoreBoard()
while game_on:
    # begins main loop of game
    screen.update()
    # re-draw the screen
    sleep(0.1)
    snake.move()
    screen.listen()
    screen.onkey(snake.up, "Up")
    # call the snake.up method from the snake class when UP is pressed
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # print(f"snake is going: {snake.segments[0].heading()}")
    # test code for snake movement

    if snake.segments[0].distance(snack) < 15:
        board.update_score()
        snack.spawn_food()
        snake.grow()
    # Using turtle distance method to see if food and snake are in the same place
    # food gets moved to a new place if the snake comes within 15 px of center of food

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -300:
        game_on = False
        board.game_over_man()
    # checks to see if the snake has gone off the screen "hit the wall"

    for seg in snake.segments[1:]:
        if seg.distance(snake.segments[0]) < 10:
            game_on = False
            board.game_over_man()
        # check to see if the segment is in the same place as the head
        # this detects collisions with the snake hitting itself
        # snake.segments[1:] is slicing the list of segments to just the tail

# this needs to stay at the bottom
screen.exitonclick()
