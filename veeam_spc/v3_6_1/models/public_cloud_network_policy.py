from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.backup_server_public_cloud_appliance_management_type import BackupServerPublicCloudApplianceManagementType
from ..models.backup_server_public_cloud_appliance_platform import BackupServerPublicCloudAppliancePlatform
from ..models.public_cloud_network_type_readonly import PublicCloudNetworkTypeReadonly
from ..models.public_cloud_policy_state import PublicCloudPolicyState
from ..models.public_cloud_policy_status import PublicCloudPolicyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_cloud_policy_session import PublicCloudPolicySession


T = TypeVar("T", bound="PublicCloudNetworkPolicy")


@_attrs_define
class PublicCloudNetworkPolicy:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a cloud network policy.
        name (Union[Unset, str]): Name of a cloud network policy.
        appliance_uid (Union[None, UUID, Unset]): UID assigned to a Veeam Backup for Public Clouds appliance.
        status (Union[Unset, PublicCloudPolicyStatus]): Status of a Veeam Backup for Public Clouds policy.
        state (Union[Unset, PublicCloudPolicyState]): State of a Veeam Backup for Public Clouds policy.
        appliance_management_type (Union[Unset, BackupServerPublicCloudApplianceManagementType]): Management type of a
            Veeam Backup for Public Clouds appliance.
        organization_uid (Union[Unset, UUID]): UID assigned to a mapped organization.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
        vnet_type (Union[Unset, PublicCloudNetworkTypeReadonly]): Type of a cloud network included in a policy.
        platform_type (Union[Unset, BackupServerPublicCloudAppliancePlatform]): Platform of a Veeam Backup for Public
            Clouds appliance.
        subscriptions_count (Union[Unset, int]): Number of Microsoft Azure subscriptions.
        regions_count (Union[Unset, int]): Number of regions.
        last_backup (Union[Unset, PublicCloudPolicySession]):
    """

    instance_uid: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    appliance_uid: Union[None, UUID, Unset] = UNSET
    status: Union[Unset, PublicCloudPolicyStatus] = UNSET
    state: Union[Unset, PublicCloudPolicyState] = UNSET
    appliance_management_type: Union[Unset, BackupServerPublicCloudApplianceManagementType] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    vnet_type: Union[Unset, PublicCloudNetworkTypeReadonly] = UNSET
    platform_type: Union[Unset, BackupServerPublicCloudAppliancePlatform] = UNSET
    subscriptions_count: Union[Unset, int] = UNSET
    regions_count: Union[Unset, int] = UNSET
    last_backup: Union[Unset, "PublicCloudPolicySession"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        name = self.name

        appliance_uid: Union[None, Unset, str]
        if isinstance(self.appliance_uid, Unset):
            appliance_uid = UNSET
        elif isinstance(self.appliance_uid, UUID):
            appliance_uid = str(self.appliance_uid)
        else:
            appliance_uid = self.appliance_uid

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        appliance_management_type: Union[Unset, str] = UNSET
        if not isinstance(self.appliance_management_type, Unset):
            appliance_management_type = self.appliance_management_type.value

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        vnet_type: Union[Unset, str] = UNSET
        if not isinstance(self.vnet_type, Unset):
            vnet_type = self.vnet_type.value

        platform_type: Union[Unset, str] = UNSET
        if not isinstance(self.platform_type, Unset):
            platform_type = self.platform_type.value

        subscriptions_count = self.subscriptions_count

        regions_count = self.regions_count

        last_backup: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_backup, Unset):
            last_backup = self.last_backup.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if name is not UNSET:
            field_dict["name"] = name
        if appliance_uid is not UNSET:
            field_dict["applianceUid"] = appliance_uid
        if status is not UNSET:
            field_dict["status"] = status
        if state is not UNSET:
            field_dict["state"] = state
        if appliance_management_type is not UNSET:
            field_dict["applianceManagementType"] = appliance_management_type
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if vnet_type is not UNSET:
            field_dict["vnetType"] = vnet_type
        if platform_type is not UNSET:
            field_dict["platformType"] = platform_type
        if subscriptions_count is not UNSET:
            field_dict["subscriptionsCount"] = subscriptions_count
        if regions_count is not UNSET:
            field_dict["regionsCount"] = regions_count
        if last_backup is not UNSET:
            field_dict["lastBackup"] = last_backup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_cloud_policy_session import PublicCloudPolicySession

        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        name = d.pop("name", UNSET)

        def _parse_appliance_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                appliance_uid_type_0 = UUID(data)

                return appliance_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        appliance_uid = _parse_appliance_uid(d.pop("applianceUid", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, PublicCloudPolicyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PublicCloudPolicyStatus(_status)

        _state = d.pop("state", UNSET)
        state: Union[Unset, PublicCloudPolicyState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PublicCloudPolicyState(_state)

        _appliance_management_type = d.pop("applianceManagementType", UNSET)
        appliance_management_type: Union[Unset, BackupServerPublicCloudApplianceManagementType]
        if isinstance(_appliance_management_type, Unset):
            appliance_management_type = UNSET
        else:
            appliance_management_type = BackupServerPublicCloudApplianceManagementType(_appliance_management_type)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        _vnet_type = d.pop("vnetType", UNSET)
        vnet_type: Union[Unset, PublicCloudNetworkTypeReadonly]
        if isinstance(_vnet_type, Unset):
            vnet_type = UNSET
        else:
            vnet_type = PublicCloudNetworkTypeReadonly(_vnet_type)

        _platform_type = d.pop("platformType", UNSET)
        platform_type: Union[Unset, BackupServerPublicCloudAppliancePlatform]
        if isinstance(_platform_type, Unset):
            platform_type = UNSET
        else:
            platform_type = BackupServerPublicCloudAppliancePlatform(_platform_type)

        subscriptions_count = d.pop("subscriptionsCount", UNSET)

        regions_count = d.pop("regionsCount", UNSET)

        _last_backup = d.pop("lastBackup", UNSET)
        last_backup: Union[Unset, PublicCloudPolicySession]
        if isinstance(_last_backup, Unset):
            last_backup = UNSET
        else:
            last_backup = PublicCloudPolicySession.from_dict(_last_backup)

        public_cloud_network_policy = cls(
            instance_uid=instance_uid,
            name=name,
            appliance_uid=appliance_uid,
            status=status,
            state=state,
            appliance_management_type=appliance_management_type,
            organization_uid=organization_uid,
            backup_server_uid=backup_server_uid,
            vnet_type=vnet_type,
            platform_type=platform_type,
            subscriptions_count=subscriptions_count,
            regions_count=regions_count,
            last_backup=last_backup,
        )

        public_cloud_network_policy.additional_properties = d
        return public_cloud_network_policy

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
