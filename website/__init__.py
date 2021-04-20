from flask import Flask

def create_app():
    app = Flask(__name__)
    # TODO: Research how to store a secret key
    app.config['SECRET_KEY'] = 'asdadad'

    # Views / Routing
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app