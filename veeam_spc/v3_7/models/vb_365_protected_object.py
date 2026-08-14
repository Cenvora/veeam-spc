from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.vb_365_protected_object_type import Vb365ProtectedObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365ProtectedObject")


@_attrs_define
class Vb365ProtectedObject:
    """
    Attributes:
        id (str | Unset): ID assigned to an object protected by Veeam Backup for Microsoft 365.
        name (str | Unset): Name of an object protected by Veeam Backup for Microsoft 365.
        repository_uid (UUID | Unset): UID assigned to a backup repository.
        repository_name (str | Unset): Name Of a backup repository.
        archive_repository_uid (UUID | Unset): UID assigned to an archive repository.
        archive_repository_name (str | Unset): Name an archive repository.
        protected_data_type (Vb365ProtectedObjectType | Unset): Type of a protected object.
        restore_points_count (int | Unset): Number of restore points created for an object protected by Veeam Backup for
            Microsoft 365.
        archive_restore_points_count (int | Unset): Number of archive restore points created for an object protected by
            Veeam Backup for Microsoft 365.
        latest_restore_point_date (datetime.datetime | Unset): Date and time when the latest restore point was created
            for an object protected by Veeam Backup for Microsoft 365.
        vb_365_server_uid (UUID | Unset): UID assigned to a Veeam Backup for Microsoft 365 server.
        vb_365_server_name (str | Unset): Name of a Veeam Backup for Microsoft 365 server.
        organization_uid (UUID | Unset): UID assigned to an organization to which a Veeam Backup for Microsoft 365
            server belongs.
        organization_name (str | Unset): Name of an organization to which a Veeam Backup for Microsoft 365 server
            belongs.
        vb_365_organization_uid (UUID | Unset): UID assigned to a Microsoft organization.
        vb_365_organization_name (str | Unset): Name of a Microsoft organization.
        site_uid (UUID | Unset): UID assigned to a Veeam Cloud Connect site on which an organization that owns a Veeam
            backup agent protecting an object is registered.
        site_name (str | Unset): Name of a Veeam Cloud Connect site on which an organization that owns Veeam backup
            agent protecting an object is registered.
        location_uid (UUID | Unset): UID assigned to a location assigned to Veeam backup agent protecting an object.
        location_name (str | Unset): Name of a location assigned to a Veeam backup agent protecting an object.
        consumes_license (bool | Unset): Indicates whether a protected object consumes license units.
        is_educational_user (bool | Unset): Indicates whether a protected user has Microsoft 365 educational
            subscription.
        file_restore_portal_url (str | Unset): URL of a file restore portal.
        is_file_restore_portal_enabled (bool | Unset): Indicates whether a file restore portal is enabled.
        is_restore_portal_access_enabled (bool | Unset): Indicates whether access to a file restore portal is enabled by
            a service provider.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    repository_uid: UUID | Unset = UNSET
    repository_name: str | Unset = UNSET
    archive_repository_uid: UUID | Unset = UNSET
    archive_repository_name: str | Unset = UNSET
    protected_data_type: Vb365ProtectedObjectType | Unset = UNSET
    restore_points_count: int | Unset = UNSET
    archive_restore_points_count: int | Unset = UNSET
    latest_restore_point_date: datetime.datetime | Unset = UNSET
    vb_365_server_uid: UUID | Unset = UNSET
    vb_365_server_name: str | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    organization_name: str | Unset = UNSET
    vb_365_organization_uid: UUID | Unset = UNSET
    vb_365_organization_name: str | Unset = UNSET
    site_uid: UUID | Unset = UNSET
    site_name: str | Unset = UNSET
    location_uid: UUID | Unset = UNSET
    location_name: str | Unset = UNSET
    consumes_license: bool | Unset = UNSET
    is_educational_user: bool | Unset = UNSET
    file_restore_portal_url: str | Unset = UNSET
    is_file_restore_portal_enabled: bool | Unset = UNSET
    is_restore_portal_access_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        repository_uid: str | Unset = UNSET
        if not isinstance(self.repository_uid, Unset):
            repository_uid = str(self.repository_uid)

        repository_name = self.repository_name

        archive_repository_uid: str | Unset = UNSET
        if not isinstance(self.archive_repository_uid, Unset):
            archive_repository_uid = str(self.archive_repository_uid)

        archive_repository_name = self.archive_repository_name

        protected_data_type: str | Unset = UNSET
        if not isinstance(self.protected_data_type, Unset):
            protected_data_type = self.protected_data_type.value

        restore_points_count = self.restore_points_count

        archive_restore_points_count = self.archive_restore_points_count

        latest_restore_point_date: str | Unset = UNSET
        if not isinstance(self.latest_restore_point_date, Unset):
            latest_restore_point_date = self.latest_restore_point_date.isoformat()

        vb_365_server_uid: str | Unset = UNSET
        if not isinstance(self.vb_365_server_uid, Unset):
            vb_365_server_uid = str(self.vb_365_server_uid)

        vb_365_server_name = self.vb_365_server_name

        organization_uid: str | Unset = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        organization_name = self.organization_name

        vb_365_organization_uid: str | Unset = UNSET
        if not isinstance(self.vb_365_organization_uid, Unset):
            vb_365_organization_uid = str(self.vb_365_organization_uid)

        vb_365_organization_name = self.vb_365_organization_name

        site_uid: str | Unset = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        site_name = self.site_name

        location_uid: str | Unset = UNSET
        if not isinstance(self.location_uid, Unset):
            location_uid = str(self.location_uid)

        location_name = self.location_name

        consumes_license = self.consumes_license

        is_educational_user = self.is_educational_user

        file_restore_portal_url = self.file_restore_portal_url

        is_file_restore_portal_enabled = self.is_file_restore_portal_enabled

        is_restore_portal_access_enabled = self.is_restore_portal_access_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if repository_uid is not UNSET:
            field_dict["repositoryUid"] = repository_uid
        if repository_name is not UNSET:
            field_dict["repositoryName"] = repository_name
        if archive_repository_uid is not UNSET:
            field_dict["archiveRepositoryUid"] = archive_repository_uid
        if archive_repository_name is not UNSET:
            field_dict["archiveRepositoryName"] = archive_repository_name
        if protected_data_type is not UNSET:
            field_dict["protectedDataType"] = protected_data_type
        if restore_points_count is not UNSET:
            field_dict["restorePointsCount"] = restore_points_count
        if archive_restore_points_count is not UNSET:
            field_dict["archiveRestorePointsCount"] = archive_restore_points_count
        if latest_restore_point_date is not UNSET:
            field_dict["latestRestorePointDate"] = latest_restore_point_date
        if vb_365_server_uid is not UNSET:
            field_dict["vb365ServerUid"] = vb_365_server_uid
        if vb_365_server_name is not UNSET:
            field_dict["vb365ServerName"] = vb_365_server_name
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if vb_365_organization_uid is not UNSET:
            field_dict["vb365OrganizationUid"] = vb_365_organization_uid
        if vb_365_organization_name is not UNSET:
            field_dict["vb365OrganizationName"] = vb_365_organization_name
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if location_uid is not UNSET:
            field_dict["locationUid"] = location_uid
        if location_name is not UNSET:
            field_dict["locationName"] = location_name
        if consumes_license is not UNSET:
            field_dict["consumesLicense"] = consumes_license
        if is_educational_user is not UNSET:
            field_dict["isEducationalUser"] = is_educational_user
        if file_restore_portal_url is not UNSET:
            field_dict["fileRestorePortalUrl"] = file_restore_portal_url
        if is_file_restore_portal_enabled is not UNSET:
            field_dict["isFileRestorePortalEnabled"] = is_file_restore_portal_enabled
        if is_restore_portal_access_enabled is not UNSET:
            field_dict["isRestorePortalAccessEnabled"] = is_restore_portal_access_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _repository_uid = d.pop("repositoryUid", UNSET)
        repository_uid: UUID | Unset
        if isinstance(_repository_uid, Unset):
            repository_uid = UNSET
        else:
            repository_uid = UUID(_repository_uid)

        repository_name = d.pop("repositoryName", UNSET)

        _archive_repository_uid = d.pop("archiveRepositoryUid", UNSET)
        archive_repository_uid: UUID | Unset
        if isinstance(_archive_repository_uid, Unset):
            archive_repository_uid = UNSET
        else:
            archive_repository_uid = UUID(_archive_repository_uid)

        archive_repository_name = d.pop("archiveRepositoryName", UNSET)

        _protected_data_type = d.pop("protectedDataType", UNSET)
        protected_data_type: Vb365ProtectedObjectType | Unset
        if isinstance(_protected_data_type, Unset):
            protected_data_type = UNSET
        else:
            protected_data_type = Vb365ProtectedObjectType(_protected_data_type)

        restore_points_count = d.pop("restorePointsCount", UNSET)

        archive_restore_points_count = d.pop("archiveRestorePointsCount", UNSET)

        _latest_restore_point_date = d.pop("latestRestorePointDate", UNSET)
        latest_restore_point_date: datetime.datetime | Unset
        if isinstance(_latest_restore_point_date, Unset):
            latest_restore_point_date = UNSET
        else:
            latest_restore_point_date = isoparse(_latest_restore_point_date)

        _vb_365_server_uid = d.pop("vb365ServerUid", UNSET)
        vb_365_server_uid: UUID | Unset
        if isinstance(_vb_365_server_uid, Unset):
            vb_365_server_uid = UNSET
        else:
            vb_365_server_uid = UUID(_vb_365_server_uid)

        vb_365_server_name = d.pop("vb365ServerName", UNSET)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: UUID | Unset
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        organization_name = d.pop("organizationName", UNSET)

        _vb_365_organization_uid = d.pop("vb365OrganizationUid", UNSET)
        vb_365_organization_uid: UUID | Unset
        if isinstance(_vb_365_organization_uid, Unset):
            vb_365_organization_uid = UNSET
        else:
            vb_365_organization_uid = UUID(_vb_365_organization_uid)

        vb_365_organization_name = d.pop("vb365OrganizationName", UNSET)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: UUID | Unset
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        site_name = d.pop("siteName", UNSET)

        _location_uid = d.pop("locationUid", UNSET)
        location_uid: UUID | Unset
        if isinstance(_location_uid, Unset):
            location_uid = UNSET
        else:
            location_uid = UUID(_location_uid)

        location_name = d.pop("locationName", UNSET)

        consumes_license = d.pop("consumesLicense", UNSET)

        is_educational_user = d.pop("isEducationalUser", UNSET)

        file_restore_portal_url = d.pop("fileRestorePortalUrl", UNSET)

        is_file_restore_portal_enabled = d.pop("isFileRestorePortalEnabled", UNSET)

        is_restore_portal_access_enabled = d.pop("isRestorePortalAccessEnabled", UNSET)

        vb_365_protected_object = cls(
            id=id,
            name=name,
            repository_uid=repository_uid,
            repository_name=repository_name,
            archive_repository_uid=archive_repository_uid,
            archive_repository_name=archive_repository_name,
            protected_data_type=protected_data_type,
            restore_points_count=restore_points_count,
            archive_restore_points_count=archive_restore_points_count,
            latest_restore_point_date=latest_restore_point_date,
            vb_365_server_uid=vb_365_server_uid,
            vb_365_server_name=vb_365_server_name,
            organization_uid=organization_uid,
            organization_name=organization_name,
            vb_365_organization_uid=vb_365_organization_uid,
            vb_365_organization_name=vb_365_organization_name,
            site_uid=site_uid,
            site_name=site_name,
            location_uid=location_uid,
            location_name=location_name,
            consumes_license=consumes_license,
            is_educational_user=is_educational_user,
            file_restore_portal_url=file_restore_portal_url,
            is_file_restore_portal_enabled=is_file_restore_portal_enabled,
            is_restore_portal_access_enabled=is_restore_portal_access_enabled,
        )

        vb_365_protected_object.additional_properties = d
        return vb_365_protected_object

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
