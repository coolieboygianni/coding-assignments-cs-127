#Name: Gianni Russell
#gianni.russell07@myhunter.cuny.edu
#Date: November 10, 2023
import turtle

def triangle(t, length):
    if length > 10:
        for _ in range(3):
            t.forward(length)
            t.left(120)
        triangle(t, length/2)

def nestedTriangle(t, length):
    if length > 10:
        for _ in range(3):
            t.forward(length)
            t.left(120)
        nestedTriangle(t, length/2)

def main():
    length = int(input("Enter edge length: "))
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-length/2, length/2*3**0.5/2)
    t.pendown()
    t.pen(pencolor="red", pensize=2)
    triangle(t, length)
    t.penup()
    t.goto(-length/2, -length/2*3**0.5/2)
    t.pendown()
    t.pen(pencolor="blue", pensize=2)
    nestedTriangle(t, length)
    turtle.done()

if __name__ == "__main__":
    main()