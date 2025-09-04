from enum import Enum


class DownloadMacManagementPackagePackageType(str, Enum):
    SH = "sh"
    ZIP = "zip"

    def __str__(self) -> str:
        return str(self.value)
