from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_error import ResponseError
    from ..models.response_metadata import ResponseMetadata
    from ..models.vb_365_backup_job import Vb365BackupJob


T = TypeVar("T", bound="PatchVb365BackupJobResponse200")


@_attrs_define
class PatchVb365BackupJobResponse200:
    """
    Attributes:
        data (Vb365BackupJob):  Example: {'name': 'BackupJob2', 'description': 'Veeam Backup for Microsoft 365 backup
            job', 'repositoryUid': '92421aa8-db1e-42ef-b210-b5d7750baffa', 'isEnabled': False, 'backupType':
            'SelectedItems', 'selectedItems': [{'itemType': 'User', 'folders': [], 'backupMailbox': True, 'backupOneDrive':
            True, 'backupArchiveMailbox': True, 'backupPersonalSite': True, 'backupSites': False, 'backupTeams': False,
            'backupTeamsChats': False, 'backupMembers': False, 'backupMemberMailbox': False, 'backupMemberArchiveMailbox':
            False, 'backupMemberOneDrive': False, 'backupMemberSite': False, 'backupGroupSite': False, 'site': None, 'team':
            None, 'user': {'id': 'lrs.onmicrosoft.com:00000000-0000-0000-0000-000000000000:00000000-0000-0000-0000-
            000000000000:858bae82-7ff7-4ab5-be78-3c2da97c9c3d:00000000-0000-0000-0000-000000000000', 'onPremisesSid': None,
            'userType': 'User', 'name': 'ktang@mycompany.onmicrosoft.com', 'displayName': 'Kate Tang'}, 'group': None},
            {'itemType': 'Team', 'folders': [], 'backupMailbox': False, 'backupOneDrive': False, 'backupArchiveMailbox':
            False, 'backupPersonalSite': False, 'backupSites': False, 'backupTeams': False, 'backupTeamsChats': False,
            'backupMembers': False, 'backupMemberMailbox': False, 'backupMemberArchiveMailbox': False,
            'backupMemberOneDrive': False, 'backupMemberSite': False, 'backupGroupSite': False, 'site': None, 'team': {'id':
            '97033983-9122-1907-94e2-46445967791a', 'displayName': 'Lrsvbm', 'description': 'Lrsvbm', 'mail':
            'Lrsvbm@mycompany.onmicrosoft.com'}, 'user': None, 'group': None}, {'itemType': 'Site', 'folders': [],
            'backupMailbox': False, 'backupOneDrive': False, 'backupArchiveMailbox': False, 'backupPersonalSite': False,
            'backupSites': False, 'backupTeams': False, 'backupTeamsChats': False, 'backupMembers': False,
            'backupMemberMailbox': False, 'backupMemberArchiveMailbox': False, 'backupMemberOneDrive': False,
            'backupMemberSite': False, 'backupGroupSite': False, 'site': {'id':
            'c518d8b0-db04-6bb8-8c39-21b18ebe71345c38aa48-1b78-4411-a0a7-15a83d0e8d50', 'title': 'Team Site', 'url':
            'https://mycompany.sharepoint.com/sites/contentTypeHub'}, 'team': None, 'user': None, 'group': None}],
            'excludedItems': [], 'schedulePolicy': {'schedulePolicyType': 'ManualOnly', 'periodicallyEvery': None,
            'dailyType': None, 'scheduleEnabled': False, 'backupWindowEnabled': False, 'backupWindowSettings':
            {'backupWindow': [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True], 'minuteOffset': None}, 'periodicallyWindowSettings':
            {'backupWindow': [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
            True, True, True, True, True, True, True, True, True], 'minuteOffset': None}, 'periodicallyWindowEnabled':
            False, 'periodicallyOffsetMinutes': None, 'dailyTime': None, 'retryEnabled': False, 'retryNumber': None,
            'retryWaitInterval': None}}.
        meta (ResponseMetadata | Unset):
        errors (list[ResponseError] | Unset):
    """

    data: Vb365BackupJob
    meta: ResponseMetadata | Unset = UNSET
    errors: list[ResponseError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_error import ResponseError
        from ..models.response_metadata import ResponseMetadata
        from ..models.vb_365_backup_job import Vb365BackupJob

        d = dict(src_dict)
        data = Vb365BackupJob.from_dict(d.pop("data"))

        _meta = d.pop("meta", UNSET)
        meta: ResponseMetadata | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResponseMetadata.from_dict(_meta)

        _errors = d.pop("errors", UNSET)
        errors: list[ResponseError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ResponseError.from_dict(errors_item_data)

                errors.append(errors_item)

        patch_vb_365_backup_job_response_200 = cls(
            data=data,
            meta=meta,
            errors=errors,
        )

        patch_vb_365_backup_job_response_200.additional_properties = d
        return patch_vb_365_backup_job_response_200

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
