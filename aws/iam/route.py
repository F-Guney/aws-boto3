from flask_smorest import Blueprint
from aws.iam import helper
from aws.iam.schema import IamUserSchema

blueprint = Blueprint("iam", __name__)


@blueprint.route("/iam", methods=["GET"])
@blueprint.response(200, IamUserSchema(many=True))
def get_iam_users():
    return helper.get_iam_users()


@blueprint.route("/iam/<name>", methods=["GET"])
@blueprint.response(200, IamUserSchema)
def get_iam_users(name: str):
    return helper.get_iam_user(name)
