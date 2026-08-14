from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription_plan_repository_label_charge import SubscriptionPlanRepositoryLabelCharge


T = TypeVar("T", bound="SubscriptionPlanRepositoryUsageByLabel")


@_attrs_define
class SubscriptionPlanRepositoryUsageByLabel:
    """
    Attributes:
        hosted (list[SubscriptionPlanRepositoryLabelCharge] | Unset): Array of dynamic hosted repository pricing
            configurations, each bound to a repository label.
        remote (list[SubscriptionPlanRepositoryLabelCharge] | Unset): Array of dynamic remote repository pricing
            configurations, each bound to a repository label.
    """

    hosted: list[SubscriptionPlanRepositoryLabelCharge] | Unset = UNSET
    remote: list[SubscriptionPlanRepositoryLabelCharge] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hosted: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hosted, Unset):
            hosted = []
            for hosted_item_data in self.hosted:
                hosted_item = hosted_item_data.to_dict()
                hosted.append(hosted_item)

        remote: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.remote, Unset):
            remote = []
            for remote_item_data in self.remote:
                remote_item = remote_item_data.to_dict()
                remote.append(remote_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hosted is not UNSET:
            field_dict["hosted"] = hosted
        if remote is not UNSET:
            field_dict["remote"] = remote

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_plan_repository_label_charge import SubscriptionPlanRepositoryLabelCharge

        d = dict(src_dict)
        _hosted = d.pop("hosted", UNSET)
        hosted: list[SubscriptionPlanRepositoryLabelCharge] | Unset = UNSET
        if _hosted is not UNSET:
            hosted = []
            for hosted_item_data in _hosted:
                hosted_item = SubscriptionPlanRepositoryLabelCharge.from_dict(hosted_item_data)

                hosted.append(hosted_item)

        _remote = d.pop("remote", UNSET)
        remote: list[SubscriptionPlanRepositoryLabelCharge] | Unset = UNSET
        if _remote is not UNSET:
            remote = []
            for remote_item_data in _remote:
                remote_item = SubscriptionPlanRepositoryLabelCharge.from_dict(remote_item_data)

                remote.append(remote_item)

        subscription_plan_repository_usage_by_label = cls(
            hosted=hosted,
            remote=remote,
        )

        subscription_plan_repository_usage_by_label.additional_properties = d
        return subscription_plan_repository_usage_by_label

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
