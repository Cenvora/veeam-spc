from enum import Enum


class AddApiKeyLoginScopesItem(str, Enum):
    INTEGRATION = "integration"
    REST = "rest"
    UI = "ui"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
