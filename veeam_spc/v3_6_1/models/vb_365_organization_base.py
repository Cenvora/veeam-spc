import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
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
        instance_uid (Union[Unset, UUID]): UID assigned to a Microsoft organization.
        region (Union[Unset, Vb365OrganizationBaseRegion]): Region where a Microsoft organization is located.
            > Available only for Microsoft 365 and hybrid organizations.
        cloud_authenticated_method (Union[Unset, Vb365OrganizationBaseCloudAuthenticatedMethod]): Authentication type of
            a Microsoft organization.
            Available only for Microsoft 365 and hybrid organization.
        protected_services (Union[Unset, list[Vb365OrganizationBaseProtectedServicesItem]]): Array of protected
            Microsoft organization services.
        vb_365_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup for Microsoft 365 server.
        vb_365_server_name (Union[Unset, str]): Name of a Veeam Backup for Microsoft 365 server.
        location_uid (Union[None, UUID, Unset]): UID assigned to a location of a management agent installed on a Veeam
            Backup for Microsoft 365 server.
            > If a Veeam Backup for Microsoft 365 server is not managed by Veeam Service Provider Console, the property
            value is `null`.
        location_name (Union[None, Unset, str]): Name of a location of a management agent installed on a Veeam Backup
            for Microsoft 365 server.
            > If a Veeam Backup for Microsoft 365 server is not managed by Veeam Service Provider Console, the property
            value is `null`.
        first_backup_time (Union[None, Unset, datetime.datetime]): Date and time when Microsoft organization were
            processed by a backup job for the first time.
        last_backup_time (Union[None, Unset, datetime.datetime]): Date and time when Microsoft organization files were
            processed by a backup job for the last time.
        registered_by (Union[None, Unset, str]): Name of a Veeam Service Provider Console organization that registered a
            Microsoft organization.
            If a Microsoft organization was not created in Veeam Service Provider Console or was deleted, the property value
            is `null`.
        registration_date (Union[None, Unset, datetime.datetime]): Date and time when a Microsoft organization was
            registered.
            If a Microsoft organization was not created in Veeam Service Provider Console, the property value is `null`.
        is_removing (Union[Unset, bool]): Indicates whether a Microsoft organization is currently being removed.
        is_job_scheduling_enabled (Union[None, Unset, bool]): Indicates whether the current user can apply changes to a
            Microsoft organization job schedule.
        mapped_organization_uid (Union[None, UUID, Unset]): UID assigned to an organization that is mapped to a
            Microsoft organization.
        mapped_organization_name (Union[None, Unset, str]): Name of an organization that is mapped to a Microsoft
            organization.
        field_embedded (Union[Unset, Vb365OrganizationBaseEmbedded]):
    """

    name: str
    type_: Vb365OrganizationBaseType
    is_backed_up: bool
    instance_uid: Union[Unset, UUID] = UNSET
    region: Union[Unset, Vb365OrganizationBaseRegion] = UNSET
    cloud_authenticated_method: Union[Unset, Vb365OrganizationBaseCloudAuthenticatedMethod] = UNSET
    protected_services: Union[Unset, list[Vb365OrganizationBaseProtectedServicesItem]] = UNSET
    vb_365_server_uid: Union[Unset, UUID] = UNSET
    vb_365_server_name: Union[Unset, str] = UNSET
    location_uid: Union[None, UUID, Unset] = UNSET
    location_name: Union[None, Unset, str] = UNSET
    first_backup_time: Union[None, Unset, datetime.datetime] = UNSET
    last_backup_time: Union[None, Unset, datetime.datetime] = UNSET
    registered_by: Union[None, Unset, str] = UNSET
    registration_date: Union[None, Unset, datetime.datetime] = UNSET
    is_removing: Union[Unset, bool] = UNSET
    is_job_scheduling_enabled: Union[None, Unset, bool] = UNSET
    mapped_organization_uid: Union[None, UUID, Unset] = UNSET
    mapped_organization_name: Union[None, Unset, str] = UNSET
    field_embedded: Union[Unset, "Vb365OrganizationBaseEmbedded"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        is_backed_up = self.is_backed_up

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        region: Union[Unset, str] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        cloud_authenticated_method: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_authenticated_method, Unset):
            cloud_authenticated_method = self.cloud_authenticated_method.value

        protected_services: Union[Unset, list[str]] = UNSET
        if not isinstance(self.protected_services, Unset):
            protected_services = []
            for protected_services_item_data in self.protected_services:
                protected_services_item = protected_services_item_data.value
                protected_services.append(protected_services_item)

        vb_365_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.vb_365_server_uid, Unset):
            vb_365_server_uid = str(self.vb_365_server_uid)

        vb_365_server_name = self.vb_365_server_name

        location_uid: Union[None, Unset, str]
        if isinstance(self.location_uid, Unset):
            location_uid = UNSET
        elif isinstance(self.location_uid, UUID):
            location_uid = str(self.location_uid)
        else:
            location_uid = self.location_uid

        location_name: Union[None, Unset, str]
        if isinstance(self.location_name, Unset):
            location_name = UNSET
        else:
            location_name = self.location_name

        first_backup_time: Union[None, Unset, str]
        if isinstance(self.first_backup_time, Unset):
            first_backup_time = UNSET
        elif isinstance(self.first_backup_time, datetime.datetime):
            first_backup_time = self.first_backup_time.isoformat()
        else:
            first_backup_time = self.first_backup_time

        last_backup_time: Union[None, Unset, str]
        if isinstance(self.last_backup_time, Unset):
            last_backup_time = UNSET
        elif isinstance(self.last_backup_time, datetime.datetime):
            last_backup_time = self.last_backup_time.isoformat()
        else:
            last_backup_time = self.last_backup_time

        registered_by: Union[None, Unset, str]
        if isinstance(self.registered_by, Unset):
            registered_by = UNSET
        else:
            registered_by = self.registered_by

        registration_date: Union[None, Unset, str]
        if isinstance(self.registration_date, Unset):
            registration_date = UNSET
        elif isinstance(self.registration_date, datetime.datetime):
            registration_date = self.registration_date.isoformat()
        else:
            registration_date = self.registration_date

        is_removing = self.is_removing

        is_job_scheduling_enabled: Union[None, Unset, bool]
        if isinstance(self.is_job_scheduling_enabled, Unset):
            is_job_scheduling_enabled = UNSET
        else:
            is_job_scheduling_enabled = self.is_job_scheduling_enabled

        mapped_organization_uid: Union[None, Unset, str]
        if isinstance(self.mapped_organization_uid, Unset):
            mapped_organization_uid = UNSET
        elif isinstance(self.mapped_organization_uid, UUID):
            mapped_organization_uid = str(self.mapped_organization_uid)
        else:
            mapped_organization_uid = self.mapped_organization_uid

        mapped_organization_name: Union[None, Unset, str]
        if isinstance(self.mapped_organization_name, Unset):
            mapped_organization_name = UNSET
        else:
            mapped_organization_name = self.mapped_organization_name

        field_embedded: Union[Unset, dict[str, Any]] = UNSET
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
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _region = d.pop("region", UNSET)
        region: Union[Unset, Vb365OrganizationBaseRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = Vb365OrganizationBaseRegion(_region)

        _cloud_authenticated_method = d.pop("cloudAuthenticatedMethod", UNSET)
        cloud_authenticated_method: Union[Unset, Vb365OrganizationBaseCloudAuthenticatedMethod]
        if isinstance(_cloud_authenticated_method, Unset):
            cloud_authenticated_method = UNSET
        else:
            cloud_authenticated_method = Vb365OrganizationBaseCloudAuthenticatedMethod(_cloud_authenticated_method)

        protected_services = []
        _protected_services = d.pop("protectedServices", UNSET)
        for protected_services_item_data in _protected_services or []:
            protected_services_item = Vb365OrganizationBaseProtectedServicesItem(protected_services_item_data)

            protected_services.append(protected_services_item)

        _vb_365_server_uid = d.pop("vb365ServerUid", UNSET)
        vb_365_server_uid: Union[Unset, UUID]
        if isinstance(_vb_365_server_uid, Unset):
            vb_365_server_uid = UNSET
        else:
            vb_365_server_uid = UUID(_vb_365_server_uid)

        vb_365_server_name = d.pop("vb365ServerName", UNSET)

        def _parse_location_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                location_uid_type_0 = UUID(data)

                return location_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        location_uid = _parse_location_uid(d.pop("locationUid", UNSET))

        def _parse_location_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_name = _parse_location_name(d.pop("locationName", UNSET))

        def _parse_first_backup_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_backup_time_type_0 = isoparse(data)

                return first_backup_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        first_backup_time = _parse_first_backup_time(d.pop("firstBackupTime", UNSET))

        def _parse_last_backup_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_backup_time_type_0 = isoparse(data)

                return last_backup_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_backup_time = _parse_last_backup_time(d.pop("lastBackupTime", UNSET))

        def _parse_registered_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        registered_by = _parse_registered_by(d.pop("registeredBy", UNSET))

        def _parse_registration_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registration_date_type_0 = isoparse(data)

                return registration_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        registration_date = _parse_registration_date(d.pop("registrationDate", UNSET))

        is_removing = d.pop("isRemoving", UNSET)

        def _parse_is_job_scheduling_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_job_scheduling_enabled = _parse_is_job_scheduling_enabled(d.pop("isJobSchedulingEnabled", UNSET))

        def _parse_mapped_organization_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mapped_organization_uid_type_0 = UUID(data)

                return mapped_organization_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        mapped_organization_uid = _parse_mapped_organization_uid(d.pop("mappedOrganizationUid", UNSET))

        def _parse_mapped_organization_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mapped_organization_name = _parse_mapped_organization_name(d.pop("mappedOrganizationName", UNSET))

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, Vb365OrganizationBaseEmbedded]
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
