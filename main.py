from turtle import Turtle, Screen

lucho = Turtle()
screen = Screen()


def move_forwards():
    lucho.forward(10)


def move_left():
    lucho.left(10)


def move_right():
    lucho.left(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_right)
screen.exitonclick()

