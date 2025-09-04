from enum import Enum


class PublicCloudNetworkTypeReadonly(str, Enum):
    AWSVPC = "AwsVpc"
    AZUREVNET = "AzureVnet"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
