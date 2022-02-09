from flask import Flask, render_template, request 
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, DateField, IntegerField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

# This is a form, we have fields for first name, last name, and a submit button
class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    date_of_birth = DateField('Date of Birth')
    luckyNumber = IntegerField("Please enter your lucky number")
    food = StringField("Please enter your favourite food!")
    submit = SubmitField('Add Name')



#GET and POST methods, POST for once the submit is pressed. GET for getting that data. 
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    # Start off as an empty string 
    message = ""

    # Instantiating the form 
    form = BasicForm()

    # If the request method is a POST 
    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        date_of_birth = form.date_of_birth.data
        luckyNumber = form.luckyNumber.data 
        food = form.food.data

        # If someone has actually filled in this data. 
        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f'Thank you, {first_name} {last_name}'

        print(date_of_birth)
        print(luckyNumber)
        print(food)

        # Testing if date of birth is equal to None, try making it so that lucky number and food can all not be empty 
        if date_of_birth is None: 
            message = "Please supply your date of birth, lucky number and food"
        else: 
            message = f"Your username is {date_of_birth}{food}{luckyNumber}"

    # Return a render template for the home.html 
    # The message should display once form is submitted
    return render_template('home.html', form=form, message=message)

if __name__ == '__main__':
     app.run(debug=True)