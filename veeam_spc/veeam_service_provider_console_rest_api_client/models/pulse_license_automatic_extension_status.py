from enum import Enum


class PulseLicenseAutomaticExtensionStatus(str, Enum):
    ALWAYSOFF = "AlwaysOff"
    ALWAYSON = "AlwaysOn"
    OFF = "Off"
    ON = "On"
    SWITCHINGTOOFF = "SwitchingToOff"
    SWITCHINGTOON = "SwitchingToOn"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
