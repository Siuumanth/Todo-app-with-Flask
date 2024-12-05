# for storing the api routes
# we create a container for our webpages related to the actual app
from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html")  # the browser will render this

