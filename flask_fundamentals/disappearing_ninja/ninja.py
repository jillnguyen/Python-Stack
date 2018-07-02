from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    link = "/static/tmnt.png"
    return render_template('ninja.html', link = link)

@app.route('/ninja/<color>')
def ninjacolor(color):
    link = "/static/"
    if color == "blue":
        link += "leonardo.jpg" 
    elif color == "red":
        link += "raphael.jpg"
    elif color == "orange":
        link += "michelangelo.jpg"
    elif color == "purple": 
        link += "donatello.jpg"
    else:
        link += "notapril.jpg"
    return render_template('ninja.html', link = link)

app.run(debug=True)




