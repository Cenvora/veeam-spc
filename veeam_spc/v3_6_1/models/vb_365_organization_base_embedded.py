from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_organization_details import Vb365OrganizationDetails
    from ..models.vb_365_server import Vb365Server


T = TypeVar("T", bound="Vb365OrganizationBaseEmbedded")


@_attrs_define
class Vb365OrganizationBaseEmbedded:
    """
    Attributes:
        organization_details (Union[Unset, Vb365OrganizationDetails]):
        vb_365_server (Union[Unset, Vb365Server]):
    """

    organization_details: Union[Unset, "Vb365OrganizationDetails"] = UNSET
    vb_365_server: Union[Unset, "Vb365Server"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization_details, Unset):
            organization_details = self.organization_details.to_dict()

        vb_365_server: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vb_365_server, Unset):
            vb_365_server = self.vb_365_server.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_details is not UNSET:
            field_dict["organizationDetails"] = organization_details
        if vb_365_server is not UNSET:
            field_dict["vb365Server"] = vb_365_server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_organization_details import Vb365OrganizationDetails
        from ..models.vb_365_server import Vb365Server

        d = dict(src_dict)
        _organization_details = d.pop("organizationDetails", UNSET)
        organization_details: Union[Unset, Vb365OrganizationDetails]
        if isinstance(_organization_details, Unset):
            organization_details = UNSET
        else:
            organization_details = Vb365OrganizationDetails.from_dict(_organization_details)

        _vb_365_server = d.pop("vb365Server", UNSET)
        vb_365_server: Union[Unset, Vb365Server]
        if isinstance(_vb_365_server, Unset):
            vb_365_server = UNSET
        else:
            vb_365_server = Vb365Server.from_dict(_vb_365_server)

        vb_365_organization_base_embedded = cls(
            organization_details=organization_details,
            vb_365_server=vb_365_server,
        )

        vb_365_organization_base_embedded.additional_properties = d
        return vb_365_organization_base_embedded

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
