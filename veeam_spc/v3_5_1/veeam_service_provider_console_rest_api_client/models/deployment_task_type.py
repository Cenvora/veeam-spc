from enum import Enum


class DeploymentTaskType(str, Enum):
    DEPLOY = "Deploy"
    DEPLOYVBR = "DeployVbr"
    DISCOVERY = "Discovery"
    EXECUTE = "Execute"
    INFRASTRUCTUREAGENTDEPLOY = "InfrastructureAgentDeploy"
    OTHER = "Other"
    PATCHNIXAGENT = "PatchNixAgent"
    PATCHPUBLICCLOUD = "PatchPublicCloud"
    PATCHVBR = "PatchVbr"
    PATCHWINAGENT = "PatchWinAgent"
    UNKNOWN = "Unknown"
    UPDATENIXAGENT = "UpdateNixAgent"
    UPDATEWINAGENT = "UpdateWinAgent"
    UPGRADEVAC = "UpgradeVac"
    UPGRADEVBR = "UpgradeVbr"
    VBDEPLOY = "VbDeploy"
    VBREGISTER = "VbRegister"
    VBRISOPREDOWNLOAD = "VbrIsoPredownload"
    VBSERVICEACCOUNTUPDATE = "VbServiceAccountUpdate"
    VBSQLACCOUNTREMOVE = "VbSqlAccountRemove"
    VBUPGRADE = "VbUpgrade"
    VBUSERACCOUNTUPDATE = "VbUserAccountUpdate"

    def __str__(self) -> str:
        return str(self.value)
