from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_hybrid_organization import Vb365HybridOrganization
    from ..models.vb_365_microsoft_365_organization import Vb365Microsoft365Organization
    from ..models.vb_365_on_premises_microsoft_organization import Vb365OnPremisesMicrosoftOrganization


T = TypeVar("T", bound="Vb365OrganizationDetails")


@_attrs_define
class Vb365OrganizationDetails:
    """
    Attributes:
        microsoft_365_organization_details (Union[Unset, Vb365Microsoft365Organization]):
        on_premises_organization_details (Union[Unset, Vb365OnPremisesMicrosoftOrganization]):
        hybrid_organization_details (Union[Unset, Vb365HybridOrganization]):
    """

    microsoft_365_organization_details: Union[Unset, "Vb365Microsoft365Organization"] = UNSET
    on_premises_organization_details: Union[Unset, "Vb365OnPremisesMicrosoftOrganization"] = UNSET
    hybrid_organization_details: Union[Unset, "Vb365HybridOrganization"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        microsoft_365_organization_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.microsoft_365_organization_details, Unset):
            microsoft_365_organization_details = self.microsoft_365_organization_details.to_dict()

        on_premises_organization_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.on_premises_organization_details, Unset):
            on_premises_organization_details = self.on_premises_organization_details.to_dict()

        hybrid_organization_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.hybrid_organization_details, Unset):
            hybrid_organization_details = self.hybrid_organization_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if microsoft_365_organization_details is not UNSET:
            field_dict["microsoft365OrganizationDetails"] = microsoft_365_organization_details
        if on_premises_organization_details is not UNSET:
            field_dict["onPremisesOrganizationDetails"] = on_premises_organization_details
        if hybrid_organization_details is not UNSET:
            field_dict["hybridOrganizationDetails"] = hybrid_organization_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_hybrid_organization import Vb365HybridOrganization
        from ..models.vb_365_microsoft_365_organization import Vb365Microsoft365Organization
        from ..models.vb_365_on_premises_microsoft_organization import Vb365OnPremisesMicrosoftOrganization

        d = dict(src_dict)
        _microsoft_365_organization_details = d.pop("microsoft365OrganizationDetails", UNSET)
        microsoft_365_organization_details: Union[Unset, Vb365Microsoft365Organization]
        if isinstance(_microsoft_365_organization_details, Unset):
            microsoft_365_organization_details = UNSET
        else:
            microsoft_365_organization_details = Vb365Microsoft365Organization.from_dict(
                _microsoft_365_organization_details
            )

        _on_premises_organization_details = d.pop("onPremisesOrganizationDetails", UNSET)
        on_premises_organization_details: Union[Unset, Vb365OnPremisesMicrosoftOrganization]
        if isinstance(_on_premises_organization_details, Unset):
            on_premises_organization_details = UNSET
        else:
            on_premises_organization_details = Vb365OnPremisesMicrosoftOrganization.from_dict(
                _on_premises_organization_details
            )

        _hybrid_organization_details = d.pop("hybridOrganizationDetails", UNSET)
        hybrid_organization_details: Union[Unset, Vb365HybridOrganization]
        if isinstance(_hybrid_organization_details, Unset):
            hybrid_organization_details = UNSET
        else:
            hybrid_organization_details = Vb365HybridOrganization.from_dict(_hybrid_organization_details)

        vb_365_organization_details = cls(
            microsoft_365_organization_details=microsoft_365_organization_details,
            on_premises_organization_details=on_premises_organization_details,
            hybrid_organization_details=hybrid_organization_details,
        )

        vb_365_organization_details.additional_properties = d
        return vb_365_organization_details

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
