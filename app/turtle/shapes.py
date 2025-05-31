from turtle import *
from time import sleep
from math import *

def draw_triangle(length, color):
    """
    Dessine un triangle équilatéral, longueur = length, couleur = color
    """
    fillcolor(color)
    begin_fill()
    for _ in range(3):
        forward(length)
        left(120)
    end_fill()
def draw_multiple_triangles(length, color, count, angle):
    """
    Dessine plusieurs triangles équilatéraux, longueur = length, couleur = color, nombre = count
    """
    for _ in range(count):
        draw_triangle(length, color)
        left(angle)
    end_fill()
def draw_square(length, color):
    """
    Dessine un carré, longueur = length, couleur = color
    """
    fillcolor(color)
    begin_fill()
    for _ in range(4):
        forward(length)
        left(90)
    end_fill()
def draw_multiple_squares(length, color, count, angle):
    """
    Dessine plusieurs carrés, longueur = length, couleur = color, nombre = count
    """
    for _ in range(count):
        draw_square(length, color)
        left(angle)
    end_fill()
def draw_koch(length, color, depth):
    """
    Dessine une courbe de Koch, longueur = length, couleur = color, profondeur = depth
    """
    fillcolor(color)
    if depth == 0:
        forward(length)
    else:
        length /= 3.0
        draw_koch(length, color, depth - 1)
        left(60)
        draw_koch(length, color, depth - 1)
        right(120)
        draw_koch(length, color, depth - 1)
        left(60)
        draw_koch(length, color, depth - 1)
    
def draw_koch_flakes(length, color, depth, count):
    """
    Dessine des flocons de neige de Koch, longueur = length, couleur = color, profondeur = depth, nombre = count
    """
    for _ in range(count):
        draw_koch(length, color, depth)
        right(360 / count)
def efface_dessin(win):
    """
    Efface le dessin en cours
    """
    sleep(1)
    win.clear()
    speed(0)
def draw_petales(length, color):
    """
    Dessine un pétale, longueur = length, couleur = color
    """
    fillcolor(color)
    circle(length, 60)
    left(120)
    circle(length, 60)
    left(120)
def draw_flower(length, color, count):
    """
    Dessine une fleur avec des pétales, longueur = length, couleur = color, nombre de pétales = count
    """
    for _ in range(count):
        draw_petales(length, color)
        left(360 / count)
    end_fill()
