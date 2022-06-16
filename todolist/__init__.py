from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMT_DATABASE_URI'] = 'sqlite://site.db'

# this means that the database will be created in the current file system
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)  #database instances
from todolist import routes