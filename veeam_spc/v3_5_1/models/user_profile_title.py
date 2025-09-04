from enum import Enum


class UserProfileTitle(str, Enum):
    MISS = "Miss"
    MR = "Mr"
    MRS = "Mrs"
    MS = "Ms"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
