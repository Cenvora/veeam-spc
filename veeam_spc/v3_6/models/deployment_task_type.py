from enum import Enum


class DeploymentTaskType(str, Enum):
    DEPLOY = "Deploy"
    DEPLOYVBR = "DeployVbr"
    DEPLOYVONE = "DeployVOne"
    DISCOVERY = "Discovery"
    EXECUTE = "Execute"
    HOSTEDAGENTDEPLOY = "HostedAgentDeploy"
    OTHER = "Other"
    PATCHNIXAGENT = "PatchNixAgent"
    PATCHPUBLICCLOUD = "PatchPublicCloud"
    PATCHVBR = "PatchVbr"
    PATCHVONE = "PatchVOne"
    PATCHWINAGENT = "PatchWinAgent"
    UNKNOWN = "Unknown"
    UPDATENIXAGENT = "UpdateNixAgent"
    UPDATEWINAGENT = "UpdateWinAgent"
    UPGRADEVAC = "UpgradeVac"
    UPGRADEVBR = "UpgradeVbr"
    UPGRADEVONE = "UpgradeVOne"
    VBDEPLOY = "VbDeploy"
    VBREGISTER = "VbRegister"
    VBRISOPREDOWNLOAD = "VbrIsoPredownload"
    VBSERVICEACCOUNTUPDATE = "VbServiceAccountUpdate"
    VBSQLACCOUNTREMOVE = "VbSqlAccountRemove"
    VBUPGRADE = "VbUpgrade"
    VBUSERACCOUNTUPDATE = "VbUserAccountUpdate"
    VONEISOPREDOWNLOAD = "VOneIsoPredownload"
    VONEPATCHISOPREDOWNLOAD = "VOnePatchIsoPredownload"

    def __str__(self) -> str:
        return str(self.value)
