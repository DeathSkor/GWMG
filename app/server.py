from flask import *
import sys
from app.turtle.shapes import *
from app.turtle.convert import *
from turtle import *

app = Flask(__name__, template_folder='web/src', static_folder='web/static')

win = Screen()
win.screensize(1000, 1000)
win.title("Turtle Shapes")
hideturtle()
win.tracer(0)
turt = Turtle()
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        form_data = request.form.get('submit')
        message = ""
        conversion_ok = 0

        match form_data:
            case "triangle":
                length = request.form.get('triangleInput1', type=int, default=100)
                count = request.form.get('triangleCount', type=int, default=8)
                color = request.form.get('triangleColor', default="#000000")
                switch = 'triangleCheckbox' in request.form
                if switch:
                    angle = request.form.get('triangleAngle', type=int, default=45)
                    draw_multiple_triangles(length, color, count, angle)
                else:
                    draw_triangle(length, color)
                message = "Triangles drawn"
            case "square":
                length = request.form.get('squareInput1', type=int, default=100)
                count = request.form.get('squareCount', type=int, default=8)
                color = request.form.get('squareColor', default='#000000')
                switch = 'squareCheckbox' in request.form
                if switch:
                    angle = request.form.get('squareAngle', type=int, default=45)
                    draw_multiple_squares(length, color, count, angle)
                else:
                    draw_square(length, color)
                message = "Squares drawn"
            case "koch":
                length = request.form.get('kochInput1', type=int, default=100)
                depth = request.form.get('kochInput2', type=int, default=3)
                color = request.form.get('kochColor', default='#000000')
                switch = 'kochCheckbox' in request.form
                if switch:
                    count = request.form.get('kochCount', type=int, default=6)
                    draw_koch_flakes(length, color, depth, count)
                else:
                    draw_koch(length, color, depth)
                message = "Koch drawn"
            case "flower":
                length = request.form.get('flowerInput1', type=int, default=100)
                count = request.form.get('flowerCount', type=int, default=8)
                color = request.form.get('flowerColor', default='#000000')
                switch = 'flowerCheckbox' in request.form
                if switch:
                    draw_flower(length, color, count)
                else:
                    draw_petales(length, color)
                message = "Flower drawn"
            case _:
                message = "Invalid selection"
        hideturtle()
        conversion_ok = convert_to_png(win)
        if conversion_ok == 1:
            return render_template('index.html', message=message)
        else:
            return render_template('index.html', message="Erreur lors de la conversion PNG")
@app.route('/output/<path:filename>')
def output_files(filename):
    return send_from_directory('web/output', filename)
    
if __name__ == "__main__":
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