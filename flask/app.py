from flask import Flask, render_template

app = Flask(__name__)


#  every function is connected to a route
#  we use the route to access the function
@app.route('/')
def hello_world():
    return 'the world is beautiful friend'

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/products')
def products():
    return  render_template('products.html')
@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/home')
def home():
    #we need to create an html page for this route in the templates folder
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

import pymysql
from flask import request
@app.route("/blog", methods=['POST', 'GET'])
def blog():
    # Logic goes here

    if request.method=='POST': #checks if user posted somethimg

        firstname = request.form['username']
        lastname = request.form['password']
        username = request.form['firstname']
        password = request.form['lastname']
        #c_word = request.form['confirm password']


        #save to the database
        #establish db connection

        con = pymysql.connect("localhost", "root", "", "registration")

        #execute SQL
        #create a cursor object, cursor executes SQL

        cursor = con.cursor()

        sql = "INSERT INTO `register_tbl`(`username`, `password`, `firstname`, `lastname`) VALUES (%s ,%s ,%s, %s)"

        cursor.execute(sql,(username,password, firstname, lastname))

        con.commit()

        return  render_template('blog.html')
    else:


        return  render_template('blog.html')
if __name__ == '__main__':  #confirms if the name called is the main application name
    app.run()
