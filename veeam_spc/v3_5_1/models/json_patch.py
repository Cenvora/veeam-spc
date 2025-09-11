from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.json_patch_op import JsonPatchOp
from ..types import UNSET, Unset

T = TypeVar("T", bound="JsonPatch")


@_attrs_define
class JsonPatch:
    """
    Attributes:
        op (JsonPatchOp): Performed operation.
        value (str): Value that is added, replaced, tested or removed by the PATCH operation.
        path (str): JSON Pointer containing path to a target location where the PATCH operation is performed.
        from_ (Union[Unset, str]): JSON Pointer containing path to a location from which data is moved or copied.
    """

    op: JsonPatchOp
    value: str
    path: str
    from_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        op = self.op.value

        value = self.value

        path = self.path

        from_ = self.from_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "op": op,
                "value": value,
                "path": path,
            }
        )
        if from_ is not UNSET:
            field_dict["from"] = from_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        op = JsonPatchOp(d.pop("op"))

        value = d.pop("value")

        path = d.pop("path")

        from_ = d.pop("from", UNSET)

        json_patch = cls(
            op=op,
            value=value,
            path=path,
            from_=from_,
        )

        json_patch.additional_properties = d
        return json_patch

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
