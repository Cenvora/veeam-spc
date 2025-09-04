from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAzureVirtualMachine")


@_attrs_define
class PublicCloudAzureVirtualMachine:
    """
    Attributes:
        virtual_machine_id (Union[Unset, str]): ID assigned to a VM.
        virtual_machine_name (Union[Unset, str]): Name of a VM.
    """

    virtual_machine_id: Union[Unset, str] = UNSET
    virtual_machine_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        virtual_machine_id = self.virtual_machine_id

        virtual_machine_name = self.virtual_machine_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if virtual_machine_id is not UNSET:
            field_dict["virtualMachineId"] = virtual_machine_id
        if virtual_machine_name is not UNSET:
            field_dict["virtualMachineName"] = virtual_machine_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        virtual_machine_id = d.pop("virtualMachineId", UNSET)

        virtual_machine_name = d.pop("virtualMachineName", UNSET)

        public_cloud_azure_virtual_machine = cls(
            virtual_machine_id=virtual_machine_id,
            virtual_machine_name=virtual_machine_name,
        )

        public_cloud_azure_virtual_machine.additional_properties = d
        return public_cloud_azure_virtual_machine

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
