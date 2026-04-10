from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pulse_tenant_mapping_status import PulseTenantMappingStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulseTenant")


@_attrs_define
class PulseTenant:
    """
    Attributes:
        instance_uid (Union[Unset, str]): UID assigned to a VCSP Pulse tenant.
        mapping_status (Union[Unset, PulseTenantMappingStatus]): Mapping status of a VCSP Pulse tenant.
        mapping_status_message (Union[Unset, str]): Message for mapping status of a VCSP Pulse tenant.
        name (Union[Unset, str]): Name of a VCSP Pulse tenant.
        mapped_master_organization_uid (Union[None, UUID, Unset]): UID assigned to a master organization mapped to a
            VCSP Pulse tenant.
        merged_organization_uids (Union[Unset, list[UUID]]): Array of UIDs assigned to organizations merged with a
            master organization.
    """

    instance_uid: Union[Unset, str] = UNSET
    mapping_status: Union[Unset, PulseTenantMappingStatus] = UNSET
    mapping_status_message: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    mapped_master_organization_uid: Union[None, UUID, Unset] = UNSET
    merged_organization_uids: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid = self.instance_uid

        mapping_status: Union[Unset, str] = UNSET
        if not isinstance(self.mapping_status, Unset):
            mapping_status = self.mapping_status.value

        mapping_status_message = self.mapping_status_message

        name = self.name

        mapped_master_organization_uid: Union[None, Unset, str]
        if isinstance(self.mapped_master_organization_uid, Unset):
            mapped_master_organization_uid = UNSET
        elif isinstance(self.mapped_master_organization_uid, UUID):
            mapped_master_organization_uid = str(self.mapped_master_organization_uid)
        else:
            mapped_master_organization_uid = self.mapped_master_organization_uid

        merged_organization_uids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.merged_organization_uids, Unset):
            merged_organization_uids = []
            for merged_organization_uids_item_data in self.merged_organization_uids:
                merged_organization_uids_item = str(merged_organization_uids_item_data)
                merged_organization_uids.append(merged_organization_uids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if mapping_status is not UNSET:
            field_dict["mappingStatus"] = mapping_status
        if mapping_status_message is not UNSET:
            field_dict["mappingStatusMessage"] = mapping_status_message
        if name is not UNSET:
            field_dict["name"] = name
        if mapped_master_organization_uid is not UNSET:
            field_dict["mappedMasterOrganizationUid"] = mapped_master_organization_uid
        if merged_organization_uids is not UNSET:
            field_dict["mergedOrganizationUids"] = merged_organization_uids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instance_uid = d.pop("instanceUid", UNSET)

        _mapping_status = d.pop("mappingStatus", UNSET)
        mapping_status: Union[Unset, PulseTenantMappingStatus]
        if isinstance(_mapping_status, Unset):
            mapping_status = UNSET
        else:
            mapping_status = PulseTenantMappingStatus(_mapping_status)

        mapping_status_message = d.pop("mappingStatusMessage", UNSET)

        name = d.pop("name", UNSET)

        def _parse_mapped_master_organization_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mapped_master_organization_uid_type_0 = UUID(data)

                return mapped_master_organization_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        mapped_master_organization_uid = _parse_mapped_master_organization_uid(
            d.pop("mappedMasterOrganizationUid", UNSET)
        )

        merged_organization_uids = []
        _merged_organization_uids = d.pop("mergedOrganizationUids", UNSET)
        for merged_organization_uids_item_data in _merged_organization_uids or []:
            merged_organization_uids_item = UUID(merged_organization_uids_item_data)

            merged_organization_uids.append(merged_organization_uids_item)

        pulse_tenant = cls(
            instance_uid=instance_uid,
            mapping_status=mapping_status,
            mapping_status_message=mapping_status_message,
            name=name,
            mapped_master_organization_uid=mapped_master_organization_uid,
            merged_organization_uids=merged_organization_uids,
        )

        pulse_tenant.additional_properties = d
        return pulse_tenant

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
