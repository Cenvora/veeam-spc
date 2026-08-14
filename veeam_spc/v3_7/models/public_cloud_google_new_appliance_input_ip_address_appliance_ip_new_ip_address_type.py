from enum import Enum


class PublicCloudGoogleNewApplianceInputIpAddressApplianceIpNewIpAddressType(str, Enum):
    DYNAMIC = "dynamic"
    STATIC = "static"

    def __str__(self) -> str:
        return str(self.value)
