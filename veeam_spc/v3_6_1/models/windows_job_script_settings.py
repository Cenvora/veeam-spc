from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.windows_job_script_settings_mode import WindowsJobScriptSettingsMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.windows_job_script import WindowsJobScript
    from ..models.windows_job_script_execution_account import WindowsJobScriptExecutionAccount


T = TypeVar("T", bound="WindowsJobScriptSettings")


@_attrs_define
class WindowsJobScriptSettings:
    """
    Attributes:
        mode (Union[Unset, WindowsJobScriptSettingsMode]): Script processing mode. Default:
            WindowsJobScriptSettingsMode.DISABLED.
        pre_freeze_script (Union[Unset, WindowsJobScript]):
        post_thaw_script (Union[Unset, WindowsJobScript]):
        credentials (Union[Unset, WindowsJobScriptExecutionAccount]):
    """

    mode: Union[Unset, WindowsJobScriptSettingsMode] = WindowsJobScriptSettingsMode.DISABLED
    pre_freeze_script: Union[Unset, "WindowsJobScript"] = UNSET
    post_thaw_script: Union[Unset, "WindowsJobScript"] = UNSET
    credentials: Union[Unset, "WindowsJobScriptExecutionAccount"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        pre_freeze_script: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pre_freeze_script, Unset):
            pre_freeze_script = self.pre_freeze_script.to_dict()

        post_thaw_script: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.post_thaw_script, Unset):
            post_thaw_script = self.post_thaw_script.to_dict()

        credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if pre_freeze_script is not UNSET:
            field_dict["preFreezeScript"] = pre_freeze_script
        if post_thaw_script is not UNSET:
            field_dict["postThawScript"] = post_thaw_script
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.windows_job_script import WindowsJobScript
        from ..models.windows_job_script_execution_account import WindowsJobScriptExecutionAccount

        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, WindowsJobScriptSettingsMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = WindowsJobScriptSettingsMode(_mode)

        _pre_freeze_script = d.pop("preFreezeScript", UNSET)
        pre_freeze_script: Union[Unset, WindowsJobScript]
        if isinstance(_pre_freeze_script, Unset):
            pre_freeze_script = UNSET
        else:
            pre_freeze_script = WindowsJobScript.from_dict(_pre_freeze_script)

        _post_thaw_script = d.pop("postThawScript", UNSET)
        post_thaw_script: Union[Unset, WindowsJobScript]
        if isinstance(_post_thaw_script, Unset):
            post_thaw_script = UNSET
        else:
            post_thaw_script = WindowsJobScript.from_dict(_post_thaw_script)

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, WindowsJobScriptExecutionAccount]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = WindowsJobScriptExecutionAccount.from_dict(_credentials)

        windows_job_script_settings = cls(
            mode=mode,
            pre_freeze_script=pre_freeze_script,
            post_thaw_script=post_thaw_script,
            credentials=credentials,
        )

        windows_job_script_settings.additional_properties = d
        return windows_job_script_settings

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
