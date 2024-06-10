from aws.client import Boto3


def update_ec2_instance_power(id: str, option: str):
    client = Boto3.client("ec2")

    ec2_operations = {
        "start": {
            "action": client.start_instances,
            "waiter": client.get_waiter("instance_running"),
        },
        "stop": {
            "action": client.stop_instances,
            "waiter": client.get_waiter("instance_stopped"),
        },
        "reboot": {
            "action": client.reboot_instances,
            "waiter": client.get_waiter("instance_status_ok"),
        },
        "terminate": {
            "action": client.terminate_instances,
            "waiter": client.get_waiter("instance_terminated"),
        },
    }

    ec2_operations[option]["action"](InstanceIds=[id])
    ec2_operations[option]["waiter"].wait(InstanceIds=[id])
