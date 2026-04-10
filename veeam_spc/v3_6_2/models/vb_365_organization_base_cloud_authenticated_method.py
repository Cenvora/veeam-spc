from enum import Enum


class Vb365OrganizationBaseCloudAuthenticatedMethod(str, Enum):
    BASIC = "Basic"
    MODERN = "Modern"
    MODERNWITHLEGACYPROTOCOLS = "ModernWithLegacyProtocols"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
