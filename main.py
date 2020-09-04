import turtle
import random


def main():
  global jae
  global y
  global z
  y = 100
  z = 30
  jae = turtle.Turtle()
  jae.speed(10)
  while True:
      rectangle(random.randint(10,50),random.randint(10,50), random.randint(0,500),random.randint(0,500))
      jae.right(random.randint(0,90))


def beginTurtle():
  jae.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
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







