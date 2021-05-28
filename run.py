
from flask import Flask, render_template
 
 
#create the object of Flask
app  = Flask(__name__)
 
#creating our routes
@app.route('/')
def index():
    return render_template('/index.html')

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
    app.run(debug=True)