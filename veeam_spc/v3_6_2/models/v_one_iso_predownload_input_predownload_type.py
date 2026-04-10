from enum import Enum


class VOneIsoPredownloadInputPredownloadType(str, Enum):
    PATCH = "Patch"
    REGULAR = "Regular"

    def __str__(self) -> str:
        return str(self.value)
