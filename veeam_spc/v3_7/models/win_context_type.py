from enum import Enum


class WinContextType(str, Enum):
    APPLICATIONDIRECTORY = "applicationDirectory"
    DOMAIN = "domain"
    MACHINE = "machine"

    def __str__(self) -> str:
        return str(self.value)
