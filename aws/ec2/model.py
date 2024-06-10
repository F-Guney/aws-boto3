from dataclasses import dataclass
from datetime import datetime
from aws.ec2.enum import EC2InstanceState, EC2InstanceType


@dataclass
class EC2Instance:
    id: str
    image_id: str
    launch_time: datetime
    name: str
    platform_details: str
    state: EC2InstanceState
    instance_type: EC2InstanceType

    @staticmethod
    def of(value):
        state = value["State"]
        tags = value["Tags"]

        name = next((tag["Value"] for tag in tags if tag["Key"] == "Name"), None)

        return EC2Instance(
            id=value["InstanceId"],
            image_id=value["ImageId"],
            launch_time=value["LaunchTime"],
            name=name,
            platform_details=value["PlatformDetails"],
            state=EC2InstanceState.of(state["Name"]),
            instance_type=EC2InstanceType.of(value["InstanceType"]),
        )
