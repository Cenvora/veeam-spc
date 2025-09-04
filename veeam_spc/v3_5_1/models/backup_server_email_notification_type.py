from enum import Enum


class BackupServerEmailNotificationType(str, Enum):
    USECUSTOMNOTIFICATIONSETTINGS = "UseCustomNotificationSettings"
    USEGLOBALNOTIFICATIONSETTINGS = "UseGlobalNotificationSettings"

    def __str__(self) -> str:
        return str(self.value)
