from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_hosted_services import CompanyHostedServices
    from ..models.company_remote_services import CompanyRemoteServices


T = TypeVar("T", bound="CompanyServices")


@_attrs_define
class CompanyServices:
    """
    Attributes:
        hosted_services (Union[Unset, CompanyHostedServices]):
        remote_services (Union[Unset, CompanyRemoteServices]):
    """

    hosted_services: Union[Unset, "CompanyHostedServices"] = UNSET
    remote_services: Union[Unset, "CompanyRemoteServices"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hosted_services: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.hosted_services, Unset):
            hosted_services = self.hosted_services.to_dict()

        remote_services: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.remote_services, Unset):
            remote_services = self.remote_services.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hosted_services is not UNSET:
            field_dict["hostedServices"] = hosted_services
        if remote_services is not UNSET:
            field_dict["remoteServices"] = remote_services

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_hosted_services import CompanyHostedServices
        from ..models.company_remote_services import CompanyRemoteServices

        d = dict(src_dict)
        _hosted_services = d.pop("hostedServices", UNSET)
        hosted_services: Union[Unset, CompanyHostedServices]
        if isinstance(_hosted_services, Unset):
            hosted_services = UNSET
        else:
            hosted_services = CompanyHostedServices.from_dict(_hosted_services)

        _remote_services = d.pop("remoteServices", UNSET)
        remote_services: Union[Unset, CompanyRemoteServices]
        if isinstance(_remote_services, Unset):
            remote_services = UNSET
        else:
            remote_services = CompanyRemoteServices.from_dict(_remote_services)

        company_services = cls(
            hosted_services=hosted_services,
            remote_services=remote_services,
        )

        company_services.additional_properties = d
        return company_services

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
