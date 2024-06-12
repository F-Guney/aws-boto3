from dataclasses import dataclass
from datetime import datetime


@dataclass
class IamUserTags:
    key: str
    value: str

    @staticmethod
    def of(value):
        return IamUserTags(
            key=value["Key"],
            value=value["Value"],
        )


@dataclass
class IamUser:
    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime

    @staticmethod
    def of(value):
        return IamUser(
            path=value["Path"],
            user_name=value["UserName"],
            user_id=value["UserId"],
            arn=value["Arn"],
            create_date=value["CreateDate"],
            password_last_used=value["PasswordLastUsed"],
        )
