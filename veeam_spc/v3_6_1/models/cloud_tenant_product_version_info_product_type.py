from enum import Enum


class CloudTenantProductVersionInfoProductType(str, Enum):
    UNKNOWN = "Unknown"
    VBR = "VBR"

    def __str__(self) -> str:
        return str(self.value)
