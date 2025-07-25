from turtle import *
from time import sleep
from math import *
def efface_dessin(win):
    """
    Efface le dessin en cours
    """
    sleep(1)
    win.clear()
    reset()
    speed(0)
def draw_triangle(length, color):
    """
    Dessine un triangle équilatéral, longueur = length, couleur = color
    """
    end_fill()
    pencolor(color)
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
    end_fill()
    pencolor(color)
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
    pencolor(color)
    fillcolor(color)
    if depth == 0:
        forward(length)
    else:
        # Divise la longueur par 3 pour chaque segment
        
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
    penup()
    pendown()
    for _ in range(count):
        draw_koch(length, color, depth)
        right(360 / count)
    penup()
    goto(0, 0)
    pendown()

def draw_petales(length, color):
    """
    Dessine un pétale, longueur = length, couleur = color
    """
    pencolor(color)
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
def draw_anything(lenght, color, sides):
    """
    Fonction qui permet de dessiner n'importe quel polygone grâce au flocon de Koch
    """
    draw_koch_flakes(lenght, color, 0, sides)
def draw_anything_multiples(lenght, color, count, angle, sides):
    """
    Fonction qui permet de dessiner n'importe quel polygone grâce au flocon de Koch
    """
    for _ in range(count):
        draw_anything(lenght, color, sides)
        left(angle)

    
