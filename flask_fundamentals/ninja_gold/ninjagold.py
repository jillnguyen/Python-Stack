from flask import Flask, render_template, session, request
import random

app = Flask(__name__)
app.secret_key = "MySecretIsAwesome"

@app.route('/')
def index():
    session['mygold'] = 0
    session['mylog'] = []
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def moneyflow():
    temp = request.form["action"]    
    if temp == "farm":
        val = random.randrange(10,20)
        myactivity = "Earn "+str(val)+" from the "+temp+""
        session['mylog'].append(myactivity)

    elif temp == "cave":
        val = random.randrange(5,10)
        myactivity = "Earn "+str(val)+" from the "+temp+""
        session['mylog'].append(myactivity)

    elif temp == "house":
        val = random.randrange(2,5)
        myactivity = "Earn "+str(val)+" from the "+temp+""
        session['mylog'].append(myactivity)

    elif temp == "casino":
        val = random.randrange(-50,50)
        if val > 0:
            color = "green"
            myactivity = "Entered the "+temp+" and earned "+str(val)+" gold"
            session['mylog'].append(myactivity)

        else:
            color = "red"
            myactivity = "Entered the "+temp+" and lost "+str(val)+" gold"
            session['mylog'].append(myactivity)
            
    session['mygold'] += val
    return render_template("index.html" , mygold = session['mygold'])

app.run(debug=True)