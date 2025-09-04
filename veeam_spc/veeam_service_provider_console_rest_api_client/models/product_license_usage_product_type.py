from enum import Enum


class ProductLicenseUsageProductType(str, Enum):
    BACKUPANDREPLICATION = "BackupAndReplication"
    CLOUDCONNECT = "CloudConnect"
    ENTERPRISEMANAGER = "EnterpriseManager"
    UNKNOWN = "Unknown"
    VB365 = "VB365"
    VONE = "VONE"
    VSPC = "VSPC"

    def __str__(self) -> str:
        return str(self.value)
