from enum import Enum


class JobSessionHeatmapWorkloadType(str, Enum):
    CLOUDDATABASE = "CloudDatabase"
    CLOUDFILESHARE = "CloudFileShare"
    CLOUDNETWORK = "CloudNetwork"
    CLOUDVM = "CloudVM"
    COMPUTER = "Computer"
    FILE = "File"
    FILESHARE = "FileShare"
    LOGS = "Logs"
    OBJECTSTORAGE = "ObjectStorage"
    UNKNOWN = "Unknown"
    USER = "User"
    VM = "Vm"

    def __str__(self) -> str:
        return str(self.value)
