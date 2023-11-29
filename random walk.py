#Name: Gianni Russell
#Date: November 21, 2023
import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(10)
  a = random.randrange(360)
  trey.right(a)