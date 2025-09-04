from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_azure_account_environment_id import EAzureAccountEnvironmentId
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudExistingAzureAccountInput")


@_attrs_define
class PublicCloudExistingAzureAccountInput:
    """
    Attributes:
        account_name (str): Name of a Microsoft Azure account.
        environment (EAzureAccountEnvironmentId): Type of a Microsoft Azure cloud environment.
        application_id (str): ID assigned to a Microsoft Azure application.
        tenant_id (str): ID assigned to a tenant available to a Microsoft Azure account.
        secret (str): Client secret.
        description (Union[Unset, str]): Description of a Microsoft Azure account.
    """

    account_name: str
    environment: EAzureAccountEnvironmentId
    application_id: str
    tenant_id: str
    secret: str
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_name = self.account_name

        environment = self.environment.value

        application_id = self.application_id

        tenant_id = self.tenant_id

        secret = self.secret

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountName": account_name,
                "environment": environment,
                "applicationId": application_id,
                "tenantId": tenant_id,
                "secret": secret,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_name = d.pop("accountName")

        environment = EAzureAccountEnvironmentId(d.pop("environment"))

        application_id = d.pop("applicationId")

        tenant_id = d.pop("tenantId")

        secret = d.pop("secret")

        description = d.pop("description", UNSET)

        public_cloud_existing_azure_account_input = cls(
            account_name=account_name,
            environment=environment,
            application_id=application_id,
            tenant_id=tenant_id,
            secret=secret,
            description=description,
        )

        public_cloud_existing_azure_account_input.additional_properties = d
        return public_cloud_existing_azure_account_input

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
