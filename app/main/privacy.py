from app.main import bp
from flask import render_template


@bp.route("/privacy", methods=['GET'])
def privacy():
    return render_template('privacy.html')
