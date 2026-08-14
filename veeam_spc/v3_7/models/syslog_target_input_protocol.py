from enum import Enum


class SyslogTargetInputProtocol(str, Enum):
    TCP = "Tcp"
    UDP = "Udp"

    def __str__(self) -> str:
        return str(self.value)
