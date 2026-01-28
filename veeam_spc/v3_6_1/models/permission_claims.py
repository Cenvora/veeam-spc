from enum import Enum


class PermissionClaims(str, Enum):
    HOSTEDVBM365JOBCREATE = "HostedVbm365JobCreate"
    HOSTEDVBM365JOBDELETE = "HostedVbm365JobDelete"
    HOSTEDVBM365JOBEDIT = "HostedVbm365JobEdit"
    HOSTEDVBM365JOBENABLEDISABLE = "HostedVbm365JobEnableDisable"
    HOSTEDVBM365JOBREPOSITORYWRITE = "HostedVbm365JobRepositoryWrite"
    HOSTEDVBM365JOBSCHEDULEWRITE = "HostedVbm365JobScheduleWrite"
    HOSTEDVBM365JOBSCOPEWRITE = "HostedVbm365JobScopeWrite"
    HOSTEDVBM365JOBSTARTSTOP = "HostedVbm365JobStartStop"
    HOSTEDVBRJOBCREATE = "HostedVbrJobCreate"
    HOSTEDVBRJOBDELETE = "HostedVbrJobDelete"
    HOSTEDVBRJOBEDIT = "HostedVbrJobEdit"
    HOSTEDVBRJOBENABLEDISABLE = "HostedVbrJobEnableDisable"
    HOSTEDVBRJOBGUESTPROCESSINGWRITE = "HostedVbrJobGuestProcessingWrite"
    HOSTEDVBRJOBRETENTIONWRITE = "HostedVbrJobRetentionWrite"
    HOSTEDVBRJOBSCHEDULEWRITE = "HostedVbrJobScheduleWrite"
    HOSTEDVBRJOBSCOPEWRITE = "HostedVbrJobScopeWrite"
    HOSTEDVBRJOBSTARTSTOP = "HostedVbrJobStartStop"
    HOSTEDVBRJOBSTORAGEWRITE = "HostedVbrJobStorageWrite"
    PUBLICCLOUDJOBCREATE = "PublicCloudJobCreate"
    PUBLICCLOUDJOBDELETE = "PublicCloudJobDelete"
    PUBLICCLOUDJOBEDIT = "PublicCloudJobEdit"
    PUBLICCLOUDJOBENABLEDISABLE = "PublicCloudJobEnableDisable"
    PUBLICCLOUDJOBSTARTSTOP = "PublicCloudJobStartStop"

    def __str__(self) -> str:
        return str(self.value)
