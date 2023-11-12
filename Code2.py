import turtle
from turtle import *

width,height,bg_color = 5000, 5000, 'white'

turtle.setup()
turtle.screensize(width,height,bg_color)

print("Use your arrow key to move")
print("Enter c to set color")
print("Enter w to set width")
print("Enter z when you want to fill a shape and enter x after completing the figer")
print("Enter o to draw / in up side")
print("Enter i to draw \ in up side")
print("Enter k to draw / in down side")
print("Enter l to draw \ in down side")

setup(500, 500)
Screen()
a = turtle.Turtle()
a.speed(0)

turtle.title("Python Turtle Drawing")

W = 100

def up():
    a.setheading(90)
    a.forward(W)

def down():
    a.setheading(270)
    a.forward(W)
  
def left():
    a.setheading(180)
    a.forward(W)
  
def right():
    a.setheading(0)
    a.forward(W)

W2 = 141.42

def o():
    a.setheading(45)
    a.forward(W2)

def i():
    a.setheading(135)
    a.forward(W2)

def k():
    a.setheading(225)
    a.forward(W2)

def l():
    a.setheading(315)
    a.forward(W2)



def w():
    c = int(input('Enter the of width : '))
    a.width(c)

def c():
    b = input('Enter the of color : ')
    a.color(str(b))

def start_fill():
    a.begin_fill()

def stop_fill():
    a.end_fill()

def clear():
    a.clear()

listen()

onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')

onkey(o, 'o')
onkey(i, 'i')
onkey(k, 'k')
onkey(l, 'l')

onkey(c, 'c')
onkey(w, 'w')

onkey(clear, 'e')

onkey(start_fill, 'z')
onkey(stop_fill, 'x')

mainloop()