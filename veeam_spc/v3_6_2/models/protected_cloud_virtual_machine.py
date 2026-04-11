from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.backup_server_public_cloud_appliance_platform import BackupServerPublicCloudAppliancePlatform
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedCloudVirtualMachine")


@_attrs_define
class ProtectedCloudVirtualMachine:
    """
    Attributes:
        instance_uid (UUID | Unset): UID assigned to a protected cloud VM.
        backup_server_uid (UUID | Unset): UID assigned to a backup server.
        organization_uid (UUID | Unset): UID assigned to an organization.
        name (str | Unset): VM hostname.
        appliance_uid (None | Unset | UUID): UID assigned to a Veeam Backup for Public Clouds appliance.
        platform_type (BackupServerPublicCloudAppliancePlatform | Unset): Platform of a Veeam Backup for Public Clouds
            appliance.
        resource_id (str | Unset): Resource ID of a cloud VM.
        destinations (list[str] | Unset): Array of locations where backup files for a cloud VM reside.
        latest_backup_date (datetime.datetime | None | Unset): Date and time of the latest backup restore point
            creation.
    """

    instance_uid: UUID | Unset = UNSET
    backup_server_uid: UUID | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    appliance_uid: None | Unset | UUID = UNSET
    platform_type: BackupServerPublicCloudAppliancePlatform | Unset = UNSET
    resource_id: str | Unset = UNSET
    destinations: list[str] | Unset = UNSET
    latest_backup_date: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        backup_server_uid: str | Unset = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        organization_uid: str | Unset = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        name = self.name

        appliance_uid: None | str | Unset
        if isinstance(self.appliance_uid, Unset):
            appliance_uid = UNSET
        elif isinstance(self.appliance_uid, UUID):
            appliance_uid = str(self.appliance_uid)
        else:
            appliance_uid = self.appliance_uid

        platform_type: str | Unset = UNSET
        if not isinstance(self.platform_type, Unset):
            platform_type = self.platform_type.value

        resource_id = self.resource_id

        destinations: list[str] | Unset = UNSET
        if not isinstance(self.destinations, Unset):
            destinations = self.destinations

        latest_backup_date: None | str | Unset
        if isinstance(self.latest_backup_date, Unset):
            latest_backup_date = UNSET
        elif isinstance(self.latest_backup_date, datetime.datetime):
            latest_backup_date = self.latest_backup_date.isoformat()
        else:
            latest_backup_date = self.latest_backup_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if name is not UNSET:
            field_dict["name"] = name
        if appliance_uid is not UNSET:
            field_dict["applianceUid"] = appliance_uid
        if platform_type is not UNSET:
            field_dict["platformType"] = platform_type
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if latest_backup_date is not UNSET:
            field_dict["latestBackupDate"] = latest_backup_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

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

        def _parse_appliance_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                appliance_uid_type_0 = UUID(data)

                return appliance_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        appliance_uid = _parse_appliance_uid(d.pop("applianceUid", UNSET))

        _platform_type = d.pop("platformType", UNSET)
        platform_type: BackupServerPublicCloudAppliancePlatform | Unset
        if isinstance(_platform_type, Unset):
            platform_type = UNSET
        else:
            platform_type = BackupServerPublicCloudAppliancePlatform(_platform_type)

        resource_id = d.pop("resourceId", UNSET)

        destinations = cast(list[str], d.pop("destinations", UNSET))

        def _parse_latest_backup_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_backup_date_type_0 = isoparse(data)

                return latest_backup_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        latest_backup_date = _parse_latest_backup_date(d.pop("latestBackupDate", UNSET))

        protected_cloud_virtual_machine = cls(
            instance_uid=instance_uid,
            backup_server_uid=backup_server_uid,
            organization_uid=organization_uid,
            name=name,
            appliance_uid=appliance_uid,
            platform_type=platform_type,
            resource_id=resource_id,
            destinations=destinations,
            latest_backup_date=latest_backup_date,
        )

        protected_cloud_virtual_machine.additional_properties = d
        return protected_cloud_virtual_machine

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
