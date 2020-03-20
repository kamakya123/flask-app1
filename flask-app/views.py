from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def Home():
    return "hello wolcome to home page"
