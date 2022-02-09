from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/exercise')
def exercise():
    return render_template('index.html', users=["ben", "harry", "bob", "jay", "matt", "bill"])

#What we put on ben.html is what is getting returned in this function
@app.route('/ben')
def ben(): 
    return render_template('ben.html')

# What we put on harry.html is what is getting returned in this function
@app.route('/harry')
def harry(): 
    return render_template('harry.html')

if __name__ == "__main__":
    app.run(debug=True)