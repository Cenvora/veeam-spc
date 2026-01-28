from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.permission_claims import PermissionClaims

T = TypeVar("T", bound="EntityPermissions")


@_attrs_define
class EntityPermissions:
    """
    Attributes:
        claims (list[PermissionClaims]): Array of permission claims assigned to a Veeam Service Provider Console entity.
    """

    claims: list[PermissionClaims]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        claims = []
        for claims_item_data in self.claims:
            claims_item = claims_item_data.value
            claims.append(claims_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "claims": claims,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        claims = []
        _claims = d.pop("claims")
        for claims_item_data in _claims:
            claims_item = PermissionClaims(claims_item_data)

            claims.append(claims_item)

        entity_permissions = cls(
            claims=claims,
        )

        entity_permissions.additional_properties = d
        return entity_permissions

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
