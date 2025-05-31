from turtle import *
from app.turtle.shapes import *
from time import sleep
from math import *
win = Screen()
win.bgcolor("white")
win.title("turtle_test")
turt = Turtle()
efface_dessin(win)
efface_dessin(win)
speed(2)
draw_flower(100, "red", 7)

win.mainloop()
 