from enum import Enum


class TestSmtpSettingsResponseResult(str, Enum):
    AUTHENTICATIONERROR = "AuthenticationError"
    CONNECTIONERROR = "ConnectionError"
    OK = "Ok"

    def __str__(self) -> str:
        return str(self.value)
