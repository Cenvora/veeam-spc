from enum import Enum


class Vb365BackupProxyProxyType(str, Enum):
    DOMAIN = "Domain"
    LOCAL = "Local"
    UNKNOWN = "Unknown"
    WORKGROUP = "Workgroup"

    def __str__(self) -> str:
        return str(self.value)
