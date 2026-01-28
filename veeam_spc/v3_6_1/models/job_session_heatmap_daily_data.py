import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_session_heatmap_session import JobSessionHeatmapSession


T = TypeVar("T", bound="JobSessionHeatmapDailyData")


@_attrs_define
class JobSessionHeatmapDailyData:
    """
    Attributes:
        date (Union[Unset, datetime.date]): Date.
        sessions (Union[None, Unset, list['JobSessionHeatmapSession']]): Array of job sessions.
    """

    date: Union[Unset, datetime.date] = UNSET
    sessions: Union[None, Unset, list["JobSessionHeatmapSession"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        sessions: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.sessions, Unset):
            sessions = UNSET
        elif isinstance(self.sessions, list):
            sessions = []
            for sessions_type_0_item_data in self.sessions:
                sessions_type_0_item = sessions_type_0_item_data.to_dict()
                sessions.append(sessions_type_0_item)

        else:
            sessions = self.sessions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if sessions is not UNSET:
            field_dict["sessions"] = sessions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_session_heatmap_session import JobSessionHeatmapSession

        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        def _parse_sessions(data: object) -> Union[None, Unset, list["JobSessionHeatmapSession"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sessions_type_0 = []
                _sessions_type_0 = data
                for sessions_type_0_item_data in _sessions_type_0:
                    sessions_type_0_item = JobSessionHeatmapSession.from_dict(sessions_type_0_item_data)

                    sessions_type_0.append(sessions_type_0_item)

                return sessions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["JobSessionHeatmapSession"]], data)

        sessions = _parse_sessions(d.pop("sessions", UNSET))

        job_session_heatmap_daily_data = cls(
            date=date,
            sessions=sessions,
        )

        job_session_heatmap_daily_data.additional_properties = d
        return job_session_heatmap_daily_data

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
