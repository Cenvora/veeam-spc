from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
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
        instance_uid (str | Unset): UID assigned to a VCSP Pulse tenant.
        mapping_status (PulseTenantMappingStatus | Unset): Mapping status of a VCSP Pulse tenant.
        mapping_status_message (str | Unset): Message for mapping status of a VCSP Pulse tenant.
        name (str | Unset): Name of a VCSP Pulse tenant.
        mapped_master_organization_uid (UUID | Unset): UID assigned to a master organization mapped to a VCSP Pulse
            tenant.
        merged_organization_uids (list[UUID] | Unset): Array of UIDs assigned to organizations merged with a master
            organization.
    """

    instance_uid: str | Unset = UNSET
    mapping_status: PulseTenantMappingStatus | Unset = UNSET
    mapping_status_message: str | Unset = UNSET
    name: str | Unset = UNSET
    mapped_master_organization_uid: UUID | Unset = UNSET
    merged_organization_uids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid = self.instance_uid

        mapping_status: str | Unset = UNSET
        if not isinstance(self.mapping_status, Unset):
            mapping_status = self.mapping_status.value

        mapping_status_message = self.mapping_status_message

        name = self.name

        mapped_master_organization_uid: str | Unset = UNSET
        if not isinstance(self.mapped_master_organization_uid, Unset):
            mapped_master_organization_uid = str(self.mapped_master_organization_uid)

        merged_organization_uids: list[str] | Unset = UNSET
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
        mapping_status: PulseTenantMappingStatus | Unset
        if isinstance(_mapping_status, Unset):
            mapping_status = UNSET
        else:
            mapping_status = PulseTenantMappingStatus(_mapping_status)

        mapping_status_message = d.pop("mappingStatusMessage", UNSET)

        name = d.pop("name", UNSET)

        _mapped_master_organization_uid = d.pop("mappedMasterOrganizationUid", UNSET)
        mapped_master_organization_uid: UUID | Unset
        if isinstance(_mapped_master_organization_uid, Unset):
            mapped_master_organization_uid = UNSET
        else:
            mapped_master_organization_uid = UUID(_mapped_master_organization_uid)

        _merged_organization_uids = d.pop("mergedOrganizationUids", UNSET)
        merged_organization_uids: list[UUID] | Unset = UNSET
        if _merged_organization_uids is not UNSET:
            merged_organization_uids = []
            for merged_organization_uids_item_data in _merged_organization_uids:
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
