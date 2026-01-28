from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reseller_cloud_connect_quota_type_0 import ResellerCloudConnectQuotaType0
    from ..models.reseller_hosted_services import ResellerHostedServices
    from ..models.reseller_remote_services import ResellerRemoteServices


T = TypeVar("T", bound="ResellerServices")


@_attrs_define
class ResellerServices:
    """
    Attributes:
        hosted_services (Union[Unset, ResellerHostedServices]):
        remote_services (Union[Unset, ResellerRemoteServices]):
        cloud_connect_quota (Union['ResellerCloudConnectQuotaType0', None, Unset]): Veeam Cloud Connect resources
            provided to a reseller.
            > If you do not provide the `null` value for this property during reseller creation, you will not be able to
            change it to `null`.
        cloud_connect_management_enabled (Union[Unset, bool]): Indicates whether Veeam Cloud Connect resources are
            available to a reseller.
             Default: False.
        is_file_level_restore_enabled (Union[Unset, bool]): Indicates whether file-level restore is available to
            reseller companies. Default: False.
    """

    hosted_services: Union[Unset, "ResellerHostedServices"] = UNSET
    remote_services: Union[Unset, "ResellerRemoteServices"] = UNSET
    cloud_connect_quota: Union["ResellerCloudConnectQuotaType0", None, Unset] = UNSET
    cloud_connect_management_enabled: Union[Unset, bool] = False
    is_file_level_restore_enabled: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.reseller_cloud_connect_quota_type_0 import ResellerCloudConnectQuotaType0

        hosted_services: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.hosted_services, Unset):
            hosted_services = self.hosted_services.to_dict()

        remote_services: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.remote_services, Unset):
            remote_services = self.remote_services.to_dict()

        cloud_connect_quota: Union[None, Unset, dict[str, Any]]
        if isinstance(self.cloud_connect_quota, Unset):
            cloud_connect_quota = UNSET
        elif isinstance(self.cloud_connect_quota, ResellerCloudConnectQuotaType0):
            cloud_connect_quota = self.cloud_connect_quota.to_dict()
        else:
            cloud_connect_quota = self.cloud_connect_quota

        cloud_connect_management_enabled = self.cloud_connect_management_enabled

        is_file_level_restore_enabled = self.is_file_level_restore_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hosted_services is not UNSET:
            field_dict["hostedServices"] = hosted_services
        if remote_services is not UNSET:
            field_dict["remoteServices"] = remote_services
        if cloud_connect_quota is not UNSET:
            field_dict["cloudConnectQuota"] = cloud_connect_quota
        if cloud_connect_management_enabled is not UNSET:
            field_dict["cloudConnectManagementEnabled"] = cloud_connect_management_enabled
        if is_file_level_restore_enabled is not UNSET:
            field_dict["isFileLevelRestoreEnabled"] = is_file_level_restore_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reseller_cloud_connect_quota_type_0 import ResellerCloudConnectQuotaType0
        from ..models.reseller_hosted_services import ResellerHostedServices
        from ..models.reseller_remote_services import ResellerRemoteServices

        d = dict(src_dict)
        _hosted_services = d.pop("hostedServices", UNSET)
        hosted_services: Union[Unset, ResellerHostedServices]
        if isinstance(_hosted_services, Unset):
            hosted_services = UNSET
        else:
            hosted_services = ResellerHostedServices.from_dict(_hosted_services)

        _remote_services = d.pop("remoteServices", UNSET)
        remote_services: Union[Unset, ResellerRemoteServices]
        if isinstance(_remote_services, Unset):
            remote_services = UNSET
        else:
            remote_services = ResellerRemoteServices.from_dict(_remote_services)

        def _parse_cloud_connect_quota(data: object) -> Union["ResellerCloudConnectQuotaType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_reseller_cloud_connect_quota_type_0 = ResellerCloudConnectQuotaType0.from_dict(data)

                return componentsschemas_reseller_cloud_connect_quota_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ResellerCloudConnectQuotaType0", None, Unset], data)

        cloud_connect_quota = _parse_cloud_connect_quota(d.pop("cloudConnectQuota", UNSET))

        cloud_connect_management_enabled = d.pop("cloudConnectManagementEnabled", UNSET)

        is_file_level_restore_enabled = d.pop("isFileLevelRestoreEnabled", UNSET)

        reseller_services = cls(
            hosted_services=hosted_services,
            remote_services=remote_services,
            cloud_connect_quota=cloud_connect_quota,
            cloud_connect_management_enabled=cloud_connect_management_enabled,
            is_file_level_restore_enabled=is_file_level_restore_enabled,
        )

        reseller_services.additional_properties = d
        return reseller_services

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
