#Name: Gianni Russell
#gianni.russell07@myhunter.cuny.edu
#Date: October 2, 2023

import turtle

# Function to draw a shape using turtle 
def draw_shape(angle):
    turtle.left(angle)
    turtle.forward(100)

#user inputed numbers
def get_user_input():
    user_input = []
    for i in range(5):
        while True:
            try:
                num = int(input("Enter number {i+1}: "))
                user_input.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")
    return user_input




user_input = get_user_input()

# Draw the shape using the user input
for angle in user_input:
    draw_shape(angle)

# Keep the window open until closed by the user
turtle.done()
