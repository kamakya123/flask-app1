from __init__ import *
#creating the the database:
mydb = client["sharma"]

#creating the collections
users = mydb["kamakya"]
app.config.from_pyfile('login.py')
from login import *

