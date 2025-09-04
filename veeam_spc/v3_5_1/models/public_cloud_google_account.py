from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudGoogleAccount")


@_attrs_define
class PublicCloudGoogleAccount:
    """
    Attributes:
        name (str): Name of a Google Cloud account.
        instance_uid (Union[Unset, UUID]): UID assigned to a Google Cloud account.
        credential_tag (Union[Unset, UUID]): Tag of Google Cloud account credentials.
        description (Union[Unset, str]): Description of a Google Cloud account.
        project_id (Union[Unset, str]): ID assigned to a project in which a Google Cloud account is created.
        created_by (Union[Unset, str]): Name of a user that created a Google Cloud account.
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect site on which a Google Cloud account is
            registered.
        organization_uid (Union[Unset, UUID]): UID assigned to a mapped organization.
        appliances (Union[Unset, list[UUID]]): Array of UIDs assigned to Veeam Backup for Public Clouds appliances to
            which a Google Cloud account is assigned.
        json_configuration (Union[Unset, str]): Configuration file of a Google Cloud account in the `JSON` format.
    """

    name: str
    instance_uid: Union[Unset, UUID] = UNSET
    credential_tag: Union[Unset, UUID] = UNSET
    description: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    site_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    appliances: Union[Unset, list[UUID]] = UNSET
    json_configuration: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        credential_tag: Union[Unset, str] = UNSET
        if not isinstance(self.credential_tag, Unset):
            credential_tag = str(self.credential_tag)

        description = self.description

        project_id = self.project_id

        created_by = self.created_by

        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        appliances: Union[Unset, list[str]] = UNSET
        if not isinstance(self.appliances, Unset):
            appliances = []
            for appliances_item_data in self.appliances:
                appliances_item = str(appliances_item_data)
                appliances.append(appliances_item)

        json_configuration = self.json_configuration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if credential_tag is not UNSET:
            field_dict["credentialTag"] = credential_tag
        if description is not UNSET:
            field_dict["description"] = description
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if appliances is not UNSET:
            field_dict["appliances"] = appliances
        if json_configuration is not UNSET:
            field_dict["jsonConfiguration"] = json_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _credential_tag = d.pop("credentialTag", UNSET)
        credential_tag: Union[Unset, UUID]
        if isinstance(_credential_tag, Unset):
            credential_tag = UNSET
        else:
            credential_tag = UUID(_credential_tag)

        description = d.pop("description", UNSET)

        project_id = d.pop("projectId", UNSET)

        created_by = d.pop("createdBy", UNSET)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: Union[Unset, UUID]
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        appliances = []
        _appliances = d.pop("appliances", UNSET)
        for appliances_item_data in _appliances or []:
            appliances_item = UUID(appliances_item_data)

            appliances.append(appliances_item)

        json_configuration = d.pop("jsonConfiguration", UNSET)

        public_cloud_google_account = cls(
            name=name,
            instance_uid=instance_uid,
            credential_tag=credential_tag,
            description=description,
            project_id=project_id,
            created_by=created_by,
            site_uid=site_uid,
            organization_uid=organization_uid,
            appliances=appliances,
            json_configuration=json_configuration,
        )

        public_cloud_google_account.additional_properties = d
        return public_cloud_google_account

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
