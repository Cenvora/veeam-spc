from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrganizationLocationInput")


@_attrs_define
class OrganizationLocationInput:
    """
    Attributes:
        organization_uid (UUID): UID assigned to an organization.
        name (str): Name of a location.
        quota_gb (int): Amount of storage space allocated to a location, in gigabytes.
    """

    organization_uid: UUID
    name: str
    quota_gb: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_uid = str(self.organization_uid)

        name = self.name

        quota_gb = self.quota_gb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organizationUid": organization_uid,
                "name": name,
                "quotaGb": quota_gb,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization_uid = UUID(d.pop("organizationUid"))

        name = d.pop("name")

        quota_gb = d.pop("quotaGb")

        organization_location_input = cls(
            organization_uid=organization_uid,
            name=name,
            quota_gb=quota_gb,
        )

        organization_location_input.additional_properties = d
        return organization_location_input

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
