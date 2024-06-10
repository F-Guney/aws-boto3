from flask_smorest import Blueprint
from aws.s3.bucket import helper
from aws.s3.bucket.schema import S3BucketObjectSchema

blueprint = Blueprint("bucket", __name__)


@blueprint.route("/s3/<name>/object", methods=["GET"])
@blueprint.response(200, S3BucketObjectSchema(many=True))
def get_s3_bucket_objects(name: str):
    return helper.get_s3_bucket_objects(name)
