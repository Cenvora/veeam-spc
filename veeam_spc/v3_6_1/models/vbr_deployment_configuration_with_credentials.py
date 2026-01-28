from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vbr_deployment_configuration import VbrDeploymentConfiguration
    from ..models.vbr_deployment_credentials import VbrDeploymentCredentials
    from ..models.vbr_deployment_license_settings import VbrDeploymentLicenseSettings


T = TypeVar("T", bound="VbrDeploymentConfigurationWithCredentials")


@_attrs_define
class VbrDeploymentConfigurationWithCredentials:
    """
    Attributes:
        configuration (VbrDeploymentConfiguration): If the `distribution` and `usePredownloadedIso` properties have the
            `null` value, the most recent version of Veeam Backup & Replication will be downloaded automatically.
        license_settings (VbrDeploymentLicenseSettings):
        credentials (Union[Unset, VbrDeploymentCredentials]):
    """

    configuration: "VbrDeploymentConfiguration"
    license_settings: "VbrDeploymentLicenseSettings"
    credentials: Union[Unset, "VbrDeploymentCredentials"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        license_settings = self.license_settings.to_dict()

        credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "licenseSettings": license_settings,
            }
        )
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vbr_deployment_configuration import VbrDeploymentConfiguration
        from ..models.vbr_deployment_credentials import VbrDeploymentCredentials
        from ..models.vbr_deployment_license_settings import VbrDeploymentLicenseSettings

        d = dict(src_dict)
        configuration = VbrDeploymentConfiguration.from_dict(d.pop("configuration"))

        license_settings = VbrDeploymentLicenseSettings.from_dict(d.pop("licenseSettings"))

        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, VbrDeploymentCredentials]
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = VbrDeploymentCredentials.from_dict(_credentials)

        vbr_deployment_configuration_with_credentials = cls(
            configuration=configuration,
            license_settings=license_settings,
            credentials=credentials,
        )

        vbr_deployment_configuration_with_credentials.additional_properties = d
        return vbr_deployment_configuration_with_credentials

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
