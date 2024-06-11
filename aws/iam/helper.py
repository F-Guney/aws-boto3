from aws.client import Boto3
from aws.iam.model import IamUser


def get_iam_users():
    client = Boto3.client("iam")
    raw_users = client.list_users()

    users = [IamUser.of(user) for user in raw_users["Users"]]
    return users
