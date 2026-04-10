from enum import Enum


class SmtpSettingsTlsMode(str, Enum):
    AUTO = "auto"
    NONE = "none"
    SSLONCONNECT = "sslOnConnect"
    STARTTLS = "startTls"
    STARTTLSWHENAVAILABLE = "startTlsWhenAvailable"

    def __str__(self) -> str:
        return str(self.value)
