from enum import Enum


class SmtpSettingsType0TlsMode(str, Enum):
    AUTO = "auto"
    NONE = "none"
    SSLONCONNECT = "sslOnConnect"
    STARTTLS = "startTls"
    STARTTLSWHENAVAILABLE = "startTlsWhenAvailable"

    def __str__(self) -> str:
        return str(self.value)
