from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_azure_environment_id_readonly import EAzureEnvironmentIdReadonly
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAzureResourceGroup")


@_attrs_define
class PublicCloudAzureResourceGroup:
    """
    Attributes:
        resource_group_name (Union[Unset, str]): Name of a resource group.
        environment (Union[Unset, EAzureEnvironmentIdReadonly]): Type of a Microsoft Azure cloud environment.
        subscription_id (Union[Unset, UUID]): UID assigned to a Microsoft Azure subscription.
        data_center_id (Union[Unset, str]): ID assigned to a Microsoft Azure datacenter.
    """

    resource_group_name: Union[Unset, str] = UNSET
    environment: Union[Unset, EAzureEnvironmentIdReadonly] = UNSET
    subscription_id: Union[Unset, UUID] = UNSET
    data_center_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_group_name = self.resource_group_name

        environment: Union[Unset, str] = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.value

        subscription_id: Union[Unset, str] = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        data_center_id = self.data_center_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_group_name is not UNSET:
            field_dict["resourceGroupName"] = resource_group_name
        if environment is not UNSET:
            field_dict["environment"] = environment
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if data_center_id is not UNSET:
            field_dict["dataCenterId"] = data_center_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_group_name = d.pop("resourceGroupName", UNSET)

        _environment = d.pop("environment", UNSET)
        environment: Union[Unset, EAzureEnvironmentIdReadonly]
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = EAzureEnvironmentIdReadonly(_environment)

        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: Union[Unset, UUID]
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        data_center_id = d.pop("dataCenterId", UNSET)

        public_cloud_azure_resource_group = cls(
            resource_group_name=resource_group_name,
            environment=environment,
            subscription_id=subscription_id,
            data_center_id=data_center_id,
        )

        public_cloud_azure_resource_group.additional_properties = d
        return public_cloud_azure_resource_group

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
