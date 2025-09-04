from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.public_cloud_file_share_type import PublicCloudFileShareType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_cloud_policy_session import PublicCloudPolicySession


T = TypeVar("T", bound="PublicCloudFileSharePolicyObject")


@_attrs_define
class PublicCloudFileSharePolicyObject:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to cloud file share.
        instance_name (Union[Unset, str]): Name of a cloud file share.
        policy_uid (Union[Unset, UUID]): UID assigned to a cloud file share policy.
        policy_name (Union[Unset, str]): Name of a cloud file share policy.
        backup_server_uid (Union[Unset, UUID]): UID assigned to a Veeam Backup & Replication server.
        resource_id (Union[Unset, str]): Resource ID of a cloud file share policy.
        last_snapshot (Union[Unset, PublicCloudPolicySession]):
        last_replica_snapshot (Union[Unset, PublicCloudPolicySession]):
        file_share_type (Union[Unset, PublicCloudFileShareType]): Public cloud fileshare type.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    instance_name: Union[Unset, str] = UNSET
    policy_uid: Union[Unset, UUID] = UNSET
    policy_name: Union[Unset, str] = UNSET
    backup_server_uid: Union[Unset, UUID] = UNSET
    resource_id: Union[Unset, str] = UNSET
    last_snapshot: Union[Unset, "PublicCloudPolicySession"] = UNSET
    last_replica_snapshot: Union[Unset, "PublicCloudPolicySession"] = UNSET
    file_share_type: Union[Unset, PublicCloudFileShareType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        instance_name = self.instance_name

        policy_uid: Union[Unset, str] = UNSET
        if not isinstance(self.policy_uid, Unset):
            policy_uid = str(self.policy_uid)

        policy_name = self.policy_name

        backup_server_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_server_uid, Unset):
            backup_server_uid = str(self.backup_server_uid)

        resource_id = self.resource_id

        last_snapshot: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_snapshot, Unset):
            last_snapshot = self.last_snapshot.to_dict()

        last_replica_snapshot: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_replica_snapshot, Unset):
            last_replica_snapshot = self.last_replica_snapshot.to_dict()

        file_share_type: Union[Unset, str] = UNSET
        if not isinstance(self.file_share_type, Unset):
            file_share_type = self.file_share_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if instance_name is not UNSET:
            field_dict["instanceName"] = instance_name
        if policy_uid is not UNSET:
            field_dict["policyUid"] = policy_uid
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if backup_server_uid is not UNSET:
            field_dict["backupServerUid"] = backup_server_uid
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if last_snapshot is not UNSET:
            field_dict["lastSnapshot"] = last_snapshot
        if last_replica_snapshot is not UNSET:
            field_dict["lastReplicaSnapshot"] = last_replica_snapshot
        if file_share_type is not UNSET:
            field_dict["fileShareType"] = file_share_type

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

        instance_name = d.pop("instanceName", UNSET)

        _policy_uid = d.pop("policyUid", UNSET)
        policy_uid: Union[Unset, UUID]
        if isinstance(_policy_uid, Unset):
            policy_uid = UNSET
        else:
            policy_uid = UUID(_policy_uid)

        policy_name = d.pop("policyName", UNSET)

        _backup_server_uid = d.pop("backupServerUid", UNSET)
        backup_server_uid: Union[Unset, UUID]
        if isinstance(_backup_server_uid, Unset):
            backup_server_uid = UNSET
        else:
            backup_server_uid = UUID(_backup_server_uid)

        resource_id = d.pop("resourceId", UNSET)

        _last_snapshot = d.pop("lastSnapshot", UNSET)
        last_snapshot: Union[Unset, PublicCloudPolicySession]
        if isinstance(_last_snapshot, Unset):
            last_snapshot = UNSET
        else:
            last_snapshot = PublicCloudPolicySession.from_dict(_last_snapshot)

        _last_replica_snapshot = d.pop("lastReplicaSnapshot", UNSET)
        last_replica_snapshot: Union[Unset, PublicCloudPolicySession]
        if isinstance(_last_replica_snapshot, Unset):
            last_replica_snapshot = UNSET
        else:
            last_replica_snapshot = PublicCloudPolicySession.from_dict(_last_replica_snapshot)

        _file_share_type = d.pop("fileShareType", UNSET)
        file_share_type: Union[Unset, PublicCloudFileShareType]
        if isinstance(_file_share_type, Unset):
            file_share_type = UNSET
        else:
            file_share_type = PublicCloudFileShareType(_file_share_type)

        public_cloud_file_share_policy_object = cls(
            instance_uid=instance_uid,
            instance_name=instance_name,
            policy_uid=policy_uid,
            policy_name=policy_name,
            backup_server_uid=backup_server_uid,
            resource_id=resource_id,
            last_snapshot=last_snapshot,
            last_replica_snapshot=last_replica_snapshot,
            file_share_type=file_share_type,
        )

        public_cloud_file_share_policy_object.additional_properties = d
        return public_cloud_file_share_policy_object

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
