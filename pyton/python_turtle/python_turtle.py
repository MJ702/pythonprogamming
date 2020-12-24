from turtle import *

crazy_turtle = Turtle()

"""
    “fastest”: 0

    “fast”: 10

    “normal”: 6

    “slow”: 3

    “slowest”: 1
"""
crazy_turtle.speed('slow')
# Forward function is used turtle forward direction (pixel)
# crazy_turtle.forward(100)

# Right function is used turn the turtle (degrees clockwise)
# crazy_turtle.right(90)

# position function is display the current position of turtle
# print(crazy_turtle.position())


# backward function is used turtle move on back side
# print(crazy_turtle.position())
# crazy_turtle.backward(100)
# print(crazy_turtle.position())

# heading function is used to display the degrees of turtle
# print(crazy_turtle.heading())
# crazy_turtle.forward(90)
# crazy_turtle.right(15)
# print(crazy_turtle.heading())
# crazy_turtle.left(40)
# print(crazy_turtle.heading())

# .Pos function is used to display the position in from of x and y
# print(crazy_turtle.pos())
# .setpos(x, y)
# crazy_turtle.setpos(60, 30)
# print(crazy_turtle.pos())
# crazy_turtle.setpos(20, 80)
# print(crazy_turtle.pos())

# move forward in x
# crazy_turtle.setx(50)
# move forward in y
# crazy_turtle.sety(50)

# print(crazy_turtle.heading())
# print(crazy_turtle.heading())
# print(crazy_turtle.position())
# crazy_turtle.forward(100)
# print(crazy_turtle.position())
# Home function is used turtle return it origin
# crazy_turtle.home()

# .circle(radius, degree)
# for i in range(0, 100, 5):
# crazy_turtle.circle(i, 195)

# .dot(size of dot, color)
# crazy_turtle.dot(10, 'green')
# crazy_turtle.forward(60)

# stamp function is used to copy of turtle origin
# crazy_turtle.color("blue")
# astamp = crazy_turtle.stamp()
# crazy_turtle.forward(50)
# clearstamp is used to clear stamp
# print(crazy_turtle.clearstamp(astamp))

# for i in range(35):
    # crazy_turtle.stamp()
    # crazy_turtle.color('blue')
    # crazy_turtle.forward(60)
    # crazy_turtle.right(50)


# for i in range(4):
    # crazy_turtle.fd(50)
    # crazy_turtle.lt(80)
# undo function is used to undo draw a line
# for i in range(8):
    # crazy_turtle.undo()

# print(crazy_turtle.position())
# crazy_turtle.goto(180, 50)
# print(crazy_turtle.towards(0, 0))
# crazy_turtle.home()
# crazy_turtle.left(50)
# crazy_turtle.forward(100)
# print(crazy_turtle.position())
# Return the turtles x coordinate. after comma give digit value display digit
# print(round(crazy_turtle.xcor(), 5))
# print(round(crazy_turtle.ycor(), 5))

# crazy_turtle.home()
# turtle distance function like pithagors prime like we give input 30, 40
# print(crazy_turtle.distance(30,40))

# crazy_turtle.left(100)
# print(crazy_turtle.heading())
# crazy_turtle.degrees(360)
# print(crazy_turtle.heading())

"""
crazy_turtle.pen(fillcolor='green', pencolor='red', pensize=2)
for i in range(0, 11):
    crazy_turtle.left(45)
    crazy_turtle.circle(50, 180)
    crazy_turtle.forward(100)
    crazy_turtle.left(45)
"""

crazy_turtle.color('red','yellow')
begin_fill()
crazy_turtle.circle(150)
end_fill()





done()


