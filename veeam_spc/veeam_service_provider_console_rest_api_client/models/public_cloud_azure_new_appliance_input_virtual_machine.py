from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAzureNewApplianceInputVirtualMachine")


@_attrs_define
class PublicCloudAzureNewApplianceInputVirtualMachine:
    """
    Attributes:
        virtual_machine_name (str): Name of a VM.
        description (Union[Unset, str]): Description of a VM.
    """

    virtual_machine_name: str
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        virtual_machine_name = self.virtual_machine_name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "virtualMachineName": virtual_machine_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        virtual_machine_name = d.pop("virtualMachineName")

        description = d.pop("description", UNSET)

        public_cloud_azure_new_appliance_input_virtual_machine = cls(
            virtual_machine_name=virtual_machine_name,
            description=description,
        )

        public_cloud_azure_new_appliance_input_virtual_machine.additional_properties = d
        return public_cloud_azure_new_appliance_input_virtual_machine

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
