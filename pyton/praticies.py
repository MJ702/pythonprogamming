from turtle import *
from random import *


print('hellow every one')
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()

turtles_1 = [t1, t2, t3, t4, t5]
wn = Turtle.getscreen(t1)
wn.bgcolor('#d2f7ce')

x = -100

for i in turtles_1:
    i.speed(0)
    i.left(90)
    i.color("brown")
    i.penup()
    x += randint(80, 160)
    i.goto(x, randint(-100, 150))
    i.pendown()


def branch_tree(turt, branch_len):
    angle = randint(25, 35)
    sf = uniform(0.6, 0.8)
    size = int(branch_len / 10)
    turt.pensize(size)
    if branch_len < 20:
        turt.color('green')
        turt.stamp()
        turt.color('brown')
    if branch_len > 10:
        turt.forward(branch_len * sf)
        turt.left(angle)
        branch_tree(turt, branch_len * sf)
        turt.right(2 * angle)
        branch_tree(turt, branch_len * sf)
        turt.left(angle)
        turt.backward(branch_len * sf)


for i in turtles_1:
    branch_tree(i, 100)

done()
