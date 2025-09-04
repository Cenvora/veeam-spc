from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.deploy_schedule import DeploySchedule
    from ..models.vbr_deployment_configuration_with_credentials import VbrDeploymentConfigurationWithCredentials


T = TypeVar("T", bound="VbrScheduledDeploymentConfigurationWithCredentials")


@_attrs_define
class VbrScheduledDeploymentConfigurationWithCredentials:
    """
    Attributes:
        configuration (VbrDeploymentConfigurationWithCredentials):
        schedule (DeploySchedule):
    """

    configuration: "VbrDeploymentConfigurationWithCredentials"
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
        from ..models.vbr_deployment_configuration_with_credentials import VbrDeploymentConfigurationWithCredentials

        d = dict(src_dict)
        configuration = VbrDeploymentConfigurationWithCredentials.from_dict(d.pop("configuration"))

        schedule = DeploySchedule.from_dict(d.pop("schedule"))

        vbr_scheduled_deployment_configuration_with_credentials = cls(
            configuration=configuration,
            schedule=schedule,
        )

        vbr_scheduled_deployment_configuration_with_credentials.additional_properties = d
        return vbr_scheduled_deployment_configuration_with_credentials

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
