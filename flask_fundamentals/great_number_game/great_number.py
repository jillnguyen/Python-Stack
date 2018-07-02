from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key="MySecretIsSafe"

@app.route('/')
def index():
    session['mykey'] = random.randrange(0,100)
    session['win'] = False
    return render_template('index.html')

@app.route('/1', methods =["POST"])
def comparison():
    session['input'] = int(request.form['input'])
    if session['input'] == session['mykey']:
        session['win'] = True
        return render_template('index.html', relative = session['relative'], mykey = session ['mykey'], input = session['input'])
    elif session['input'] > session['mykey']:
        session['relative'] = 'high'
        return render_template('index.html', relative = session['relative'], mykey = session ['mykey'], input = session['input'])
    else:
        session['relative'] = 'low'
        return render_template('index.html', relative = session['relative'], mykey = session ['mykey'], input = session['input'])

@app.route('/2')
def win():
    session.pop('input')
    return render_template("index.html")
    
app.run(debug=True)





