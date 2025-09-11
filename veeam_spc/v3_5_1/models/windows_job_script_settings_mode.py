from enum import Enum


class WindowsJobScriptSettingsMode(str, Enum):
    DISABLED = "Disabled"
    FAILJOBONERROR = "FailJobOnError"
    IGNOREERRORS = "IgnoreErrors"

    def __str__(self) -> str:
        return str(self.value)
