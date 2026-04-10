from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_server_file_job_object_source import BackupServerFileJobObjectSource
    from ..models.backup_server_job_object_last_session import BackupServerJobObjectLastSession


T = TypeVar("T", bound="BackupServerFileShareCopyJobObject")


@_attrs_define
class BackupServerFileShareCopyJobObject:
    """
    Attributes:
        job_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Backup & Replication.
        unique_job_uid (Union[Unset, UUID]): UID assigned to a job in Veeam Service Provider Console.
        file_share_uid (Union[Unset, UUID]): UID assigned to a file share server.
        path (Union[Unset, str]): Path to a location of protected data.
        sources (Union[Unset, list['BackupServerFileJobObjectSource']]): Processed files and folders.
        last_session (Union[Unset, BackupServerJobObjectLastSession]):
    """

    job_uid: Union[Unset, UUID] = UNSET
    unique_job_uid: Union[Unset, UUID] = UNSET
    file_share_uid: Union[Unset, UUID] = UNSET
    path: Union[Unset, str] = UNSET
    sources: Union[Unset, list["BackupServerFileJobObjectSource"]] = UNSET
    last_session: Union[Unset, "BackupServerJobObjectLastSession"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        unique_job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.unique_job_uid, Unset):
            unique_job_uid = str(self.unique_job_uid)

        file_share_uid: Union[Unset, str] = UNSET
        if not isinstance(self.file_share_uid, Unset):
            file_share_uid = str(self.file_share_uid)

        path = self.path

        sources: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        last_session: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_session, Unset):
            last_session = self.last_session.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if unique_job_uid is not UNSET:
            field_dict["uniqueJobUid"] = unique_job_uid
        if file_share_uid is not UNSET:
            field_dict["fileShareUid"] = file_share_uid
        if path is not UNSET:
            field_dict["path"] = path
        if sources is not UNSET:
            field_dict["sources"] = sources
        if last_session is not UNSET:
            field_dict["lastSession"] = last_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.backup_server_file_job_object_source import BackupServerFileJobObjectSource
        from ..models.backup_server_job_object_last_session import BackupServerJobObjectLastSession

        d = dict(src_dict)
        _job_uid = d.pop("jobUid", UNSET)
        job_uid: Union[Unset, UUID]
        if isinstance(_job_uid, Unset):
            job_uid = UNSET
        else:
            job_uid = UUID(_job_uid)

        _unique_job_uid = d.pop("uniqueJobUid", UNSET)
        unique_job_uid: Union[Unset, UUID]
        if isinstance(_unique_job_uid, Unset):
            unique_job_uid = UNSET
        else:
            unique_job_uid = UUID(_unique_job_uid)

        _file_share_uid = d.pop("fileShareUid", UNSET)
        file_share_uid: Union[Unset, UUID]
        if isinstance(_file_share_uid, Unset):
            file_share_uid = UNSET
        else:
            file_share_uid = UUID(_file_share_uid)

        path = d.pop("path", UNSET)

        sources = []
        _sources = d.pop("sources", UNSET)
        for sources_item_data in _sources or []:
            sources_item = BackupServerFileJobObjectSource.from_dict(sources_item_data)

            sources.append(sources_item)

        _last_session = d.pop("lastSession", UNSET)
        last_session: Union[Unset, BackupServerJobObjectLastSession]
        if isinstance(_last_session, Unset):
            last_session = UNSET
        else:
            last_session = BackupServerJobObjectLastSession.from_dict(_last_session)

        backup_server_file_share_copy_job_object = cls(
            job_uid=job_uid,
            unique_job_uid=unique_job_uid,
            file_share_uid=file_share_uid,
            path=path,
            sources=sources,
            last_session=last_session,
        )

        backup_server_file_share_copy_job_object.additional_properties = d
        return backup_server_file_share_copy_job_object

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
