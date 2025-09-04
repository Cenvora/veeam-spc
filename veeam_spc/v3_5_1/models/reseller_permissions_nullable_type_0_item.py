from enum import Enum


class ResellerPermissionsNullableType0Item(str, Enum):
    REST = "REST"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
