from enum import Enum


class AlarmActionCondition(str, Enum):
    ALLSTATES = "AllStates"
    ERRORSANDWARNINGS = "ErrorsAndWarnings"
    ERRORSONLY = "ErrorsOnly"

    def __str__(self) -> str:
        return str(self.value)
