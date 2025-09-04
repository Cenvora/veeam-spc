from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.deploy_schedule import DeploySchedule
    from ..models.vbr_patch_configuration import VbrPatchConfiguration


T = TypeVar("T", bound="VbrScheduledPatchConfiguration")


@_attrs_define
class VbrScheduledPatchConfiguration:
    """
    Attributes:
        configuration (VbrPatchConfiguration):
        schedule (DeploySchedule):
    """

    configuration: "VbrPatchConfiguration"
    schedule: "DeploySchedule"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        schedule = self.schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "schedule": schedule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deploy_schedule import DeploySchedule
        from ..models.vbr_patch_configuration import VbrPatchConfiguration

        d = dict(src_dict)
        configuration = VbrPatchConfiguration.from_dict(d.pop("configuration"))

        schedule = DeploySchedule.from_dict(d.pop("schedule"))

        vbr_scheduled_patch_configuration = cls(
            configuration=configuration,
            schedule=schedule,
        )

        vbr_scheduled_patch_configuration.additional_properties = d
        return vbr_scheduled_patch_configuration

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
