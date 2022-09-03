from flask import Flask as f, render_template,request, flash

app = f(__name__)

app.secret_key="mojic"
@app.route("/")
def home():
    flash('Enter number?')
    return render_template("index.html")
@app.route('/greet', methods=['POST','GET'])
def greet():
    if "5" in str(request.form['phoneNumber']):
        flash('This ' + str(request.form['phoneNumber']) + " is special ")
    elif "2" in str(request.form['phoneNumber']):
        flash('This ' + str(request.form['phoneNumber']) + " is special ")
    elif "6" in str(request.form['phoneNumber']):
        flash('This ' + str(request.form['phoneNumber']) + " is special ")
    else:
        flash('Sorry ' + str(request.form['phoneNumber'])+ " is a normal number")
    return render_template("index.html")
    

