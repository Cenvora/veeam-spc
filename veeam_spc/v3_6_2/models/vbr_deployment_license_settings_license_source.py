from enum import Enum


class VbrDeploymentLicenseSettingsLicenseSource(str, Enum):
    ANSWERXML = "AnswerXml"
    LICENSEFILECONTENT = "LicenseFileContent"
    LICENSEUID = "LicenseUid"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
