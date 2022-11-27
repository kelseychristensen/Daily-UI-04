from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import math

app = Flask(__name__)
Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        display_calc = True
        room_size = request.values.get("room")
        box_size = request.values.get("box")
        cost = request.values.get("cost")
        num_needed = int(math.ceil(float(room_size)/float(box_size)))
        calced_cost = float(float(num_needed)*float(cost))
        if calced_cost % .5 == 0:
            new_calc = f"{float(float(num_needed)*float(cost))}0"
        else:
            new_calc = round(float(float(num_needed)*float(cost)), 2)
        return render_template("index.html", display_calc=display_calc, num_needed=num_needed, calced_cost=new_calc)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)