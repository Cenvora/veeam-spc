from enum import Enum


class CloudTenantGatewaySelectionType(str, Enum):
    GATEWAYPOOL = "GatewayPool"
    STANDALONEGATEWAYS = "StandaloneGateways"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
