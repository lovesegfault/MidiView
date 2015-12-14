from turtle import *
from random import randint, uniform
import pygame.midi


def random_move(turtle, distance):
    """turn turtle through random angle and move forward by random distance"""
    while True:
        if i.poll():
            midi_in = i.read(20)
            print(midi_in[0][0][2])
            angle = uniform(-90, 90)
            d = uniform(0, midi_in[0][0][2]/10)
            turtle.left(angle)
            turtle.forward(d)
            break
        else:
            continue


def randcolor():
    """return random color --- a 3-tupe"""
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def gohome(turtle):
    """send turtle home without leaving a track."""
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()


def random_walk(turtle, distance, steps):
    """Send turtle on random walk."""
    turtle.color(randcolor(), randcolor())
    turtle.pensize(10)
    for step in range(0, steps):
        random_move(turtle, distance)
    gohome(turtle)


def repeat(steps, trials):
    """Repeat random_walk."""
    for trial in range(0, trials):
        random_walk(fred, 5, steps)


def saveImage(turtle, filename):
    """Save drawing to eps file."""
    ts = turtle.getscreen()
    tc = ts.getcanvas()
    tc.postscript(file=filename)
pygame.midi.init()
input_id = 3
i = pygame.midi.Input(input_id)

fred = Turtle()
fred.speed("fastest")
colormode(255)

fred.dot(10, "black")
repeat(2000, 20)

saveImage(fred, "fred1234.eps")
exitonclick()
