from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_session_heatmap_daily_data import JobSessionHeatmapDailyData


T = TypeVar("T", bound="JobSessionHeatmap")


@_attrs_define
class JobSessionHeatmap:
    """
    Attributes:
        success_jobs_count (Union[Unset, int]): Number of successful job sessions.
        warning_jobs_count (Union[Unset, int]): Number of job sessions that ended with warnings.
        fail_jobs_count (Union[Unset, int]): Number of failed job sessions.
        data_per_days (Union[None, Unset, list['JobSessionHeatmapDailyData']]): Detailed information on job sessions on
            each day.
    """

    success_jobs_count: Union[Unset, int] = UNSET
    warning_jobs_count: Union[Unset, int] = UNSET
    fail_jobs_count: Union[Unset, int] = UNSET
    data_per_days: Union[None, Unset, list["JobSessionHeatmapDailyData"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success_jobs_count = self.success_jobs_count

        warning_jobs_count = self.warning_jobs_count

        fail_jobs_count = self.fail_jobs_count

        data_per_days: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.data_per_days, Unset):
            data_per_days = UNSET
        elif isinstance(self.data_per_days, list):
            data_per_days = []
            for data_per_days_type_0_item_data in self.data_per_days:
                data_per_days_type_0_item = data_per_days_type_0_item_data.to_dict()
                data_per_days.append(data_per_days_type_0_item)

        else:
            data_per_days = self.data_per_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success_jobs_count is not UNSET:
            field_dict["successJobsCount"] = success_jobs_count
        if warning_jobs_count is not UNSET:
            field_dict["warningJobsCount"] = warning_jobs_count
        if fail_jobs_count is not UNSET:
            field_dict["failJobsCount"] = fail_jobs_count
        if data_per_days is not UNSET:
            field_dict["dataPerDays"] = data_per_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_session_heatmap_daily_data import JobSessionHeatmapDailyData

        d = dict(src_dict)
        success_jobs_count = d.pop("successJobsCount", UNSET)

        warning_jobs_count = d.pop("warningJobsCount", UNSET)

        fail_jobs_count = d.pop("failJobsCount", UNSET)

        def _parse_data_per_days(data: object) -> Union[None, Unset, list["JobSessionHeatmapDailyData"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_per_days_type_0 = []
                _data_per_days_type_0 = data
                for data_per_days_type_0_item_data in _data_per_days_type_0:
                    data_per_days_type_0_item = JobSessionHeatmapDailyData.from_dict(data_per_days_type_0_item_data)

                    data_per_days_type_0.append(data_per_days_type_0_item)

                return data_per_days_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["JobSessionHeatmapDailyData"]], data)

        data_per_days = _parse_data_per_days(d.pop("dataPerDays", UNSET))

        job_session_heatmap = cls(
            success_jobs_count=success_jobs_count,
            warning_jobs_count=warning_jobs_count,
            fail_jobs_count=fail_jobs_count,
            data_per_days=data_per_days,
        )

        job_session_heatmap.additional_properties = d
        return job_session_heatmap

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
