from enum import Enum


class CompanyPermissionsNullableItem(str, Enum):
    REST = "REST"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
