from dataclasses import dataclass
from datetime import datetime


@dataclass
class S3Bucket:
    name: str
    creation_date: datetime
    owner_name: str
    owner_id: str

    @staticmethod
    def of(value, owner):
        return S3Bucket(
            name=value["Name"],
            creation_date=value["CreationDate"],
            owner_name=owner["DisplayName"],
            owner_id=owner["ID"],
        )
