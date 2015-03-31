#!usr/bin/env python

import turtle
import random

def main():
    tList = []
    head = 0
    numTurtles = 10
    for i in range(numTurtles):
        nt = turtle.Turtle()  # Make a new turtle, initialize values
        nt.setheading(head)
        nt.pensize(2)
        #nt.color(random.randrange(256), random.randrange(256), random.randrange(256))
        nt.speed(10)
        nt.tracer(30,0)
        tList.append(nt)  # Add the new turtle to the list
        head = head + 360/numTurtles

    for i in range(100):
        moveTurtles(tList, 15, i)

    w = tList[0]
    w.up()
    w.goto(-130, 40)
    #w.write("Happy Birthday !", True, "center", "30px Arial")
    w.goto(-130, -35)
    #w.write("Zhang", True, "center", "30px Arial")

def moveTurtles(turtleList, dist, angle):
    for turtle in turtleList: # Make every turtle on the list do the same action
        turtle.forward(dist)
        turtle.right(angle)

main()


