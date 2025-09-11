from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription_plan_backup_and_replication_licenses import SubscriptionPlanBackupAndReplicationLicenses
    from ..models.subscription_plan_cloud_connect_licenses import SubscriptionPlanCloudConnectLicenses
    from ..models.subscription_plan_data_platform_licenses import SubscriptionPlanDataPlatformLicenses
    from ..models.subscription_plan_vb365_licenses import SubscriptionPlanVB365Licenses
    from ..models.subscription_plan_veeam_one_licenses import SubscriptionPlanVeeamOneLicenses
    from ..models.subscription_plan_vspc_licenses import SubscriptionPlanVspcLicenses


T = TypeVar("T", bound="SubscriptionPlanLicenses")


@_attrs_define
class SubscriptionPlanLicenses:
    """
    Attributes:
        vspc_licenses (Union[Unset, SubscriptionPlanVspcLicenses]):
        backup_and_replication_standard_edition_licenses (Union[Unset, SubscriptionPlanBackupAndReplicationLicenses]):
        backup_and_replication_enterprise_edition_licenses (Union[Unset, SubscriptionPlanBackupAndReplicationLicenses]):
        backup_and_replication_enterprise_plus_edition_licenses (Union[Unset,
            SubscriptionPlanBackupAndReplicationLicenses]):
        vdp_foundation_package_licenses (Union[Unset, SubscriptionPlanDataPlatformLicenses]):
        vdp_advanced_package_licenses (Union[Unset, SubscriptionPlanDataPlatformLicenses]):
        vdp_premium_package_licenses (Union[Unset, SubscriptionPlanDataPlatformLicenses]):
        cloud_connect_licenses (Union[Unset, SubscriptionPlanCloudConnectLicenses]):
        vb_365_licenses (Union[Unset, SubscriptionPlanVB365Licenses]):
        veeam_one_licenses (Union[Unset, SubscriptionPlanVeeamOneLicenses]):
    """

    vspc_licenses: Union[Unset, "SubscriptionPlanVspcLicenses"] = UNSET
    backup_and_replication_standard_edition_licenses: Union[Unset, "SubscriptionPlanBackupAndReplicationLicenses"] = (
        UNSET
    )
    backup_and_replication_enterprise_edition_licenses: Union[Unset, "SubscriptionPlanBackupAndReplicationLicenses"] = (
        UNSET
    )
    backup_and_replication_enterprise_plus_edition_licenses: Union[
        Unset, "SubscriptionPlanBackupAndReplicationLicenses"
    ] = UNSET
    vdp_foundation_package_licenses: Union[Unset, "SubscriptionPlanDataPlatformLicenses"] = UNSET
    vdp_advanced_package_licenses: Union[Unset, "SubscriptionPlanDataPlatformLicenses"] = UNSET
    vdp_premium_package_licenses: Union[Unset, "SubscriptionPlanDataPlatformLicenses"] = UNSET
    cloud_connect_licenses: Union[Unset, "SubscriptionPlanCloudConnectLicenses"] = UNSET
    vb_365_licenses: Union[Unset, "SubscriptionPlanVB365Licenses"] = UNSET
    veeam_one_licenses: Union[Unset, "SubscriptionPlanVeeamOneLicenses"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vspc_licenses: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vspc_licenses, Unset):
            vspc_licenses = self.vspc_licenses.to_dict()

        backup_and_replication_standard_edition_licenses: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_and_replication_standard_edition_licenses, Unset):
            backup_and_replication_standard_edition_licenses = (
                self.backup_and_replication_standard_edition_licenses.to_dict()
            )

        backup_and_replication_enterprise_edition_licenses: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_and_replication_enterprise_edition_licenses, Unset):
            backup_and_replication_enterprise_edition_licenses = (
                self.backup_and_replication_enterprise_edition_licenses.to_dict()
            )

        backup_and_replication_enterprise_plus_edition_licenses: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.backup_and_replication_enterprise_plus_edition_licenses, Unset):
            backup_and_replication_enterprise_plus_edition_licenses = (
                self.backup_and_replication_enterprise_plus_edition_licenses.to_dict()
            )

        vdp_foundation_package_licenses: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vdp_foundation_package_licenses, Unset):
            vdp_foundation_package_licenses = self.vdp_foundation_package_licenses.to_dict()

        vdp_advanced_package_licenses: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vdp_advanced_package_licenses, Unset):
            vdp_advanced_package_licenses = self.vdp_advanced_package_licenses.to_dict()

        vdp_premium_package_licenses: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vdp_premium_package_licenses, Unset):
            vdp_premium_package_licenses = self.vdp_premium_package_licenses.to_dict()

        cloud_connect_licenses: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cloud_connect_licenses, Unset):
            cloud_connect_licenses = self.cloud_connect_licenses.to_dict()

        vb_365_licenses: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vb_365_licenses, Unset):
            vb_365_licenses = self.vb_365_licenses.to_dict()

        veeam_one_licenses: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.veeam_one_licenses, Unset):
            veeam_one_licenses = self.veeam_one_licenses.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vspc_licenses is not UNSET:
            field_dict["vspcLicenses"] = vspc_licenses
        if backup_and_replication_standard_edition_licenses is not UNSET:
            field_dict["backupAndReplicationStandardEditionLicenses"] = backup_and_replication_standard_edition_licenses
        if backup_and_replication_enterprise_edition_licenses is not UNSET:
            field_dict["backupAndReplicationEnterpriseEditionLicenses"] = (
                backup_and_replication_enterprise_edition_licenses
            )
        if backup_and_replication_enterprise_plus_edition_licenses is not UNSET:
            field_dict["backupAndReplicationEnterprisePlusEditionLicenses"] = (
                backup_and_replication_enterprise_plus_edition_licenses
            )
        if vdp_foundation_package_licenses is not UNSET:
            field_dict["vdpFoundationPackageLicenses"] = vdp_foundation_package_licenses
        if vdp_advanced_package_licenses is not UNSET:
            field_dict["vdpAdvancedPackageLicenses"] = vdp_advanced_package_licenses
        if vdp_premium_package_licenses is not UNSET:
            field_dict["vdpPremiumPackageLicenses"] = vdp_premium_package_licenses
        if cloud_connect_licenses is not UNSET:
            field_dict["cloudConnectLicenses"] = cloud_connect_licenses
        if vb_365_licenses is not UNSET:
            field_dict["vb365Licenses"] = vb_365_licenses
        if veeam_one_licenses is not UNSET:
            field_dict["veeamOneLicenses"] = veeam_one_licenses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_plan_backup_and_replication_licenses import (
            SubscriptionPlanBackupAndReplicationLicenses,
        )
        from ..models.subscription_plan_cloud_connect_licenses import SubscriptionPlanCloudConnectLicenses
        from ..models.subscription_plan_data_platform_licenses import SubscriptionPlanDataPlatformLicenses
        from ..models.subscription_plan_vb365_licenses import SubscriptionPlanVB365Licenses
        from ..models.subscription_plan_veeam_one_licenses import SubscriptionPlanVeeamOneLicenses
        from ..models.subscription_plan_vspc_licenses import SubscriptionPlanVspcLicenses

        d = dict(src_dict)
        _vspc_licenses = d.pop("vspcLicenses", UNSET)
        vspc_licenses: Union[Unset, SubscriptionPlanVspcLicenses]
        if isinstance(_vspc_licenses, Unset):
            vspc_licenses = UNSET
        else:
            vspc_licenses = SubscriptionPlanVspcLicenses.from_dict(_vspc_licenses)

        _backup_and_replication_standard_edition_licenses = d.pop("backupAndReplicationStandardEditionLicenses", UNSET)
        backup_and_replication_standard_edition_licenses: Union[Unset, SubscriptionPlanBackupAndReplicationLicenses]
        if isinstance(_backup_and_replication_standard_edition_licenses, Unset):
            backup_and_replication_standard_edition_licenses = UNSET
        else:
            backup_and_replication_standard_edition_licenses = SubscriptionPlanBackupAndReplicationLicenses.from_dict(
                _backup_and_replication_standard_edition_licenses
            )

        _backup_and_replication_enterprise_edition_licenses = d.pop(
            "backupAndReplicationEnterpriseEditionLicenses", UNSET
        )
        backup_and_replication_enterprise_edition_licenses: Union[Unset, SubscriptionPlanBackupAndReplicationLicenses]
        if isinstance(_backup_and_replication_enterprise_edition_licenses, Unset):
            backup_and_replication_enterprise_edition_licenses = UNSET
        else:
            backup_and_replication_enterprise_edition_licenses = SubscriptionPlanBackupAndReplicationLicenses.from_dict(
                _backup_and_replication_enterprise_edition_licenses
            )

        _backup_and_replication_enterprise_plus_edition_licenses = d.pop(
            "backupAndReplicationEnterprisePlusEditionLicenses", UNSET
        )
        backup_and_replication_enterprise_plus_edition_licenses: Union[
            Unset, SubscriptionPlanBackupAndReplicationLicenses
        ]
        if isinstance(_backup_and_replication_enterprise_plus_edition_licenses, Unset):
            backup_and_replication_enterprise_plus_edition_licenses = UNSET
        else:
            backup_and_replication_enterprise_plus_edition_licenses = (
                SubscriptionPlanBackupAndReplicationLicenses.from_dict(
                    _backup_and_replication_enterprise_plus_edition_licenses
                )
            )

        _vdp_foundation_package_licenses = d.pop("vdpFoundationPackageLicenses", UNSET)
        vdp_foundation_package_licenses: Union[Unset, SubscriptionPlanDataPlatformLicenses]
        if isinstance(_vdp_foundation_package_licenses, Unset):
            vdp_foundation_package_licenses = UNSET
        else:
            vdp_foundation_package_licenses = SubscriptionPlanDataPlatformLicenses.from_dict(
                _vdp_foundation_package_licenses
            )

        _vdp_advanced_package_licenses = d.pop("vdpAdvancedPackageLicenses", UNSET)
        vdp_advanced_package_licenses: Union[Unset, SubscriptionPlanDataPlatformLicenses]
        if isinstance(_vdp_advanced_package_licenses, Unset):
            vdp_advanced_package_licenses = UNSET
        else:
            vdp_advanced_package_licenses = SubscriptionPlanDataPlatformLicenses.from_dict(
                _vdp_advanced_package_licenses
            )

        _vdp_premium_package_licenses = d.pop("vdpPremiumPackageLicenses", UNSET)
        vdp_premium_package_licenses: Union[Unset, SubscriptionPlanDataPlatformLicenses]
        if isinstance(_vdp_premium_package_licenses, Unset):
            vdp_premium_package_licenses = UNSET
        else:
            vdp_premium_package_licenses = SubscriptionPlanDataPlatformLicenses.from_dict(_vdp_premium_package_licenses)

        _cloud_connect_licenses = d.pop("cloudConnectLicenses", UNSET)
        cloud_connect_licenses: Union[Unset, SubscriptionPlanCloudConnectLicenses]
        if isinstance(_cloud_connect_licenses, Unset):
            cloud_connect_licenses = UNSET
        else:
            cloud_connect_licenses = SubscriptionPlanCloudConnectLicenses.from_dict(_cloud_connect_licenses)

        _vb_365_licenses = d.pop("vb365Licenses", UNSET)
        vb_365_licenses: Union[Unset, SubscriptionPlanVB365Licenses]
        if isinstance(_vb_365_licenses, Unset):
            vb_365_licenses = UNSET
        else:
            vb_365_licenses = SubscriptionPlanVB365Licenses.from_dict(_vb_365_licenses)

        _veeam_one_licenses = d.pop("veeamOneLicenses", UNSET)
        veeam_one_licenses: Union[Unset, SubscriptionPlanVeeamOneLicenses]
        if isinstance(_veeam_one_licenses, Unset):
            veeam_one_licenses = UNSET
        else:
            veeam_one_licenses = SubscriptionPlanVeeamOneLicenses.from_dict(_veeam_one_licenses)

        subscription_plan_licenses = cls(
            vspc_licenses=vspc_licenses,
            backup_and_replication_standard_edition_licenses=backup_and_replication_standard_edition_licenses,
            backup_and_replication_enterprise_edition_licenses=backup_and_replication_enterprise_edition_licenses,
            backup_and_replication_enterprise_plus_edition_licenses=backup_and_replication_enterprise_plus_edition_licenses,
            vdp_foundation_package_licenses=vdp_foundation_package_licenses,
            vdp_advanced_package_licenses=vdp_advanced_package_licenses,
            vdp_premium_package_licenses=vdp_premium_package_licenses,
            cloud_connect_licenses=cloud_connect_licenses,
            vb_365_licenses=vb_365_licenses,
            veeam_one_licenses=veeam_one_licenses,
        )

        subscription_plan_licenses.additional_properties = d
        return subscription_plan_licenses

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
