from flask import *
import sys
from app.turtle.shapes import *
from app.turtle.convert import *
from turtle import *

app = Flask(__name__, template_folder='web/src', static_folder='web/static')

win = Screen()
win.setup(1000, 1000)
win.title("Turtle Shapes") # On retrouve le minima pour faire fonctionner le module turtle comme le screen, la tortue
hideturtle()
win.tracer(0)
turt = Turtle()
@app.route('/', methods=['GET', 'POST'])
def index():
    #Si la méthode est GET, on affiche le formulaire
    #Si la méthode est POST, on traite les données du formulaire
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        form_data = request.form.get('submit')
        message = ""
        conversion_ok = 0

        match form_data: # On récupère la valeur de la liste déroulante
            case "polygone":
                length = request.form.get('polygoneInput1', type=int, default=100)
                count = request.form.get('polygoneCount', type=int, default=8)
                color = request.form.get('polygoneColor', default='#000000')
                sides = request.form.get('polygoneSides', type=int, default=3)
                switch = 'polygoneCheckbox' in request.form
                if switch: # En fonction de si l'utilisateur a coché la case ou non, on dessine un polygone ou plusieurs polygones
                    angle = request.form.get('polygoneAngle', type=int, default=45)
                    penup() # On lève le stylo pour ne pas dessiner de ligne jusqu'à la position de départ
                    goto(0, 0) # On place la tortue au centre de l'écran pour dessiner les polygones
                    pendown() # On pose le stylo pour dessiner
                    draw_anything_multiples(length, color, count, angle, sides)
                else:
                    penup() # On lève le stylo pour ne pas dessiner de ligne jusqu'à la position de départ
                    goto(-200, 200) # On place la tortue au centre de l'écran pour dessiner les polygones
                    pendown() # On pose le stylo pour dessiner
                    draw_anything(length, color, sides)
                message = "polygones drawn"
            case "koch":
                
                length = request.form.get('kochInput1', type=int, default=100)
                depth = request.form.get('kochInput2', type=int, default=3)
                color = request.form.get('kochColor', default='#000000')
                switch = 'kochCheckbox' in request.form
                
                if switch: # En fonction de si l'utilisateur a coché la case ou non, on dessine une courbe de Koch ou plusieurs, ce qui permet de faire des flocons de neige
                    count = request.form.get('kochCount', type=int, default=6)
                    penup()
                    goto(-200, 200)
                    pendown()# On place la tortue en haut à gauche de l'écran pour dessiner les flocons de neige
                    draw_koch_flakes(length, color, depth, count)
                else:
                    draw_koch(length, color, depth)
                message = "Koch drawn"

            case "flower":
                length = request.form.get('flowerInput1', type=int, default=100)
                count = request.form.get('flowerCount', type=int, default=8)
                color = request.form.get('flowerColor', default='#000000')
                penup()
                goto(0, 0)
                pendown()
                switch = 'flowerCheckbox' in request.form
                if switch: # En fonction de si l'utilisateur a coché la case ou non, on dessine une pétale ou une fleur
                    draw_flower(length, color, count)
                else:
                    draw_petales(length, color)
                message = "Flower drawn"
            case _:
                message = "Invalid selection"
        hideturtle() # On cache la tortue pour ne pas qu'elle soit visible sur le dessin final
        win.update() # On met à jour la fenêtre pour afficher le dessin
        conversion_ok = convert_to_png(win)
        if conversion_ok == 1:
            return render_template('index.html', message=message)
        else:
            return render_template('index.html', message="Erreur lors de la conversion PNG")
@app.route('/output/<path:filename>') # Route pour les fichiers statiques tel que l'image PNG
def output_files(filename):
    return send_from_directory('web/output', filename)
    
if __name__ == "__main__": # Permet de lancer le serveur Flask en DEBUG lors de l'exécution du script
    if len(sys.argv) > 1:
        choice = sys.argv[1].upper()
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
    app.run(debug=choice, port=5000, threaded=False, host='0.0.0.0')