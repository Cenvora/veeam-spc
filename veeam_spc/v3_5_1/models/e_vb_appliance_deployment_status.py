from enum import Enum


class EVbApplianceDeploymentStatus(str, Enum):
    CONNECTING = "Connecting"
    FAILED = "Failed"
    INSTALLING = "Installing"
    SERVICEACCOUNTCREATING = "ServiceAccountCreating"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    UPDATECREDENTIALS = "UpdateCredentials"
    UPGRADING = "Upgrading"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
