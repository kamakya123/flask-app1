#!/usr/bin/python3
from flask import *
from pymongo import MongoClient
app = Flask(__name__)
#connecting to the local host database:
client = MongoClient()

#if run.py was removed in any case then uncomment these and run the package itself
#app.config.from_pyfile('database.py')
#app.config.from_pyfile('login.py')
app.config.from_pyfile('run.py')
#from login import *
#from database import *
from run import *
#if __name__=="__main__":
    #app.run(debug = True)
