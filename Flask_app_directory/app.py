from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route('/home')
def hello_internet(): 
    return render_template('account.html', title='My Account')

@app.route('/about')
def about_page(): 
    return redirect(url_for('hello_internet'))

@app.route('/home/<word>')
def home(word): 
    return word.upper()

@app.route('/home/<int:number>')
def number_example(number):
    answer = number * number 
    return str(answer)

if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=5000)