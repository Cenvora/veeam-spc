from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.paging_information import PagingInformation


T = TypeVar("T", bound="ResponseMetadataType0")


@_attrs_define
class ResponseMetadataType0:
    """
    Attributes:
        paging_info (Union[Unset, PagingInformation]): Pagination data.
    """

    paging_info: Union[Unset, "PagingInformation"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        paging_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.paging_info, Unset):
            paging_info = self.paging_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paging_info is not UNSET:
            field_dict["pagingInfo"] = paging_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paging_information import PagingInformation

        d = dict(src_dict)
        _paging_info = d.pop("pagingInfo", UNSET)
        paging_info: Union[Unset, PagingInformation]
        if isinstance(_paging_info, Unset):
            paging_info = UNSET
        else:
            paging_info = PagingInformation.from_dict(_paging_info)

        response_metadata_type_0 = cls(
            paging_info=paging_info,
        )

        response_metadata_type_0.additional_properties = d
        return response_metadata_type_0

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
