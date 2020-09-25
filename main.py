import turtle
import random


def main():
  global jae
  global y
  global z
  global colorFade
  y = 50
  z = 3
  colorFade = 256
  jae = turtle.Turtle()
  jae.speed(10)
  while True:
    jae.penup()
    jae.goto(0,-50)
    jae.pendown()
    triangle(y)
    if y <= 0:
      jae.right(30)
      colorFade = 256
      y = 50

    y -= z
    colorFade -= 10
      #rectangle(random.randint(10,50),random.randint(10,50), random.randint(0,500),random.randint(0,500))
      #jae.right(random.randint(0,90))


def beginTurtle():
  jae.fillcolor(colorFade,0,0)
  jae.begin_fill()

def rectangle(width,height,x_start,y_start):
  jae.penup()
  jae.goto(x_start, y_start)
  jae.pendown()
  beginTurtle()
  jae.forward(width)
  jae.right(90)
  jae.forward(height)
  jae.right(90)
  jae.forward(width)
  jae.right(90)
  jae.forward(height)
  jae.right(90)
  jae.end_fill()

def square(width,x_start,y_start):
  rectangle(width, width,x_start,y_start)

def triangle(length):
  beginTurtle()
  jae.forward(length)
  jae.right(120)
  jae.forward(length)
  jae.right(120)
  jae.forward(length)
  jae.right(120)
  jae.end_fill()


def circle(diameter):
  beginTurtle()
  jae.circle(diameter)
  jae.end_fill()

main()







