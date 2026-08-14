from enum import Enum


class PublicCloudAwsNewApplianceInputIpAddressApplianceIpNewIpAddressType(str, Enum):
    DYNAMIC = "dynamic"
    STATIC = "static"

    def __str__(self) -> str:
        return str(self.value)
