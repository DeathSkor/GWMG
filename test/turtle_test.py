from turtle import *
from app.turtle.shapes import *
from time import sleep
from math import *
from sys import argv
from random import *

if __name__ == "__main__":
    if len(argv) > 1:
            choice = argv[1].upper()
            if choice == "DEBUG":
                print("Running in debug mode")
                choice = 1
            elif choice.isdigit():
                choice = int(choice)
                if choice == 1:
                    print("Running in debug mode")
                    choice = 1
                else:
                    print("Invalid argument, Add DEBUG or 1 to run in debug mode")
                    exit(1)
    else:
        choice = 0
win = Screen()
win.bgcolor("white")
win.title("turtle_test")
turt = Turtle()
while (1):
    print("1: Triangles\n2: Squares\n3: Koch flakes\n4: Flower\n0: exit")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            if (choice):
                efface_dessin(win)
                draw_multiple_triangles(100, "blue", 8, 45)
        case "2":
            if (choice):
                efface_dessin(win)
                draw_multiple_squares(100, "red", 8, 45) 
        case "3":
            if (choice):
                efface_dessin(win)
                draw_koch_flakes(100, "green", 4, 4)
        case "4":
            if (choice):
                efface_dessin(win)
                draw_flower(100, "purple", 45)
        case "0":
            print("Exiting...")
            break
done()
# This code is a test script for the turtle graphics module, allowing users to draw shapes interactively.
            
        