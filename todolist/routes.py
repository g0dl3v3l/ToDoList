from flask import render_template, url_for, flash, redirect, request
from todolist import app 


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/" , methods =['POST', 'GET'])
def value():
    task = request.form.get('task')
    return render_template('index.html' , value = task)






