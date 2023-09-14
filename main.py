from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# setting up screen size, bg colour
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
scoreboard = Scoreboard()
# Creating three box snake by "snake = Snake()"
snake = Snake()
# creating food on screen by "food = Food()"
food = Food()
# listening to keyboard input to move the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
# moving the snake continuously by while loop & snake.move()
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detecting the collision of food and produced the food in random place
    if snake.box_list[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.recall()
    if snake.box_list[0].xcor() > 280 or snake.box_list[0].xcor() < -280 or snake.box_list[0].ycor() > 280 or snake.box_list[0].ycor() < -280:
        is_game_on = False
        scoreboard.game_over()
        scoreboard.highest_score()
    for n in snake.box_list[1:]:
        if snake.box_list[0].distance(n) < 10:
            is_game_on = False
            scoreboard.game_over()
            scoreboard.highest_score()

screen.exitonclick()
