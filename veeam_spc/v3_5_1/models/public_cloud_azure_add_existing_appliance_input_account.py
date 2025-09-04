from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_azure_environment_id import EAzureEnvironmentId

T = TypeVar("T", bound="PublicCloudAzureAddExistingApplianceInputAccount")


@_attrs_define
class PublicCloudAzureAddExistingApplianceInputAccount:
    """
    Attributes:
        account_uid (UUID): UID assigned to an account in Microsoft Azure.
        subscription_id (str): ID assigned to a Microsoft Azure connection.
        data_center_id (str): ID assigned to a Microsoft Azure datacenter.
        connection_uid (UUID): UID assigned to a Microsoft Azure connection.
        environment (EAzureEnvironmentId): Type of a Microsoft Azure cloud environment.
    """

    account_uid: UUID
    subscription_id: str
    data_center_id: str
    connection_uid: UUID
    environment: EAzureEnvironmentId
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_uid = str(self.account_uid)

        subscription_id = self.subscription_id

        data_center_id = self.data_center_id

        connection_uid = str(self.connection_uid)

        environment = self.environment.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountUid": account_uid,
                "subscriptionId": subscription_id,
                "dataCenterId": data_center_id,
                "connectionUid": connection_uid,
                "environment": environment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_uid = UUID(d.pop("accountUid"))

        subscription_id = d.pop("subscriptionId")

        data_center_id = d.pop("dataCenterId")

        connection_uid = UUID(d.pop("connectionUid"))

        environment = EAzureEnvironmentId(d.pop("environment"))

        public_cloud_azure_add_existing_appliance_input_account = cls(
            account_uid=account_uid,
            subscription_id=subscription_id,
            data_center_id=data_center_id,
            connection_uid=connection_uid,
            environment=environment,
        )

        public_cloud_azure_add_existing_appliance_input_account.additional_properties = d
        return public_cloud_azure_add_existing_appliance_input_account

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
