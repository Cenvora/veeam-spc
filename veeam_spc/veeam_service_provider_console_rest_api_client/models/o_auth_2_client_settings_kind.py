from enum import Enum


class OAuth2ClientSettingsKind(str, Enum):
    AZURE = "Azure"
    GOOGLE = "Google"

    def __str__(self) -> str:
        return str(self.value)
