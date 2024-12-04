from flask import Flask

#initialized flask application
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']  =  'somerandomstuff' #encrypts our cookie and session data
     
    # we need to register the following webpages in our app
    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')   # no prefix rn

    
    return app




# in the default app , we do app.route and stuff, but now we can do views.route, auth.route since we have registered the stuff

# if we had added a prefix for example /auth, then to access all the webpages contained in auth, we will need to use /auth/webpage, but since we have no prefix we can just do /webpage.,,