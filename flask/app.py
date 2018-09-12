from flask import Flask, render_template

app = Flask(__name__)


#  every function is connected to a route
#  we use the route to access the function
@app.route('/')
def hello_world():
    return 'the world is beautiful friend'

@app.route('/lee')
def waddup_lee():
    return 'say hey to me and you'

@app.route('/login')
def login():
    return 'welcome to my login'

@app.route('/order')
def order():
    return 'place your order'

@app.route('/home')
def home():
    #we need to create an html page for this route in the templates folder
    return render_template('home.html')
if __name__ == '__main__':  #confirms if the name called is the main application name
    app.run()
