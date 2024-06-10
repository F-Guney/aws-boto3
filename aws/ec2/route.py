from flask_smorest import Blueprint

from aws.ec2 import helper
from aws.ec2.schema import EC2InstanceSchema

blueprint = Blueprint("ec2", __name__)


@blueprint.route("/ec2", methods=["GET"])
@blueprint.response(200, EC2InstanceSchema(many=True))
def get_ec2_instances():
    return helper.get_ec2_instances()


@blueprint.route("/ec2/<id>", methods=["GET"])
@blueprint.response(200, EC2InstanceSchema)
def get_ec2_instance(id: str):
    return helper.get_ec2_instance(id)
