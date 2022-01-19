from turtle import Turtle, Screen

lucho = Turtle()
screen = Screen()


def move_forwards():
    lucho.forward(10)


def move_backwards():
    lucho.backward(10)


def move_left():
    lucho.left(10)


def move_right():
    lucho.right(10)


def clear_screen():
    lucho.speed(0)
    lucho.clear()
    lucho.hideturtle()
    lucho.penup()
    lucho.home()
    lucho.pendown()
    lucho.showturtle()


screen.listen()
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()

