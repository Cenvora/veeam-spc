from enum import Enum


class PulseTenantMappingStatus(str, Enum):
    FAILEDTOMAP = "FailedToMap"
    MAPPED = "Mapped"
    MAPPINGINPROGGRESS = "MappingInProggress"
    NOTMAPPED = "NotMapped"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
