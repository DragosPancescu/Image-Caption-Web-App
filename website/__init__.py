from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    # TODO: Research how to store a secret key
    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    # Views / Routing
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app