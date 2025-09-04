from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.organization_license_usage_organization_type import OrganizationLicenseUsageOrganizationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationLicenseUsage")


@_attrs_define
class OrganizationLicenseUsage:
    """
    Attributes:
        organization_type (Union[Unset, OrganizationLicenseUsageOrganizationType]): Organization type.
        organization_name (Union[Unset, str]): Organization name.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        tenant_uid (Union[Unset, UUID]): UID assigned to a tenant.
            > For resellers the property value is `null`.
        used_points (Union[Unset, float]): Number of license points used by an organization.
    """

    organization_type: Union[Unset, OrganizationLicenseUsageOrganizationType] = UNSET
    organization_name: Union[Unset, str] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    tenant_uid: Union[Unset, UUID] = UNSET
    used_points: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_type: Union[Unset, str] = UNSET
        if not isinstance(self.organization_type, Unset):
            organization_type = self.organization_type.value

        organization_name = self.organization_name

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        tenant_uid: Union[Unset, str] = UNSET
        if not isinstance(self.tenant_uid, Unset):
            tenant_uid = str(self.tenant_uid)

        used_points = self.used_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_type is not UNSET:
            field_dict["organizationType"] = organization_type
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if tenant_uid is not UNSET:
            field_dict["tenantUid"] = tenant_uid
        if used_points is not UNSET:
            field_dict["usedPoints"] = used_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _organization_type = d.pop("organizationType", UNSET)
        organization_type: Union[Unset, OrganizationLicenseUsageOrganizationType]
        if isinstance(_organization_type, Unset):
            organization_type = UNSET
        else:
            organization_type = OrganizationLicenseUsageOrganizationType(_organization_type)

        organization_name = d.pop("organizationName", UNSET)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _tenant_uid = d.pop("tenantUid", UNSET)
        tenant_uid: Union[Unset, UUID]
        if isinstance(_tenant_uid, Unset):
            tenant_uid = UNSET
        else:
            tenant_uid = UUID(_tenant_uid)

        used_points = d.pop("usedPoints", UNSET)

        organization_license_usage = cls(
            organization_type=organization_type,
            organization_name=organization_name,
            organization_uid=organization_uid,
            tenant_uid=tenant_uid,
            used_points=used_points,
        )

        organization_license_usage.additional_properties = d
        return organization_license_usage

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
