from enum import Enum


class DownloadWindowsManagementPackagePackageType(str, Enum):
    EXE = "exe"
    MSI = "msi"

    def __str__(self) -> str:
        return str(self.value)
