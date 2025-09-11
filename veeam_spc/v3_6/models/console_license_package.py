from enum import Enum


class ConsoleLicensePackage(str, Enum):
    ADVANCED = "Advanced"
    BACKUP = "Backup"
    ESSENTIALS = "Essentials"
    FOUNDATION = "Foundation"
    NONE = "None"
    ONE = "ONE"
    ORCHESTRATOR = "Orchestrator"
    PREMIUM = "Premium"
    STARTER = "Starter"
    SUITE = "Suite"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
