from enum import Enum


class ComputerInfoGuestOsType(str, Enum):
    DOMAINCONTROLLER = "DomainController"
    LINUX = "Linux"
    MAC = "Mac"
    SERVER = "Server"
    UNKNOWN = "Unknown"
    WORKSTATION = "Workstation"

    def __str__(self) -> str:
        return str(self.value)
