from enum import Enum


class WebhookAuthType(str, Enum):
    BASICAUTH = "BasicAuth"
    BEARERTOKEN = "BearerToken"
    CUSTOMHEADER = "CustomHeader"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
