import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedOnPremisesFileShare")


@_attrs_define
class ProtectedOnPremisesFileShare:
    """
    Attributes:
        file_share_uid (Union[Unset, UUID]): UID assigned to a file share.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a backup server.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        name (Union[Unset, str]): Name of a file share.
        latest_restore_point_date (Union[Unset, datetime.datetime]): Date and time of the latest restore point creation.
        total_archive_size (Union[Unset, int]): Size of archived file copies, in bytes.
        total_short_term_backup_size (Union[Unset, int]): Size of recent file copies, in bytes.
        archive_restore_points (Union[Unset, int]): Number of restore points for long-term retention.
        restore_points (Union[Unset, int]): Number of restore points.
    """

    file_share_uid: Union[Unset, UUID] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    latest_restore_point_date: Union[Unset, datetime.datetime] = UNSET
    total_archive_size: Union[Unset, int] = UNSET
    total_short_term_backup_size: Union[Unset, int] = UNSET
    archive_restore_points: Union[Unset, int] = UNSET
    restore_points: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_share_uid: Union[Unset, str] = UNSET
        if not isinstance(self.file_share_uid, Unset):
            file_share_uid = str(self.file_share_uid)

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        name = self.name

        latest_restore_point_date: Union[Unset, str] = UNSET
        if not isinstance(self.latest_restore_point_date, Unset):
            latest_restore_point_date = self.latest_restore_point_date.isoformat()

        total_archive_size = self.total_archive_size

        total_short_term_backup_size = self.total_short_term_backup_size

        archive_restore_points = self.archive_restore_points

        restore_points = self.restore_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_share_uid is not UNSET:
            field_dict["fileShareUid"] = file_share_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if name is not UNSET:
            field_dict["name"] = name
        if latest_restore_point_date is not UNSET:
            field_dict["latestRestorePointDate"] = latest_restore_point_date
        if total_archive_size is not UNSET:
            field_dict["totalArchiveSize"] = total_archive_size
        if total_short_term_backup_size is not UNSET:
            field_dict["totalShortTermBackupSize"] = total_short_term_backup_size
        if archive_restore_points is not UNSET:
            field_dict["archiveRestorePoints"] = archive_restore_points
        if restore_points is not UNSET:
            field_dict["restorePoints"] = restore_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _file_share_uid = d.pop("fileShareUid", UNSET)
        file_share_uid: Union[Unset, UUID]
        if isinstance(_file_share_uid, Unset):
            file_share_uid = UNSET
        else:
            file_share_uid = UUID(_file_share_uid)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        name = d.pop("name", UNSET)

        _latest_restore_point_date = d.pop("latestRestorePointDate", UNSET)
        latest_restore_point_date: Union[Unset, datetime.datetime]
        if isinstance(_latest_restore_point_date, Unset):
            latest_restore_point_date = UNSET
        else:
            latest_restore_point_date = isoparse(_latest_restore_point_date)

        total_archive_size = d.pop("totalArchiveSize", UNSET)

        total_short_term_backup_size = d.pop("totalShortTermBackupSize", UNSET)

        archive_restore_points = d.pop("archiveRestorePoints", UNSET)

        restore_points = d.pop("restorePoints", UNSET)

        protected_on_premises_file_share = cls(
            file_share_uid=file_share_uid,
            backup_server_uid=backup_server_uid,
            organization_uid=organization_uid,
            name=name,
            latest_restore_point_date=latest_restore_point_date,
            total_archive_size=total_archive_size,
            total_short_term_backup_size=total_short_term_backup_size,
            archive_restore_points=archive_restore_points,
            restore_points=restore_points,
        )

        protected_on_premises_file_share.additional_properties = d
        return protected_on_premises_file_share

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
