from enum import Enum


class LocalUserRuleType(str, Enum):
    WINNTGROUP = "winNTGroup"
    WINNTUSER = "winNTUser"

    def __str__(self) -> str:
        return str(self.value)
