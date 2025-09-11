from enum import Enum


class LinuxBackupVolumeSourceSettingsVolumeType(str, Enum):
    BTRFS = "BTRFS"
    DEVICE = "Device"
    LVM = "LVM"
    MOUNTPOINT = "MountPoint"

    def __str__(self) -> str:
        return str(self.value)
