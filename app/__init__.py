from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    return app
