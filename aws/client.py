from os import getenv
from aws.connection import Connection

AWS_ACCESS_KEY_ID = getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = getenv("AWS_SECRET_ACCESS_KEY")
REGION_NAME = getenv("REGION_NAME")


class Boto3:
    @classmethod
    def client(self, client_type: str):
        try:
            connection = Connection(
                client_type=client_type,
                acces_key_id=AWS_ACCESS_KEY_ID,
                secret_access_key=AWS_SECRET_ACCESS_KEY,
                region=REGION_NAME,
            )
            connection.connect()
            return connection.client
        except Exception as exception:
            raise Exception(exception)
