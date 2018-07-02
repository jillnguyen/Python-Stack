from flask import Flask, render_template, request, flash

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    if len(name) < 1 or len(comment) < 1:
        flash("The form requires both name and comment to be filled out")
    elif len(comment) > 120:
        flash("Comment should be less than 120 characters")
    else:
        flash("SUCCESS! Information is shown")                
    print (name, location, language, comment)
    return redirect("/", name = name, location = location, language = language, comment = comment)

app.run(debug=True)