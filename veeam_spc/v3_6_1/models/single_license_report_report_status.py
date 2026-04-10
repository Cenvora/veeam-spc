from enum import Enum


class SingleLicenseReportReportStatus(str, Enum):
    APPROVALREQUIRED = "ApprovalRequired"
    APPROVED = "Approved"
    FINALIZATION = "Finalization"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
