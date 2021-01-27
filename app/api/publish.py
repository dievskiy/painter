from app.api import bp
from app.api import aws_controller
from flask import abort, request
import uuid
import os

bucket_name = os.environ['BUCKET_NAME']


@bp.route("/publish", methods=["POST"])
def publish_image():
    if not request.json:
        abort(400)
    if 'data' not in request.json:
        abort(400)

    img_base64 = request.json['data']
    img_base64 = img_base64.replace("data:image/png;base64,", "")

    file_name = str(uuid.uuid4()) + '.png'
    aws_controller.save_to_bucket(img_base64, file_name)

    return {"status": "ok",
            "_link": f"https://{bucket_name}.s3.eu-central-1.amazonaws.com/{file_name}"}, 201
