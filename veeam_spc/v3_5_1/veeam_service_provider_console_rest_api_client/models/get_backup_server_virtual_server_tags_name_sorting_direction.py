from enum import Enum


class GetBackupServerVirtualServerTagsNameSortingDirection(str, Enum):
    ASCENDING = "ascending"
    DESCENDING = "descending"

    def __str__(self) -> str:
        return str(self.value)
