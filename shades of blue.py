#Name: Gianni Russell
#gianni.russell07@myhunter.cuny.edu
#Date: September 19, 2023
#this program makes a turtle draw all the shades of blue


import turtle				


tur = turtle.Turtle()		
tur.shape("turtle")		
tur.backward(100)		


for i in range(0,255,10):
  tur.forward(10)		
  tur.pensize(i)		
  tur.color(0,0,i)
