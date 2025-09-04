from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.e_azure_account_environment_id import EAzureAccountEnvironmentId
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAzureAccountInput")


@_attrs_define
class PublicCloudAzureAccountInput:
    """
    Attributes:
        account_name (str): Name of an account.
        environment (EAzureAccountEnvironmentId): Type of a Microsoft Azure cloud environment.
        user_code (str): User code.
        description (Union[Unset, str]): Description of an account.
    """

    account_name: str
    environment: EAzureAccountEnvironmentId
    user_code: str
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_name = self.account_name

        environment = self.environment.value

        user_code = self.user_code

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountName": account_name,
                "environment": environment,
                "userCode": user_code,
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

        user_code = d.pop("userCode")

        description = d.pop("description", UNSET)

        public_cloud_azure_account_input = cls(
            account_name=account_name,
            environment=environment,
            user_code=user_code,
            description=description,
        )

        public_cloud_azure_account_input.additional_properties = d
        return public_cloud_azure_account_input

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
