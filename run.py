from __init__ import *

app.config.from_pyfile('database.py')
app.config.from_pyfile('login.py')

from login import *
from database import *
app.run(debug = True)
