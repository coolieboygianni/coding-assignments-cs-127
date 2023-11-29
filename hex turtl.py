#Name: Gianni Russell
#gianni.russell07@myhunter.cuny.edu
#Date: September 26, 2023
#This program asks the user for a input of a hexstring color then prints a turtle shape with that color.
import turtle

# Ask the user for the hexcode of a color
hexcode = input("Enter the hexcode of a color: ")

# Create a turtle and set its color to the specified color
t = turtle.Turtle()
t.color(hexcode)
t.shape("turtle")
