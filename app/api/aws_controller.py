import base64
import boto3

s3 = boto3.resource('s3')
bucket_name = 'open-paint'


def save_to_bucket(image: str, file_name) -> None:
    """
    Saves base64 encoded picture as png to bucket on aws s3
    :param image: base64-encoded picture
    :return:
    """
    obj = s3.Object(bucket_name, file_name)
    obj.put(Body=base64.b64decode(image))
    return
