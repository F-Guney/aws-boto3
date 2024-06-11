from marshmallow import Schema, fields


class IamUserSchema(Schema):
    path = fields.String()
    user_name = fields.String()
    user_id = fields.String()
    arn = fields.String()
    create_date = fields.DateTime()
    password_last_used = fields.DateTime()
