from aws.client import Boto3
from aws.ec2.model import EC2Instance


def get_ec2_instances():
    client = Boto3.client("ec2")
    raw_instances = client.describe_instances()

    instances = [
        EC2Instance.of(instance)
        for reservation in raw_instances["Reservations"]
        for instance in reservation["Instances"]
    ]

    return instances


def get_ec2_instance(id: str):
    client = Boto3.client("ec2")
    raw_instances = client.describe_instances(InstanceIds=[id])

    instance = next(
        (
            EC2Instance.of(instance)
            for reservation in raw_instances["Reservations"]
            for instance in reservation["Instances"]
        ),
        None,
    )

    return instance
