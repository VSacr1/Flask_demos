from flask import Flask 
# Database connector, Object relational Mapper
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30), nullable=False)
    complete = db.Column(db.Boolean, default=False)

db.drop_all()
db.create_all()

# Creating task for our table. 
# Test that a table can accept the entry and there is nothing wrong with code. 
sample_task = Todos(
    task = "Teaching Flask! Testing the drop all command",
    complete = False
)

# Adding the task to the table. 
db.session.add(sample_task)
db.session.commit()

@app.route('/')
def index(): 
    todo = Todos.query.first()
    return todo.task

@app.route('/add')
def add():
    return "Add a new task!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')