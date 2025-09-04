from enum import Enum


class DiscoveryRuleStatus(str, Enum):
    CANCELED = "Canceled"
    CANCELLATIONREQUESTED = "CancellationRequested"
    CANCELLATIONREQUESTFAILED = "CancellationRequestFailed"
    CREATED = "Created"
    FAILED = "Failed"
    RUNNING = "Running"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
