from turtle import *
from app.turtle.shapes import *
from PIL import Image
import os
def convert_to_png(win):
    hideturtle()
    cv = win.getcanvas()
    # On récupère un fichier PostScript depuis la librairie turtle pour ensuite
    # le convertir en PNG avec PIL
    cv.postscript(file='app/turtle/ps/files.eps', width=1000, height=1000)
    if os.path.exists('app/web/output/result.png'): # On supprime l'ancienne image si elle existe
        os.remove('app/web/output/result.png')
        print("deleted previous result.png")
        img = Image.open('app/turtle/ps/files.eps')
        img.save('app/web/output/result.png', 'png') # Conversion en PNG dans /app/web/output
        img.close() #On ferme l'image pour laisser les autres processus l'utiliser
        print(f"Screenshot saved as result.png")
    else:
        print("No previous result.png to delete")
        img = Image.open('app/turtle/ps/files.eps')
        img.save('app/web/output/result.png', 'png')
        img.close()
        print(f"Screenshot saved as result.png")
    efface_dessin(win) # On efface le dessin actuel
    return 1