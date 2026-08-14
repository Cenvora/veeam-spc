from enum import Enum


class GetBackupServerDeploymentConfigurationXmlBackupServerDeploymentType(str, Enum):
    INSTALLATION = "installation"
    UPGRADE = "upgrade"

    def __str__(self) -> str:
        return str(self.value)
