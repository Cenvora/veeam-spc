from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.async_action_request_data_query_parameters import AsyncActionRequestDataQueryParameters


T = TypeVar("T", bound="AsyncActionRequestData")


@_attrs_define
class AsyncActionRequestData:
    """
    Example:
        {'requestBody': '{ "siteUid": "d18f40ef-a80f-45c0-a4b6-0de1f5615145", "cloudTenantType": "General",
            "vCloudOrganizationUid": null, "leaseExpirationEnabled": false, "ownerCredentials": { "userName": "Alpha",
            "password": "Password1" }, "description": "Site Resource for Alpha Company", "throttlingEnabled": false,
            "throttlingValue": 1, "throttlingUnit": "MbitPerSec", "maxConcurrentTask": 1, "backupProtectionEnabled": false,
            "backupProtectionPeriodDays": 1, "gatewaySelectionType": "StandaloneGateways", "isGatewayFailoverEnabled":
            false}', 'queryParameters': None}

    Attributes:
        request_body (str | Unset): Content of a request body of the operation that initiated an async action.
        query_parameters (AsyncActionRequestDataQueryParameters | Unset): Key-value map containing query parameters of
            the operation that initiated an async action.
    """

    request_body: str | Unset = UNSET
    query_parameters: AsyncActionRequestDataQueryParameters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_body = self.request_body

        query_parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_parameters, Unset):
            query_parameters = self.query_parameters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_body is not UNSET:
            field_dict["requestBody"] = request_body
        if query_parameters is not UNSET:
            field_dict["queryParameters"] = query_parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.async_action_request_data_query_parameters import AsyncActionRequestDataQueryParameters

        d = dict(src_dict)
        request_body = d.pop("requestBody", UNSET)

        _query_parameters = d.pop("queryParameters", UNSET)
        query_parameters: AsyncActionRequestDataQueryParameters | Unset
        if isinstance(_query_parameters, Unset):
            query_parameters = UNSET
        else:
            query_parameters = AsyncActionRequestDataQueryParameters.from_dict(_query_parameters)

        async_action_request_data = cls(
            request_body=request_body,
            query_parameters=query_parameters,
        )

        async_action_request_data.additional_properties = d
        return async_action_request_data

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
