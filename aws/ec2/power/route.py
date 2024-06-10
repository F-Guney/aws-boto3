from flask_smorest import Blueprint
from flask_smorest.response import Response

from aws.ec2.power import helper

blueprint = Blueprint("power", __name__)


@blueprint.route("/ec2/<id>/power/<option>", methods=["PUT"])
@blueprint.response(200)
def update_ec2_instance_power(id: str, option: str):
    helper.update_ec2_instance_power(id, option)
    return Response(status=200)
