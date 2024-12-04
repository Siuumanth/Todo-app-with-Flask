# we create a container for our webpages related to the auth

from flask import Blueprint

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return "<p>login<p>"

@auth.route('/logout')
def logout():
    return "<p>logout<p>"

@auth.route('/signup')
def sign_up():
    return "<p>Sign Up<p>"