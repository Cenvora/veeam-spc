from enum import Enum


class ActiveAlarmArea(str, Enum):
    VONE = "vone"
    VSPC = "vspc"

    def __str__(self) -> str:
        return str(self.value)
