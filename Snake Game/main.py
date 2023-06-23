from turtle import Screen
from snek import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("grey")
screen.title("Ostrava Snake Game")
screen.tracer(0)


snek = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.right, "Right")
screen.onkey(snek.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snek.move()

    if snek.head.distance(food)<15:
        food.refresh()
        snek.extend()
        scoreboard.score_count()

    if snek.head.xcor() > 280 or snek.head.xcor() < -280 or snek.head.ycor() > 280 or snek.head.xcor() < -280:
        scoreboard.reset()
        snek.reset_snake()

    for segments in snek.segments[1:]:
        if snek.head.distance(segments) < 10:
            scoreboard.reset()
            snek.reset_snake()








screen.exitonclick()