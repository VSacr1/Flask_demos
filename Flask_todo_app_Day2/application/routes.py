from application import app, db 
from application.models import Todos 
from flask import render_template 

#READ
# all_todos = all_todos is assigning what comes out of the database table to a variable so we can 
# later use this in our home.html in a for loop if needed. 
@app.route('/')
def index(): 
    all_todos = Todos.query.all()
    return render_template('home.html', all_todos=all_todos)

#CREATE
# latest_Todo is taking the latest item in the database (last primary key) then 
# if statement if it is the latest_Todo then add a new item to the table. Give it an id of id+1 
# Else if there is nothing in our database it will just make a new item auto assigning it id 1
@app.route('/add')
def add():
    latest_Todo = Todos.query.order_by(Todos.id.desc()).first()
    if latest_Todo:
        new_todo = Todos(task="Get Azure Access!" +str(latest_Todo.id+1))
    else: 
        new_todo = Todos(task="Teach Flask")
    db.session.add(new_todo)
    db.session.commit()
    return "Added new item to our list"

#UPDATE
# Looking at updating the complete boolean on a certain id
# Changes the completed field in table for this id to True 
@app.route('/complete/<int:id>')
def complete(id):
    # Getting our item from our database based on the id result from our routes
    todo = Todos.query.get(id)
    todo.completed = True 
    db.session.commit()
    return "Todo is now complete"

# Changes the completed field in the table for this id to False
@app.route('/incomplete/<int:id>')
def incomplete(id):
    todo = Todos.query.get(id)
    todo.completed = False
    db.session.commit()
    return "Todo is now incomplete"

# What ever goes into task is our updated task that then updates our latest result. 
# Same logic applied to our add task method
@app.route('/update/<task>')
def update(task):
    latest_todo = Todos.query.order_by(Todos.id.desc()).first()
    latest_todo.task = task 
    db.session.commit() 
    return "Updated most recent Todo"

# DELETE
# Grabbing latest one in the list
# Deleting it
@app.route('/delete')
def delete(): 
    latest_todo = Todos.query.order_by(Todos.id.desc()).first()
    db.session.delete(latest_todo)
    db.session.commit()
    return "Deleted most recent Todo"

