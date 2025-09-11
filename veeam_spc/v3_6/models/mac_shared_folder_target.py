from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mac_common_credentials import MacCommonCredentials


T = TypeVar("T", bound="MacSharedFolderTarget")


@_attrs_define
class MacSharedFolderTarget:
    """
    Attributes:
        path (str): Path to a network shared folder.
        credentials (Union[Unset, MacCommonCredentials]):
    """

    path: str
    credentials: Union[Unset, "MacCommonCredentials"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mac_common_credentials import MacCommonCredentials

        d = dict(src_dict)
        path = d.pop("path")

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, MacCommonCredentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = MacCommonCredentials.from_dict(_credentials)

        mac_shared_folder_target = cls(
            path=path,
            credentials=credentials,
        )

        mac_shared_folder_target.additional_properties = d
        return mac_shared_folder_target

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
