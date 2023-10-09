import turtle
from turtle import *

width,height,bg_color = 5000, 5000, 'white'

turtle.setup()
turtle.screensize(width,height,bg_color)

print("Enter c to set color")
print("Enter a when you want to fill a shape and enter b after completing the figer")

setup(500, 500)
Screen()
turtle = turtle.Turtle()
turtle.speed(0)
turtle.width(5)
 
 
def up():
    turtle.setheading(90)
    turtle.forward(100)
 
 
def down():
    turtle.setheading(270)
    turtle.forward(100)
 
 
def left():
    turtle.setheading(180)
    turtle.forward(100)
 
 
def right():
    turtle.setheading(0)
    turtle.forward(100)
 
def color():
    while True:
        a = input('Enter the of color: ')
        turtle.color(str(a))

def start_fill():
    turtle.begin_fill()

def stop_fill():
    turtle.end_fill()
 
listen()
onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')

onkey(color, 'c')

onkey(start_fill, 'a')
onkey(stop_fill, 'b')

mainloop()