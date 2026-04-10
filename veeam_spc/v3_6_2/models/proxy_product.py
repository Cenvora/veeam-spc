from enum import Enum


class ProxyProduct(str, Enum):
    VEEAMBACKUPMICROSOFT365 = "VeeamBackupMicrosoft365"
    VEEAMBACKUPREPLICATION = "VeeamBackupReplication"
    VEEAMONE = "VeeamONE"

    def __str__(self) -> str:
        return str(self.value)
