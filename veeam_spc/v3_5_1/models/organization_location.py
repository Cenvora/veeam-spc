from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.organization_location_type import OrganizationLocationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationLocation")


@_attrs_define
class OrganizationLocation:
    """
    Attributes:
        name (str): Name of a location.
        quota_gb (int): Amount of storage space allocated to a location, in gigabytes.
        instance_uid (Union[Unset, UUID]): UID assigned to a location in Veeam Service Provider Console.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        type_ (Union[Unset, OrganizationLocationType]): Type of an organization location. Default:
            OrganizationLocationType.CUSTOM.
    """

    name: str
    quota_gb: int
    instance_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    type_: Union[Unset, OrganizationLocationType] = OrganizationLocationType.CUSTOM
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        quota_gb = self.quota_gb

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "quotaGb": quota_gb,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        quota_gb = d.pop("quotaGb")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, OrganizationLocationType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = OrganizationLocationType(_type_)

        organization_location = cls(
            name=name,
            quota_gb=quota_gb,
            instance_uid=instance_uid,
            organization_uid=organization_uid,
            type_=type_,
        )

        organization_location.additional_properties = d
        return organization_location

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
