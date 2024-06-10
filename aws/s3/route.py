from flask_smorest import Blueprint
from aws.s3 import helper
from aws.s3.schema import S3BucketSchema

blueprint = Blueprint("s3", __name__)


@blueprint.route("/s3", methods=["GET"])
@blueprint.response(200, S3BucketSchema(many=True))
def get_s3_buckets():
    return helper.get_s3_buckets()


@blueprint.route("/s3/<name>", methods=["GET"])
@blueprint.response(200, S3BucketSchema)
def get_s3_bucket(name: str):
    return helper.get_s3_bucket(name)
