from enum import Enum


class PublicCloudFileShareType(str, Enum):
    AWSEFS = "AwsEfs"
    AWSFSX = "AwsFsx"
    AZUREFILES = "AzureFiles"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
