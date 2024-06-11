from aws.client import Boto3
from aws.iam.model import IamUser


def get_iam_users():
    client = Boto3.client("iam")
    raw_users = client.list_users()

    users = list(map(IamUser.of, raw_users["Users"]))
    return users


def get_iam_user(name: str):
    client = Boto3.client("iam")
    raw_user = client.get_user(UserName=name)

    return IamUser.of(raw_user["User"])
