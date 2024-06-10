from aws.client import Boto3
from aws.s3.bucket.model import S3BucketObject


def get_s3_bucket_objects(bucket):
    client = Boto3.client("s3")
    raw_objects = client.list_objects_v2(Bucket=bucket)

    objects = [
        S3BucketObject.of(bucket_object) for bucket_object in raw_objects["Contents"]
    ]
    return objects
