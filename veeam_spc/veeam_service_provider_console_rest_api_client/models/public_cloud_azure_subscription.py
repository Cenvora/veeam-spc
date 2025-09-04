from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_azure_environment_id_readonly import EAzureEnvironmentIdReadonly
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAzureSubscription")


@_attrs_define
class PublicCloudAzureSubscription:
    """
    Attributes:
        subscription_id (Union[Unset, UUID]): ID assigned to a Microsoft Azure subscription.
        subscription_name (Union[Unset, str]): Name of a Microsoft Azure subscription.
        environment (Union[Unset, EAzureEnvironmentIdReadonly]): Type of a Microsoft Azure cloud environment.
        tenant_id (Union[Unset, str]): ID assigned to a tenant available to a Microsoft Azure account.
    """

    subscription_id: Union[Unset, UUID] = UNSET
    subscription_name: Union[Unset, str] = UNSET
    environment: Union[Unset, EAzureEnvironmentIdReadonly] = UNSET
    tenant_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscription_id: Union[Unset, str] = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        subscription_name = self.subscription_name

        environment: Union[Unset, str] = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.value

        tenant_id = self.tenant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if subscription_name is not UNSET:
            field_dict["subscriptionName"] = subscription_name
        if environment is not UNSET:
            field_dict["environment"] = environment
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: Union[Unset, UUID]
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        subscription_name = d.pop("subscriptionName", UNSET)

        _environment = d.pop("environment", UNSET)
        environment: Union[Unset, EAzureEnvironmentIdReadonly]
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = EAzureEnvironmentIdReadonly(_environment)

        tenant_id = d.pop("tenantId", UNSET)

        public_cloud_azure_subscription = cls(
            subscription_id=subscription_id,
            subscription_name=subscription_name,
            environment=environment,
            tenant_id=tenant_id,
        )

        public_cloud_azure_subscription.additional_properties = d
        return public_cloud_azure_subscription

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
