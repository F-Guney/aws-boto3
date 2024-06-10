from marshmallow import Schema, fields
from aws.s3.bucket.enum import S3BucketStorageClass


class S3BucketObjectSchema(Schema):
    key = fields.String()
    last_modified = fields.DateTime()
    size = fields.Integer()
    storage_class = fields.Enum(S3BucketStorageClass)
