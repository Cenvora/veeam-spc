from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linux_job_script import LinuxJobScript


T = TypeVar("T", bound="LinuxJobScriptSettings")


@_attrs_define
class LinuxJobScriptSettings:
    """
    Attributes:
        enabled (Union[Unset, bool]): Indicates whether script processing is enabled. Default: False.
        pre_job_script (Union[Unset, LinuxJobScript]):
        post_job_script (Union[Unset, LinuxJobScript]):
        pre_freeze_script (Union[Unset, LinuxJobScript]):
        post_thaw_script (Union[Unset, LinuxJobScript]):
    """

    enabled: Union[Unset, bool] = False
    pre_job_script: Union[Unset, "LinuxJobScript"] = UNSET
    post_job_script: Union[Unset, "LinuxJobScript"] = UNSET
    pre_freeze_script: Union[Unset, "LinuxJobScript"] = UNSET
    post_thaw_script: Union[Unset, "LinuxJobScript"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        pre_job_script: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pre_job_script, Unset):
            pre_job_script = self.pre_job_script.to_dict()

        post_job_script: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.post_job_script, Unset):
            post_job_script = self.post_job_script.to_dict()

        pre_freeze_script: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pre_freeze_script, Unset):
            pre_freeze_script = self.pre_freeze_script.to_dict()

        post_thaw_script: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.post_thaw_script, Unset):
            post_thaw_script = self.post_thaw_script.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if pre_job_script is not UNSET:
            field_dict["preJobScript"] = pre_job_script
        if post_job_script is not UNSET:
            field_dict["postJobScript"] = post_job_script
        if pre_freeze_script is not UNSET:
            field_dict["preFreezeScript"] = pre_freeze_script
        if post_thaw_script is not UNSET:
            field_dict["postThawScript"] = post_thaw_script

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linux_job_script import LinuxJobScript

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _pre_job_script = d.pop("preJobScript", UNSET)
        pre_job_script: Union[Unset, LinuxJobScript]
        if isinstance(_pre_job_script, Unset):
            pre_job_script = UNSET
        else:
            pre_job_script = LinuxJobScript.from_dict(_pre_job_script)

        _post_job_script = d.pop("postJobScript", UNSET)
        post_job_script: Union[Unset, LinuxJobScript]
        if isinstance(_post_job_script, Unset):
            post_job_script = UNSET
        else:
            post_job_script = LinuxJobScript.from_dict(_post_job_script)

        _pre_freeze_script = d.pop("preFreezeScript", UNSET)
        pre_freeze_script: Union[Unset, LinuxJobScript]
        if isinstance(_pre_freeze_script, Unset):
            pre_freeze_script = UNSET
        else:
            pre_freeze_script = LinuxJobScript.from_dict(_pre_freeze_script)

        _post_thaw_script = d.pop("postThawScript", UNSET)
        post_thaw_script: Union[Unset, LinuxJobScript]
        if isinstance(_post_thaw_script, Unset):
            post_thaw_script = UNSET
        else:
            post_thaw_script = LinuxJobScript.from_dict(_post_thaw_script)

        linux_job_script_settings = cls(
            enabled=enabled,
            pre_job_script=pre_job_script,
            post_job_script=post_job_script,
            pre_freeze_script=pre_freeze_script,
            post_thaw_script=post_thaw_script,
        )

        linux_job_script_settings.additional_properties = d
        return linux_job_script_settings

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
