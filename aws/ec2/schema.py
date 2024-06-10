from marshmallow import Schema, fields
from aws.ec2.enum import EC2InstanceType, EC2InstanceState


class EC2InstanceSchema(Schema):
    id = fields.String()
    name = fields.String()
    image_id = fields.String()
    instance_type = fields.Enum(EC2InstanceType)
    launch_time = fields.DateTime()
    state = fields.Enum(EC2InstanceState)
    platform_details = fields.String()
