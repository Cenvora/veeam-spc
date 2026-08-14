from enum import Enum


class AlarmActionType(str, Enum):
    EXECUTELOCALSCRIPT = "ExecuteLocalScript"
    EXECUTEREMOTESCRIPT = "ExecuteRemoteScript"
    SENDCUSTOMEMAIL = "SendCustomEmail"
    SENDGLOBALEMAIL = "SendGlobalEmail"
    SENDWEBHOOK = "SendWebhook"

    def __str__(self) -> str:
        return str(self.value)
