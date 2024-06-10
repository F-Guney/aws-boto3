from aws.client import Boto3
from aws.s3.model import S3Bucket


def get_s3_buckets():
    client = Boto3.client("s3")
    buckets = client.list_buckets()

    buckets = [S3Bucket.of(bucket, buckets["Owner"]) for bucket in buckets["Buckets"]]
    return buckets


def get_s3_bucket(name: str):
    client = Boto3.client("s3")
    buckets = client.list_buckets()

    bucket = next(
        (
            S3Bucket.of(bucket, buckets["Owner"])
            for bucket in buckets["Buckets"]
            if name == bucket["Name"]
        ),
        None,
    )
    return bucket
