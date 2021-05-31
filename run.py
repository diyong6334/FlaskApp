
from os import name
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

 
 
#create the object of Flask
app  = Flask(__name__)
app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root: '' @localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False
db = SQLAlchemy(app)

#creating Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    def __init__(self, name, email,phone):
        self.name = name
        self.email = email
        self.phone = phone 
 
#creating our routes
@app.route('/')
def index():
    return render_template('/index.html')

#creating our about routes
@app.route('/about')
def about():
    return render_template('/about.html')
 
#contact routes
@app.route('/contact')
def contact():
    return render_template('/contact.html')

#Galary routes
@app.route('/galary')
def galary():
    return render_template('/galary.html')

#product routes
@app.route('/product')
def product():
    return render_template('/product.html')

#service routes
@app.route('/services')
def services():
    return render_template('/services.html')

    #news routes
@app.route('/news')
def news():
    return render_template('/news.html')

 
#run flask app
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)