from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")



@app.route('/projects')
def my_projects():
    return render_template("project.html")


@app.route('/about')
def about():
    return render_template("about.html")
    
app.run(debug = True) 