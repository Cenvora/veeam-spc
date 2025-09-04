from enum import Enum


class DownloadWindowsManagementPackageOsType(str, Enum):
    X64 = "x64"
    X86 = "x86"

    def __str__(self) -> str:
        return str(self.value)
