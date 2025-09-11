from enum import Enum


class UserLoginStatus(str, Enum):
    DISABLED = "disabled"
    DISABLEDDUESYSTEMCOMPONENTSRESTRICTIONS = "disabledDueSystemComponentsRestrictions"
    DISABLEDDUETOCOMPANY = "disabledDueToCompany"
    DISABLEDDUETOSYSTEM = "disabledDueToSystem"
    DISABLEDDUETOUSER = "disabledDueToUser"
    ENABLED = "enabled"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
