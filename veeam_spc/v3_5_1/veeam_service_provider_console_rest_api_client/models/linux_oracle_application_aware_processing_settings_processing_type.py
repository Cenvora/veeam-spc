from enum import Enum


class LinuxOracleApplicationAwareProcessingSettingsProcessingType(str, Enum):
    DISABLEPROCESS = "DisableProcess"
    REQUIRESUCCESS = "RequireSuccess"
    TRYPROCESS = "TryProcess"

    def __str__(self) -> str:
        return str(self.value)
