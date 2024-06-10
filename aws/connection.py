import logging
import boto3

logger = logging.getLogger(__name__)


class Connection:
    def __init__(
        self, client_type: str, acces_key_id: str, secret_access_key: str, region: str
    ):
        self.client = None
        self.client_type = client_type
        self.access_key_id = acces_key_id
        self.secret_access_key = secret_access_key
        self.region = region

    def connect(self):
        try:
            self.client = boto3.client(
                self.client_type,
                aws_access_key_id=self.access_key_id,
                aws_secret_access_key=self.secret_access_key,
                region_name=self.region,
            )
            logger.debug(f"Connection for {self.client_type} service established")
        except Exception as exception:
            raise ConnectionError(exception)
