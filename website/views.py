# for storing the api routes
# we create a container for our webpages related to the actual app
from flask import Blueprint

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return '<h1>Welcome<h1>'  # the browser will render this

