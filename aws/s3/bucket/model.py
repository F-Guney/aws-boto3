from dataclasses import dataclass
from datetime import datetime
from aws.s3.bucket.enum import S3BucketStorageClass


@dataclass
class S3BucketObject:
    key: str
    last_modified: datetime
    size: int
    storage_class: S3BucketStorageClass

    @staticmethod
    def of(value):
        return S3BucketObject(
            key=value["Key"],
            last_modified=value["LastModified"],
            size=value["Size"],
            storage_class=S3BucketStorageClass.of(value["StorageClass"]),
        )
