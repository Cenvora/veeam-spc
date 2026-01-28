from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_script_periodicity_type import BackupServerScriptPeriodicityType
from ..models.days_of_week import DaysOfWeek
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_script_command import BackupServerScriptCommand


T = TypeVar("T", bound="BackupServerJobScriptsSettingsType0")


@_attrs_define
class BackupServerJobScriptsSettingsType0:
    """Script settings.

    Attributes:
        pre_command (Union[Unset, BackupServerScriptCommand]):
        post_command (Union[Unset, BackupServerScriptCommand]):
        periodicity_type (Union[Unset, BackupServerScriptPeriodicityType]): Type of script execution periodicity.
        run_script_every (Union[None, Unset, int]): Number of backup job sessions after which the scripts must be
            executed.
        day_of_week (Union[None, Unset, list[DaysOfWeek]]): Days of the week when the scripts must be executed.
    """

    pre_command: Union[Unset, "BackupServerScriptCommand"] = UNSET
    post_command: Union[Unset, "BackupServerScriptCommand"] = UNSET
    periodicity_type: Union[Unset, BackupServerScriptPeriodicityType] = UNSET
    run_script_every: Union[None, Unset, int] = UNSET
    day_of_week: Union[None, Unset, list[DaysOfWeek]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pre_command: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pre_command, Unset):
            pre_command = self.pre_command.to_dict()

        post_command: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.post_command, Unset):
            post_command = self.post_command.to_dict()

        periodicity_type: Union[Unset, str] = UNSET
        if not isinstance(self.periodicity_type, Unset):
            periodicity_type = self.periodicity_type.value

        run_script_every: Union[None, Unset, int]
        if isinstance(self.run_script_every, Unset):
            run_script_every = UNSET
        else:
            run_script_every = self.run_script_every

        day_of_week: Union[None, Unset, list[str]]
        if isinstance(self.day_of_week, Unset):
            day_of_week = UNSET
        elif isinstance(self.day_of_week, list):
            day_of_week = []
            for day_of_week_type_0_item_data in self.day_of_week:
                day_of_week_type_0_item = day_of_week_type_0_item_data.value
                day_of_week.append(day_of_week_type_0_item)

        else:
            day_of_week = self.day_of_week

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pre_command is not UNSET:
            field_dict["preCommand"] = pre_command
        if post_command is not UNSET:
            field_dict["postCommand"] = post_command
        if periodicity_type is not UNSET:
            field_dict["periodicityType"] = periodicity_type
        if run_script_every is not UNSET:
            field_dict["runScriptEvery"] = run_script_every
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_script_command import BackupServerScriptCommand

        d = dict(src_dict)
        _pre_command = d.pop("preCommand", UNSET)
        pre_command: Union[Unset, BackupServerScriptCommand]
        if isinstance(_pre_command, Unset):
            pre_command = UNSET
        else:
            pre_command = BackupServerScriptCommand.from_dict(_pre_command)

        _post_command = d.pop("postCommand", UNSET)
        post_command: Union[Unset, BackupServerScriptCommand]
        if isinstance(_post_command, Unset):
            post_command = UNSET
        else:
            post_command = BackupServerScriptCommand.from_dict(_post_command)

        _periodicity_type = d.pop("periodicityType", UNSET)
        periodicity_type: Union[Unset, BackupServerScriptPeriodicityType]
        if isinstance(_periodicity_type, Unset):
            periodicity_type = UNSET
        else:
            periodicity_type = BackupServerScriptPeriodicityType(_periodicity_type)

        def _parse_run_script_every(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        run_script_every = _parse_run_script_every(d.pop("runScriptEvery", UNSET))

        def _parse_day_of_week(data: object) -> Union[None, Unset, list[DaysOfWeek]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                day_of_week_type_0 = []
                _day_of_week_type_0 = data
                for day_of_week_type_0_item_data in _day_of_week_type_0:
                    day_of_week_type_0_item = DaysOfWeek(day_of_week_type_0_item_data)

                    day_of_week_type_0.append(day_of_week_type_0_item)

                return day_of_week_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[DaysOfWeek]], data)

        day_of_week = _parse_day_of_week(d.pop("dayOfWeek", UNSET))

        backup_server_job_scripts_settings_type_0 = cls(
            pre_command=pre_command,
            post_command=post_command,
            periodicity_type=periodicity_type,
            run_script_every=run_script_every,
            day_of_week=day_of_week,
        )

        backup_server_job_scripts_settings_type_0.additional_properties = d
        return backup_server_job_scripts_settings_type_0

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
