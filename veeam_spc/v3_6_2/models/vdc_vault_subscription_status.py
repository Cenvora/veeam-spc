from enum import Enum


class VdcVaultSubscriptionStatus(str, Enum):
    ACTIVE = "Active"
    SUSPENDED = "Suspended"
    TERMINATED = "Terminated"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
