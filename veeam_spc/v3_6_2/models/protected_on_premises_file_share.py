from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
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
        file_share_uid (UUID | Unset): UID assigned to a file share.
        backup_server_uid (UUID | Unset): UID assigned to a backup server.
        organization_uid (UUID | Unset): UID assigned to an organization.
        name (str | Unset): Name of a file share.
        latest_restore_point_date (datetime.datetime | None | Unset): Date and time of the latest restore point
            creation.
        total_archive_size (int | Unset): Size of archived file copies, in bytes.
        total_short_term_backup_size (int | Unset): Size of recent file copies, in bytes.
        archive_restore_points (int | Unset): Number of restore points for long-term retention.
        restore_points (int | Unset): Number of restore points.
    """

    file_share_uid: UUID | Unset = UNSET
    backup_server_uid: UUID | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    latest_restore_point_date: datetime.datetime | None | Unset = UNSET
    total_archive_size: int | Unset = UNSET
    total_short_term_backup_size: int | Unset = UNSET
    archive_restore_points: int | Unset = UNSET
    restore_points: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_share_uid: str | Unset = UNSET
        if not isinstance(self.file_share_uid, Unset):
            file_share_uid = str(self.file_share_uid)

        backup_server_uid: str | Unset = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        organization_uid: str | Unset = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        name = self.name

        latest_restore_point_date: None | str | Unset
        if isinstance(self.latest_restore_point_date, Unset):
            latest_restore_point_date = UNSET
        elif isinstance(self.latest_restore_point_date, datetime.datetime):
            latest_restore_point_date = self.latest_restore_point_date.isoformat()
        else:
            latest_restore_point_date = self.latest_restore_point_date

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
        file_share_uid: UUID | Unset
        if isinstance(_file_share_uid, Unset):
            file_share_uid = UNSET
        else:
            file_share_uid = UUID(_file_share_uid)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: UUID | Unset
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: UUID | Unset
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        name = d.pop("name", UNSET)

        def _parse_latest_restore_point_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_restore_point_date_type_0 = isoparse(data)

                return latest_restore_point_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        latest_restore_point_date = _parse_latest_restore_point_date(d.pop("latestRestorePointDate", UNSET))

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
