from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.management_agent_credentials import ManagementAgentCredentials
    from ..models.vbr_deployment_distribution_source import VbrDeploymentDistributionSource


T = TypeVar("T", bound="VbrDeploymentConfiguration")


@_attrs_define
class VbrDeploymentConfiguration:
    """If the `distribution` and `usePredownloadedIso` properties have the `null` value, the most recent version of Veeam
    Backup & Replication will be downloaded automatically.

        Attributes:
            answer_xml (str): XML string containing installation parameters.
                > To obtain a template of XML string, perform the `GetBackupServerDeploymentConfigurationXml` operation.
            distribution (Union[Unset, VbrDeploymentDistributionSource]):
            use_predownloaded_iso (Union[None, Unset, bool]): Indicates whether the predownloaded Veeam Backup & Replication
                setup file is used for installation.
                > Provided value has higher priority than the `distribution` property value.
            allow_auto_reboot (Union[None, Unset, bool]): Indicates whether a server must be automatically rebooted after
                the installation is complete.
            stop_all_activities (Union[None, Unset, bool]): Indicates whether all other tasks must be stopped during
                installation. Can be enabled only for update installation.
            use_management_agent_credentials (Union[None, Unset, bool]): Indicates whether management agent credentials must
                be used as service account credentials.
                > Provided value has higher priority than the `adminCredentials` property value.
            admin_credentials (Union[Unset, ManagementAgentCredentials]):
    """

    answer_xml: str
    distribution: Union[Unset, "VbrDeploymentDistributionSource"] = UNSET
    use_predownloaded_iso: Union[None, Unset, bool] = UNSET
    allow_auto_reboot: Union[None, Unset, bool] = UNSET
    stop_all_activities: Union[None, Unset, bool] = UNSET
    use_management_agent_credentials: Union[None, Unset, bool] = UNSET
    admin_credentials: Union[Unset, "ManagementAgentCredentials"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        answer_xml = self.answer_xml

        distribution: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.distribution, Unset):
            distribution = self.distribution.to_dict()

        use_predownloaded_iso: Union[None, Unset, bool]
        if isinstance(self.use_predownloaded_iso, Unset):
            use_predownloaded_iso = UNSET
        else:
            use_predownloaded_iso = self.use_predownloaded_iso

        allow_auto_reboot: Union[None, Unset, bool]
        if isinstance(self.allow_auto_reboot, Unset):
            allow_auto_reboot = UNSET
        else:
            allow_auto_reboot = self.allow_auto_reboot

        stop_all_activities: Union[None, Unset, bool]
        if isinstance(self.stop_all_activities, Unset):
            stop_all_activities = UNSET
        else:
            stop_all_activities = self.stop_all_activities

        use_management_agent_credentials: Union[None, Unset, bool]
        if isinstance(self.use_management_agent_credentials, Unset):
            use_management_agent_credentials = UNSET
        else:
            use_management_agent_credentials = self.use_management_agent_credentials

        admin_credentials: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.admin_credentials, Unset):
            admin_credentials = self.admin_credentials.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "answerXml": answer_xml,
            }
        )
        if distribution is not UNSET:
            field_dict["distribution"] = distribution
        if use_predownloaded_iso is not UNSET:
            field_dict["usePredownloadedIso"] = use_predownloaded_iso
        if allow_auto_reboot is not UNSET:
            field_dict["allowAutoReboot"] = allow_auto_reboot
        if stop_all_activities is not UNSET:
            field_dict["stopAllActivities"] = stop_all_activities
        if use_management_agent_credentials is not UNSET:
            field_dict["useManagementAgentCredentials"] = use_management_agent_credentials
        if admin_credentials is not UNSET:
            field_dict["adminCredentials"] = admin_credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.management_agent_credentials import ManagementAgentCredentials
        from ..models.vbr_deployment_distribution_source import VbrDeploymentDistributionSource

        d = dict(src_dict)
        answer_xml = d.pop("answerXml")

        _distribution = d.pop("distribution", UNSET)
        distribution: Union[Unset, VbrDeploymentDistributionSource]
        if isinstance(_distribution, Unset):
            distribution = UNSET
        else:
            distribution = VbrDeploymentDistributionSource.from_dict(_distribution)

        def _parse_use_predownloaded_iso(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        use_predownloaded_iso = _parse_use_predownloaded_iso(d.pop("usePredownloadedIso", UNSET))

        def _parse_allow_auto_reboot(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        allow_auto_reboot = _parse_allow_auto_reboot(d.pop("allowAutoReboot", UNSET))

        def _parse_stop_all_activities(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        stop_all_activities = _parse_stop_all_activities(d.pop("stopAllActivities", UNSET))

        def _parse_use_management_agent_credentials(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        use_management_agent_credentials = _parse_use_management_agent_credentials(
            d.pop("useManagementAgentCredentials", UNSET)
        )

        _admin_credentials = d.pop("adminCredentials", UNSET)
        admin_credentials: Union[Unset, ManagementAgentCredentials]
        if isinstance(_admin_credentials, Unset):
            admin_credentials = UNSET
        else:
            admin_credentials = ManagementAgentCredentials.from_dict(_admin_credentials)

        vbr_deployment_configuration = cls(
            answer_xml=answer_xml,
            distribution=distribution,
            use_predownloaded_iso=use_predownloaded_iso,
            allow_auto_reboot=allow_auto_reboot,
            stop_all_activities=stop_all_activities,
            use_management_agent_credentials=use_management_agent_credentials,
            admin_credentials=admin_credentials,
        )

        vbr_deployment_configuration.additional_properties = d
        return vbr_deployment_configuration

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
