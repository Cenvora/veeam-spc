from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedOnPremisesFileShareSource")


@_attrs_define
class ProtectedOnPremisesFileShareSource:
    """
    Attributes:
        path (Union[Unset, str]): Path to a location of protected data.
        inclusion_masks (Union[Unset, list[str]]): Names and name masks of files that must be included into a backup
            scope.
        exclusion_masks (Union[Unset, list[str]]): Names and name masks of files that must be excluded from a backup
            scope.
    """

    path: Union[Unset, str] = UNSET
    inclusion_masks: Union[Unset, list[str]] = UNSET
    exclusion_masks: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        inclusion_masks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.inclusion_masks, Unset):
            inclusion_masks = self.inclusion_masks

        exclusion_masks: Union[Unset, list[str]] = UNSET
        if not isinstance(self.exclusion_masks, Unset):
            exclusion_masks = self.exclusion_masks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if inclusion_masks is not UNSET:
            field_dict["inclusionMasks"] = inclusion_masks
        if exclusion_masks is not UNSET:
            field_dict["exclusionMasks"] = exclusion_masks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path", UNSET)

        inclusion_masks = cast(list[str], d.pop("inclusionMasks", UNSET))

        exclusion_masks = cast(list[str], d.pop("exclusionMasks", UNSET))

        protected_on_premises_file_share_source = cls(
            path=path,
            inclusion_masks=inclusion_masks,
            exclusion_masks=exclusion_masks,
        )

        protected_on_premises_file_share_source.additional_properties = d
        return protected_on_premises_file_share_source

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
