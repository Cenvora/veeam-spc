from enum import Enum


class DiscoveryRuleFilterPlatformsItem(str, Enum):
    AMAZONWEBSERVICES = "AmazonWebServices"
    GOOGLECLOUD = "GoogleCloud"
    MICROSOFTAZURE = "MicrosoftAzure"
    MICROSOFTHYPERVANDVMWAREVSPHERE = "MicrosoftHyperVandVmWareVSphere"
    OTHER = "Other"
    PHYSICAL = "Physical"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
