from enum import Enum


class WindowsWorkstationJobPeriodicalScheduleSettingsFinalizingAction(str, Enum):
    HIBERNATE = "Hibernate"
    KEEPRUNNING = "KeepRunning"
    SHUTDOWN = "Shutdown"
    SLEEP = "Sleep"

    def __str__(self) -> str:
        return str(self.value)
