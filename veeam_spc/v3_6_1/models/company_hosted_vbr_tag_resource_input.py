from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.virtual_server_tag import VirtualServerTag


T = TypeVar("T", bound="CompanyHostedVbrTagResourceInput")


@_attrs_define
class CompanyHostedVbrTagResourceInput:
    """
    Attributes:
        virtual_center_uid (UUID): vCenter Server UID.
        virtual_server_tag (VirtualServerTag):
    """

    virtual_center_uid: UUID
    virtual_server_tag: "VirtualServerTag"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        virtual_center_uid = str(self.virtual_center_uid)

        virtual_server_tag = self.virtual_server_tag.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "virtualCenterUid": virtual_center_uid,
                "virtualServerTag": virtual_server_tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.virtual_server_tag import VirtualServerTag

        d = dict(src_dict)
        virtual_center_uid = UUID(d.pop("virtualCenterUid"))

        virtual_server_tag = VirtualServerTag.from_dict(d.pop("virtualServerTag"))

        company_hosted_vbr_tag_resource_input = cls(
            virtual_center_uid=virtual_center_uid,
            virtual_server_tag=virtual_server_tag,
        )

        company_hosted_vbr_tag_resource_input.additional_properties = d
        return company_hosted_vbr_tag_resource_input

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
