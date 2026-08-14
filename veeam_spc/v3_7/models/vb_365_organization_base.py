from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.vb_365_organization_base_cloud_authenticated_method import Vb365OrganizationBaseCloudAuthenticatedMethod
from ..models.vb_365_organization_base_protected_services_item import Vb365OrganizationBaseProtectedServicesItem
from ..models.vb_365_organization_base_region import Vb365OrganizationBaseRegion
from ..models.vb_365_organization_base_type import Vb365OrganizationBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_organization_base_embedded import Vb365OrganizationBaseEmbedded


T = TypeVar("T", bound="Vb365OrganizationBase")


@_attrs_define
class Vb365OrganizationBase:
    """
    Attributes:
        name (str): Name of a Microsoft organization.
        type_ (Vb365OrganizationBaseType): Type of a Microsoft organization.
        is_backed_up (bool): Indicates whether the Microsoft organization files have been processed by a backup job.
        instance_uid (UUID | Unset): UID assigned to a Microsoft organization.
        region (Vb365OrganizationBaseRegion | Unset): Region where a Microsoft organization is located.
            > Available only for Microsoft 365 and hybrid organizations.
        cloud_authenticated_method (Vb365OrganizationBaseCloudAuthenticatedMethod | Unset): Authentication type of a
            Microsoft organization.
            Available only for Microsoft 365 and hybrid organization.
        protected_services (list[Vb365OrganizationBaseProtectedServicesItem] | Unset): Array of protected Microsoft
            organization services.
        vb_365_server_uid (UUID | Unset): UID assigned to a Veeam Backup for Microsoft 365 server.
        vb_365_server_name (str | Unset): Name of a Veeam Backup for Microsoft 365 server.
        location_uid (UUID | Unset): UID assigned to a location of a management agent installed on a Veeam Backup for
            Microsoft 365 server.
            > If a Veeam Backup for Microsoft 365 server is not managed by Veeam Service Provider Console, the property
            value is `null`.
        location_name (str | Unset): Name of a location of a management agent installed on a Veeam Backup for Microsoft
            365 server.
            > If a Veeam Backup for Microsoft 365 server is not managed by Veeam Service Provider Console, the property
            value is `null`.
        first_backup_time (datetime.datetime | Unset): Date and time when Microsoft organization were processed by a
            backup job for the first time.
        last_backup_time (datetime.datetime | Unset): Date and time when Microsoft organization files were processed by
            a backup job for the last time.
        registered_by (str | Unset): Name of a Veeam Service Provider Console organization that registered a Microsoft
            organization.
            If a Microsoft organization was not created in Veeam Service Provider Console or was deleted, the property value
            is `null`.
        registration_date (datetime.datetime | Unset): Date and time when a Microsoft organization was registered.
            If a Microsoft organization was not created in Veeam Service Provider Console, the property value is `null`.
        is_removing (bool | Unset): Indicates whether a Microsoft organization is currently being removed.
        is_job_scheduling_enabled (bool | Unset): Indicates whether the current user can apply changes to a Microsoft
            organization job schedule.
        mapped_organization_uid (UUID | Unset): UID assigned to an organization that is mapped to a Microsoft
            organization.
        mapped_organization_name (str | Unset): Name of an organization that is mapped to a Microsoft organization.
        field_embedded (Vb365OrganizationBaseEmbedded | Unset):
    """

    name: str
    type_: Vb365OrganizationBaseType
    is_backed_up: bool
    instance_uid: UUID | Unset = UNSET
    region: Vb365OrganizationBaseRegion | Unset = UNSET
    cloud_authenticated_method: Vb365OrganizationBaseCloudAuthenticatedMethod | Unset = UNSET
    protected_services: list[Vb365OrganizationBaseProtectedServicesItem] | Unset = UNSET
    vb_365_server_uid: UUID | Unset = UNSET
    vb_365_server_name: str | Unset = UNSET
    location_uid: UUID | Unset = UNSET
    location_name: str | Unset = UNSET
    first_backup_time: datetime.datetime | Unset = UNSET
    last_backup_time: datetime.datetime | Unset = UNSET
    registered_by: str | Unset = UNSET
    registration_date: datetime.datetime | Unset = UNSET
    is_removing: bool | Unset = UNSET
    is_job_scheduling_enabled: bool | Unset = UNSET
    mapped_organization_uid: UUID | Unset = UNSET
    mapped_organization_name: str | Unset = UNSET
    field_embedded: Vb365OrganizationBaseEmbedded | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        is_backed_up = self.is_backed_up

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        region: str | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        cloud_authenticated_method: str | Unset = UNSET
        if not isinstance(self.cloud_authenticated_method, Unset):
            cloud_authenticated_method = self.cloud_authenticated_method.value

        protected_services: list[str] | Unset = UNSET
        if not isinstance(self.protected_services, Unset):
            protected_services = []
            for protected_services_item_data in self.protected_services:
                protected_services_item = protected_services_item_data.value
                protected_services.append(protected_services_item)

        vb_365_server_uid: str | Unset = UNSET
        if not isinstance(self.vb_365_server_uid, Unset):
            vb_365_server_uid = str(self.vb_365_server_uid)

        vb_365_server_name = self.vb_365_server_name

        location_uid: str | Unset = UNSET
        if not isinstance(self.location_uid, Unset):
            location_uid = str(self.location_uid)

        location_name = self.location_name

        first_backup_time: str | Unset = UNSET
        if not isinstance(self.first_backup_time, Unset):
            first_backup_time = self.first_backup_time.isoformat()

        last_backup_time: str | Unset = UNSET
        if not isinstance(self.last_backup_time, Unset):
            last_backup_time = self.last_backup_time.isoformat()

        registered_by = self.registered_by

        registration_date: str | Unset = UNSET
        if not isinstance(self.registration_date, Unset):
            registration_date = self.registration_date.isoformat()

        is_removing = self.is_removing

        is_job_scheduling_enabled = self.is_job_scheduling_enabled

        mapped_organization_uid: str | Unset = UNSET
        if not isinstance(self.mapped_organization_uid, Unset):
            mapped_organization_uid = str(self.mapped_organization_uid)

        mapped_organization_name = self.mapped_organization_name

        field_embedded: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "isBackedUp": is_backed_up,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if region is not UNSET:
            field_dict["region"] = region
        if cloud_authenticated_method is not UNSET:
            field_dict["cloudAuthenticatedMethod"] = cloud_authenticated_method
        if protected_services is not UNSET:
            field_dict["protectedServices"] = protected_services
        if vb_365_server_uid is not UNSET:
            field_dict["vb365ServerUid"] = vb_365_server_uid
        if vb_365_server_name is not UNSET:
            field_dict["vb365ServerName"] = vb_365_server_name
        if location_uid is not UNSET:
            field_dict["locationUid"] = location_uid
        if location_name is not UNSET:
            field_dict["locationName"] = location_name
        if first_backup_time is not UNSET:
            field_dict["firstBackupTime"] = first_backup_time
        if last_backup_time is not UNSET:
            field_dict["lastBackupTime"] = last_backup_time
        if registered_by is not UNSET:
            field_dict["registeredBy"] = registered_by
        if registration_date is not UNSET:
            field_dict["registrationDate"] = registration_date
        if is_removing is not UNSET:
            field_dict["isRemoving"] = is_removing
        if is_job_scheduling_enabled is not UNSET:
            field_dict["isJobSchedulingEnabled"] = is_job_scheduling_enabled
        if mapped_organization_uid is not UNSET:
            field_dict["mappedOrganizationUid"] = mapped_organization_uid
        if mapped_organization_name is not UNSET:
            field_dict["mappedOrganizationName"] = mapped_organization_name
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_organization_base_embedded import Vb365OrganizationBaseEmbedded

        d = dict(src_dict)
        name = d.pop("name")

        type_ = Vb365OrganizationBaseType(d.pop("type"))

        is_backed_up = d.pop("isBackedUp")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _region = d.pop("region", UNSET)
        region: Vb365OrganizationBaseRegion | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = Vb365OrganizationBaseRegion(_region)

        _cloud_authenticated_method = d.pop("cloudAuthenticatedMethod", UNSET)
        cloud_authenticated_method: Vb365OrganizationBaseCloudAuthenticatedMethod | Unset
        if isinstance(_cloud_authenticated_method, Unset):
            cloud_authenticated_method = UNSET
        else:
            cloud_authenticated_method = Vb365OrganizationBaseCloudAuthenticatedMethod(_cloud_authenticated_method)

        _protected_services = d.pop("protectedServices", UNSET)
        protected_services: list[Vb365OrganizationBaseProtectedServicesItem] | Unset = UNSET
        if _protected_services is not UNSET:
            protected_services = []
            for protected_services_item_data in _protected_services:
                protected_services_item = Vb365OrganizationBaseProtectedServicesItem(protected_services_item_data)

                protected_services.append(protected_services_item)

        _vb_365_server_uid = d.pop("vb365ServerUid", UNSET)
        vb_365_server_uid: UUID | Unset
        if isinstance(_vb_365_server_uid, Unset):
            vb_365_server_uid = UNSET
        else:
            vb_365_server_uid = UUID(_vb_365_server_uid)

        vb_365_server_name = d.pop("vb365ServerName", UNSET)

        _location_uid = d.pop("locationUid", UNSET)
        location_uid: UUID | Unset
        if isinstance(_location_uid, Unset):
            location_uid = UNSET
        else:
            location_uid = UUID(_location_uid)

        location_name = d.pop("locationName", UNSET)

        _first_backup_time = d.pop("firstBackupTime", UNSET)
        first_backup_time: datetime.datetime | Unset
        if isinstance(_first_backup_time, Unset):
            first_backup_time = UNSET
        else:
            first_backup_time = isoparse(_first_backup_time)

        _last_backup_time = d.pop("lastBackupTime", UNSET)
        last_backup_time: datetime.datetime | Unset
        if isinstance(_last_backup_time, Unset):
            last_backup_time = UNSET
        else:
            last_backup_time = isoparse(_last_backup_time)

        registered_by = d.pop("registeredBy", UNSET)

        _registration_date = d.pop("registrationDate", UNSET)
        registration_date: datetime.datetime | Unset
        if isinstance(_registration_date, Unset):
            registration_date = UNSET
        else:
            registration_date = isoparse(_registration_date)

        is_removing = d.pop("isRemoving", UNSET)

        is_job_scheduling_enabled = d.pop("isJobSchedulingEnabled", UNSET)

        _mapped_organization_uid = d.pop("mappedOrganizationUid", UNSET)
        mapped_organization_uid: UUID | Unset
        if isinstance(_mapped_organization_uid, Unset):
            mapped_organization_uid = UNSET
        else:
            mapped_organization_uid = UUID(_mapped_organization_uid)

        mapped_organization_name = d.pop("mappedOrganizationName", UNSET)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Vb365OrganizationBaseEmbedded | Unset
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = Vb365OrganizationBaseEmbedded.from_dict(_field_embedded)

        vb_365_organization_base = cls(
            name=name,
            type_=type_,
            is_backed_up=is_backed_up,
            instance_uid=instance_uid,
            region=region,
            cloud_authenticated_method=cloud_authenticated_method,
            protected_services=protected_services,
            vb_365_server_uid=vb_365_server_uid,
            vb_365_server_name=vb_365_server_name,
            location_uid=location_uid,
            location_name=location_name,
            first_backup_time=first_backup_time,
            last_backup_time=last_backup_time,
            registered_by=registered_by,
            registration_date=registration_date,
            is_removing=is_removing,
            is_job_scheduling_enabled=is_job_scheduling_enabled,
            mapped_organization_uid=mapped_organization_uid,
            mapped_organization_name=mapped_organization_name,
            field_embedded=field_embedded,
        )

        vb_365_organization_base.additional_properties = d
        return vb_365_organization_base

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
