from enum import Enum


class LinuxOracleArchivedLogsTruncationConfigTruncationMode(str, Enum):
    TRUNCATEBYAGE = "TruncateByAge"
    TRUNCATEBYSIZE = "TruncateBySize"
    TRUNCATEDISABLED = "TruncateDisabled"

    def __str__(self) -> str:
        return str(self.value)
