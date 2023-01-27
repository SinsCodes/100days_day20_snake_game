from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)
##1.SNAKEBODY
snake=Snake()
food=Food()
score=Score()
## CONTROLSNAKE
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


##2.MOVE THE SNAKE
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on=False
        score.game_over()
    for segment in snake.segments[1:]:
        # if snake.head==segment:
        #     pass

        if snake.head.distance(segment) < 10:

            game_is_on=False
            score.game_over()









screen.exitonclick()