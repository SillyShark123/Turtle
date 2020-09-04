import turtle
import random


def main():
  global jae
  global y
  global z
  global colorFade
  y = 500
  z = 30
  colorFade = 256
  jae = turtle.Turtle()
  jae.speed(10)
  while True:
    jae.penup()
    jae.goto(0,-1000)
    jae.pendown()
    circle(y)
    colorFade -= 20
    y -= z
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


def circle(diameter):
  beginTurtle()
  jae.circle(diameter)
  jae.end_fill()

main()







