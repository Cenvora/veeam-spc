from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_license_usage import ProductLicenseUsage


T = TypeVar("T", bound="OrganizationUsageOfLicensesWithSameSupportId")


@_attrs_define
class OrganizationUsageOfLicensesWithSameSupportId:
    """
    Attributes:
        organization_name (str | Unset): Organization name.
        organization_uid (UUID | Unset): UID assigned to an organization.
        support_id (str | Unset): License support ID.
        not_collected_client_servers (list[str] | Unset): Array of client servers from which Veeam Service Provider
            Console could not collect the license usage data.
        cloned_client_servers (list[str] | Unset): Array of cloned client servers.
        unsupported_client_servers (list[str] | Unset): Array of unsupported client servers.
        usage_by_license_and_product (list[ProductLicenseUsage] | Unset): License usage for each license and product.
    """

    organization_name: str | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    support_id: str | Unset = UNSET
    not_collected_client_servers: list[str] | Unset = UNSET
    cloned_client_servers: list[str] | Unset = UNSET
    unsupported_client_servers: list[str] | Unset = UNSET
    usage_by_license_and_product: list[ProductLicenseUsage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_name = self.organization_name

        organization_uid: str | Unset = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        support_id = self.support_id

        not_collected_client_servers: list[str] | Unset = UNSET
        if not isinstance(self.not_collected_client_servers, Unset):
            not_collected_client_servers = self.not_collected_client_servers

        cloned_client_servers: list[str] | Unset = UNSET
        if not isinstance(self.cloned_client_servers, Unset):
            cloned_client_servers = self.cloned_client_servers

        unsupported_client_servers: list[str] | Unset = UNSET
        if not isinstance(self.unsupported_client_servers, Unset):
            unsupported_client_servers = self.unsupported_client_servers

        usage_by_license_and_product: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.usage_by_license_and_product, Unset):
            usage_by_license_and_product = []
            for usage_by_license_and_product_item_data in self.usage_by_license_and_product:
                usage_by_license_and_product_item = usage_by_license_and_product_item_data.to_dict()
                usage_by_license_and_product.append(usage_by_license_and_product_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if support_id is not UNSET:
            field_dict["supportId"] = support_id
        if not_collected_client_servers is not UNSET:
            field_dict["notCollectedClientServers"] = not_collected_client_servers
        if cloned_client_servers is not UNSET:
            field_dict["clonedClientServers"] = cloned_client_servers
        if unsupported_client_servers is not UNSET:
            field_dict["unsupportedClientServers"] = unsupported_client_servers
        if usage_by_license_and_product is not UNSET:
            field_dict["usageByLicenseAndProduct"] = usage_by_license_and_product

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_license_usage import ProductLicenseUsage

        d = dict(src_dict)
        organization_name = d.pop("organizationName", UNSET)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: UUID | Unset
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        support_id = d.pop("supportId", UNSET)

        not_collected_client_servers = cast(list[str], d.pop("notCollectedClientServers", UNSET))

        cloned_client_servers = cast(list[str], d.pop("clonedClientServers", UNSET))

        unsupported_client_servers = cast(list[str], d.pop("unsupportedClientServers", UNSET))

        _usage_by_license_and_product = d.pop("usageByLicenseAndProduct", UNSET)
        usage_by_license_and_product: list[ProductLicenseUsage] | Unset = UNSET
        if _usage_by_license_and_product is not UNSET:
            usage_by_license_and_product = []
            for usage_by_license_and_product_item_data in _usage_by_license_and_product:
                usage_by_license_and_product_item = ProductLicenseUsage.from_dict(
                    usage_by_license_and_product_item_data
                )

                usage_by_license_and_product.append(usage_by_license_and_product_item)

        organization_usage_of_licenses_with_same_support_id = cls(
            organization_name=organization_name,
            organization_uid=organization_uid,
            support_id=support_id,
            not_collected_client_servers=not_collected_client_servers,
            cloned_client_servers=cloned_client_servers,
            unsupported_client_servers=unsupported_client_servers,
            usage_by_license_and_product=usage_by_license_and_product,
        )

        organization_usage_of_licenses_with_same_support_id.additional_properties = d
        return organization_usage_of_licenses_with_same_support_id

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
