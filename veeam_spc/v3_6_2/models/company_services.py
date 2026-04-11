from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        hosted_services (CompanyHostedServices | None | Unset):
        remote_services (CompanyRemoteServices | None | Unset):
    """

    hosted_services: CompanyHostedServices | None | Unset = UNSET
    remote_services: CompanyRemoteServices | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hosted_services: dict[str, Any] | None | Unset = UNSET
        if not isinstance(self.hosted_services, Unset):
            if self.hosted_services is None:
                hosted_services = None
            else:
                hosted_services = self.hosted_services.to_dict()

        remote_services: dict[str, Any] | None | Unset = UNSET
        if not isinstance(self.remote_services, Unset):
            if self.remote_services is None:
                remote_services = None
            else:
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

        def _parse_hosted_services(
            data: object,
        ) -> CompanyHostedServices | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_company_hosted_services = (
                    CompanyHostedServices.from_dict(data)
                )

                return componentsschemas_company_hosted_services
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyHostedServices | None | Unset, data)

        _hosted_services = d.pop("hostedServices", UNSET)
        hosted_services = _parse_hosted_services(_hosted_services)

        def _parse_remote_services(
            data: object,
        ) -> CompanyRemoteServices | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_company_remote_services = (
                    CompanyRemoteServices.from_dict(data)
                )

                return componentsschemas_company_remote_services
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyRemoteServices | None | Unset, data)

        _remote_services = d.pop("remoteServices", UNSET)
        remote_services = _parse_remote_services(_remote_services)

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
