from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.v_one_deployment_configuration import VOneDeploymentConfiguration
    from ..models.v_one_deployment_license_settings import VOneDeploymentLicenseSettings


T = TypeVar("T", bound="VOneDeploymentConfigurationWithCredentials")


@_attrs_define
class VOneDeploymentConfigurationWithCredentials:
    """
    Attributes:
        configuration (VOneDeploymentConfiguration): Deployment configuration.
            > If the `distribution` and `usePredownloadedIso` properties have the `null` value, the most recent version of
            Veeam ONE will be downloaded automatically.
        license_settings (VOneDeploymentLicenseSettings):
    """

    configuration: "VOneDeploymentConfiguration"
    license_settings: "VOneDeploymentLicenseSettings"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        license_settings = self.license_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "licenseSettings": license_settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v_one_deployment_configuration import VOneDeploymentConfiguration
        from ..models.v_one_deployment_license_settings import VOneDeploymentLicenseSettings

        d = dict(src_dict)
        configuration = VOneDeploymentConfiguration.from_dict(d.pop("configuration"))

        license_settings = VOneDeploymentLicenseSettings.from_dict(d.pop("licenseSettings"))

        v_one_deployment_configuration_with_credentials = cls(
            configuration=configuration,
            license_settings=license_settings,
        )

        v_one_deployment_configuration_with_credentials.additional_properties = d
        return v_one_deployment_configuration_with_credentials

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
