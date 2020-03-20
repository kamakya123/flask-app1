from flask import Blueprint 
main = Blueprint('login',__name__)

@main.route('/login')
def login():
    return 'you are logged in successfully'

