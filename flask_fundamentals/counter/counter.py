from flask import Flask, render_template, session

app = Flask(__name__)

app.secret_key = "It is session lecture"

@app.route('/')
def index():
    if not 'counter' in session:
        session['counter'] = 0
    else:
        session['counter'] += 1              
    return render_template("index.html", counter = session['counter'])    

@app.route('/2')
def mouseclk():
    if not 'counter' in session:
        session['counter'] = 0
    else:
        session['counter'] += 2      
    return render_template("index.html", counter = session['counter']) 

@app.route('/3')
def reset():
    
    if 'counter' in session:
        del session['counter']
    return render_template("index.html", counter = 0)

app.run(debug=True)
    
    