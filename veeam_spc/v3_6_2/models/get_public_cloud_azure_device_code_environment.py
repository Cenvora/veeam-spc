from enum import Enum


class GetPublicCloudAzureDeviceCodeEnvironment(str, Enum):
    CHINA = "China"
    GERMANY = "Germany"
    GLOBAL = "Global"
    USGOVERNMENT = "UsGovernment"

    def __str__(self) -> str:
        return str(self.value)
