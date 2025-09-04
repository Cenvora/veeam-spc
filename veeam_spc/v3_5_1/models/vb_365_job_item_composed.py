from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vb_365_job_item_composed_item_type import Vb365JobItemComposedItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vb_365_job_item_group import Vb365JobItemGroup
    from ..models.vb_365_job_item_site import Vb365JobItemSite
    from ..models.vb_365_job_item_team import Vb365JobItemTeam
    from ..models.vb_365_job_item_user import Vb365JobItemUser


T = TypeVar("T", bound="Vb365JobItemComposed")


@_attrs_define
class Vb365JobItemComposed:
    """
    Attributes:
        id (Union[Unset, str]): ID assigned to a backup job item.
        item_type (Union[Unset, Vb365JobItemComposedItemType]): Type of a backup job item.
        folders (Union[None, Unset, list[str]]): Array of folders included in a backup job.
        backup_mailbox (Union[Unset, bool]): Indicates whether a backup job must include mailboxes. Default: False.
        backup_one_drive (Union[Unset, bool]): Indicates whether a backup job must include OneDrive data. Default:
            False.
        backup_archive_mailbox (Union[Unset, bool]): Indicates whether a backup job must include mailbox archive.
            Default: False.
        backup_personal_site (Union[Unset, bool]): Indicates whether a backup job must include personal sites. Default:
            False.
        backup_sites (Union[Unset, bool]): Indicates whether a backup job must include sites. Default: False.
        backup_teams (Union[Unset, bool]): Indicates whether a backup job must include Microsoft Teams data. Default:
            False.
        backup_teams_chats (Union[Unset, bool]): Indicates whether a backup job must include Microsoft Teams chat data.
            Default: False.
        backup_members (Union[Unset, bool]): Indicates whether a backup job must include group member data. Default:
            False.
        backup_member_mailbox (Union[Unset, bool]): Indicates whether a backup job must include group member mailboxes.
            Default: False.
        backup_member_archive_mailbox (Union[Unset, bool]): Indicates whether a backup job must include group member
            mailbox archive. Default: False.
        backup_member_one_drive (Union[Unset, bool]): Indicates whether a backup job must include group member OneDrive
            data. Default: False.
        backup_member_site (Union[Unset, bool]): Indicates whether a backup job must include group member sites.
            Default: False.
        backup_group_site (Union[Unset, bool]): Indicates whether a backup job must include group sites. Default: False.
        site (Union[Unset, Vb365JobItemSite]):
        team (Union[Unset, Vb365JobItemTeam]):
        user (Union[Unset, Vb365JobItemUser]):
        group (Union[Unset, Vb365JobItemGroup]):
    """

    id: Union[Unset, str] = UNSET
    item_type: Union[Unset, Vb365JobItemComposedItemType] = UNSET
    folders: Union[None, Unset, list[str]] = UNSET
    backup_mailbox: Union[Unset, bool] = False
    backup_one_drive: Union[Unset, bool] = False
    backup_archive_mailbox: Union[Unset, bool] = False
    backup_personal_site: Union[Unset, bool] = False
    backup_sites: Union[Unset, bool] = False
    backup_teams: Union[Unset, bool] = False
    backup_teams_chats: Union[Unset, bool] = False
    backup_members: Union[Unset, bool] = False
    backup_member_mailbox: Union[Unset, bool] = False
    backup_member_archive_mailbox: Union[Unset, bool] = False
    backup_member_one_drive: Union[Unset, bool] = False
    backup_member_site: Union[Unset, bool] = False
    backup_group_site: Union[Unset, bool] = False
    site: Union[Unset, "Vb365JobItemSite"] = UNSET
    team: Union[Unset, "Vb365JobItemTeam"] = UNSET
    user: Union[Unset, "Vb365JobItemUser"] = UNSET
    group: Union[Unset, "Vb365JobItemGroup"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        folders: Union[None, Unset, list[str]]
        if isinstance(self.folders, Unset):
            folders = UNSET
        elif isinstance(self.folders, list):
            folders = self.folders

        else:
            folders = self.folders

        backup_mailbox = self.backup_mailbox

        backup_one_drive = self.backup_one_drive

        backup_archive_mailbox = self.backup_archive_mailbox

        backup_personal_site = self.backup_personal_site

        backup_sites = self.backup_sites

        backup_teams = self.backup_teams

        backup_teams_chats = self.backup_teams_chats

        backup_members = self.backup_members

        backup_member_mailbox = self.backup_member_mailbox

        backup_member_archive_mailbox = self.backup_member_archive_mailbox

        backup_member_one_drive = self.backup_member_one_drive

        backup_member_site = self.backup_member_site

        backup_group_site = self.backup_group_site

        site: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.to_dict()

        team: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if folders is not UNSET:
            field_dict["folders"] = folders
        if backup_mailbox is not UNSET:
            field_dict["backupMailbox"] = backup_mailbox
        if backup_one_drive is not UNSET:
            field_dict["backupOneDrive"] = backup_one_drive
        if backup_archive_mailbox is not UNSET:
            field_dict["backupArchiveMailbox"] = backup_archive_mailbox
        if backup_personal_site is not UNSET:
            field_dict["backupPersonalSite"] = backup_personal_site
        if backup_sites is not UNSET:
            field_dict["backupSites"] = backup_sites
        if backup_teams is not UNSET:
            field_dict["backupTeams"] = backup_teams
        if backup_teams_chats is not UNSET:
            field_dict["backupTeamsChats"] = backup_teams_chats
        if backup_members is not UNSET:
            field_dict["backupMembers"] = backup_members
        if backup_member_mailbox is not UNSET:
            field_dict["backupMemberMailbox"] = backup_member_mailbox
        if backup_member_archive_mailbox is not UNSET:
            field_dict["backupMemberArchiveMailbox"] = backup_member_archive_mailbox
        if backup_member_one_drive is not UNSET:
            field_dict["backupMemberOneDrive"] = backup_member_one_drive
        if backup_member_site is not UNSET:
            field_dict["backupMemberSite"] = backup_member_site
        if backup_group_site is not UNSET:
            field_dict["backupGroupSite"] = backup_group_site
        if site is not UNSET:
            field_dict["site"] = site
        if team is not UNSET:
            field_dict["team"] = team
        if user is not UNSET:
            field_dict["user"] = user
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vb_365_job_item_group import Vb365JobItemGroup
        from ..models.vb_365_job_item_site import Vb365JobItemSite
        from ..models.vb_365_job_item_team import Vb365JobItemTeam
        from ..models.vb_365_job_item_user import Vb365JobItemUser

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _item_type = d.pop("itemType", UNSET)
        item_type: Union[Unset, Vb365JobItemComposedItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = Vb365JobItemComposedItemType(_item_type)

        def _parse_folders(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                folders_type_0 = cast(list[str], data)

                return folders_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        folders = _parse_folders(d.pop("folders", UNSET))

        backup_mailbox = d.pop("backupMailbox", UNSET)

        backup_one_drive = d.pop("backupOneDrive", UNSET)

        backup_archive_mailbox = d.pop("backupArchiveMailbox", UNSET)

        backup_personal_site = d.pop("backupPersonalSite", UNSET)

        backup_sites = d.pop("backupSites", UNSET)

        backup_teams = d.pop("backupTeams", UNSET)

        backup_teams_chats = d.pop("backupTeamsChats", UNSET)

        backup_members = d.pop("backupMembers", UNSET)

        backup_member_mailbox = d.pop("backupMemberMailbox", UNSET)

        backup_member_archive_mailbox = d.pop("backupMemberArchiveMailbox", UNSET)

        backup_member_one_drive = d.pop("backupMemberOneDrive", UNSET)

        backup_member_site = d.pop("backupMemberSite", UNSET)

        backup_group_site = d.pop("backupGroupSite", UNSET)

        _site = d.pop("site", UNSET)
        site: Union[Unset, Vb365JobItemSite]
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = Vb365JobItemSite.from_dict(_site)

        _team = d.pop("team", UNSET)
        team: Union[Unset, Vb365JobItemTeam]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Vb365JobItemTeam.from_dict(_team)

        _user = d.pop("user", UNSET)
        user: Union[Unset, Vb365JobItemUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = Vb365JobItemUser.from_dict(_user)

        _group = d.pop("group", UNSET)
        group: Union[Unset, Vb365JobItemGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = Vb365JobItemGroup.from_dict(_group)

        vb_365_job_item_composed = cls(
            id=id,
            item_type=item_type,
            folders=folders,
            backup_mailbox=backup_mailbox,
            backup_one_drive=backup_one_drive,
            backup_archive_mailbox=backup_archive_mailbox,
            backup_personal_site=backup_personal_site,
            backup_sites=backup_sites,
            backup_teams=backup_teams,
            backup_teams_chats=backup_teams_chats,
            backup_members=backup_members,
            backup_member_mailbox=backup_member_mailbox,
            backup_member_archive_mailbox=backup_member_archive_mailbox,
            backup_member_one_drive=backup_member_one_drive,
            backup_member_site=backup_member_site,
            backup_group_site=backup_group_site,
            site=site,
            team=team,
            user=user,
            group=group,
        )

        vb_365_job_item_composed.additional_properties = d
        return vb_365_job_item_composed

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
