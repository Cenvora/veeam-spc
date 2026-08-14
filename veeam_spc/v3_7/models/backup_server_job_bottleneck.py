from enum import Enum


class BackupServerJobBottleneck(str, Enum):
    NETWORK = "Network"
    NONE = "None"
    PROXY = "Proxy"
    SOURCE = "Source"
    SOURCEWANACCELERATOR = "SourceWanAccelerator"
    TARGET = "Target"
    TARGETWANACCELERATOR = "TargetWanAccelerator"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
