#Name: Gianni Russell
#gianni.russell07@myhunter.cuny.edu
#Date: September 19, 2023
#This program makes a turtle draw s turtle shape then makes that shape draw a hexagon with the color cornflower blue
import turtle

t= turtle.Turtle()
t.shape("turtle")
t.color("cornflowerblue")

for i in range(5):
  t.forward(100) 
  t.left(72)
