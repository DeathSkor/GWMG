from turtle import *
from app.turtle.shapes import *
from PIL import Image
import os
def convert_to_png(win):
    hideturtle()
    cv = win.getcanvas()
    cv.postscript(file='app/turtle/ps/files.eps', width=1000, height=1000)
    if os.path.exists('app/web/output/result.png'):
        os.remove('app/web/output/result.png')
        print("deleted previous result.png")
        img = Image.open('app/turtle/ps/files.eps')
        img.save('app/web/output/result.png', 'png')
        img.close()
        print(f"Screenshot saved as result.png")
    else:
        print("No previous result.png to delete")
        img = Image.open('app/turtle/ps/files.eps')
        img.save('app/web/output/result.png', 'png')
        img.close()
        print(f"Screenshot saved as result.png")
    efface_dessin(win)
    return 1