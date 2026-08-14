from enum import Enum


class OAuth2SignInParametersNavigationMode(str, Enum):
    REDIRECT = "redirect"

    def __str__(self) -> str:
        return str(self.value)
