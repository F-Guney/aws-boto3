from marshmallow import Schema, fields


class S3BucketSchema(Schema):
    name = fields.String()
    creation_date = fields.DateTime()
    owner_name = fields.String()
    owner_id = fields.String()
