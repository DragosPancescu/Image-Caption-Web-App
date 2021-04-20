from flask import Flask

ALLOWED_IMAGE_EXTENSION = ['jpg', 'png', 'jpeg']
MAXIMUM_MEMORY = 1024 * 1024 # As in bytes

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    # Views / Routing
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app