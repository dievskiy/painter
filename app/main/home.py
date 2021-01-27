from app.main import bp
from flask import render_template


@bp.route("/", methods=['GET'])
def home():
    return render_template('index.html')

