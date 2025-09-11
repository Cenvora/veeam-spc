from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicCloudAwsAccount")


@_attrs_define
class PublicCloudAwsAccount:
    """
    Attributes:
        access_key (str): AWS access key.
        account_uid (Union[Unset, UUID]): UID assigned to an AWS account.
        credential_tag (Union[Unset, UUID]): UID assigned to an account in AWS.
        secret_key (Union[Unset, str]): AWS access secret key.
        description (Union[Unset, str]): Description of an AWS account.
        created_by (Union[Unset, str]): Name of a user that created an AWS account.
        site_uid (Union[Unset, UUID]): UID assigned to a Veeam Cloud Connect site on which an AWS account is registered.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization associated with an AWS account.
        appliances (Union[Unset, list[UUID]]): Array of UIDs assigned to associated Veeam Backup for Public Clouds
            appliances.
    """

    access_key: str
    account_uid: Union[Unset, UUID] = UNSET
    credential_tag: Union[Unset, UUID] = UNSET
    secret_key: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    site_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    appliances: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_key = self.access_key

        account_uid: Union[Unset, str] = UNSET
        if not isinstance(self.account_uid, Unset):
            account_uid = str(self.account_uid)

        credential_tag: Union[Unset, str] = UNSET
        if not isinstance(self.credential_tag, Unset):
            credential_tag = str(self.credential_tag)

        secret_key = self.secret_key

        description = self.description

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessKey": access_key,
            }
        )
        if account_uid is not UNSET:
            field_dict["accountUid"] = account_uid
        if credential_tag is not UNSET:
            field_dict["credentialTag"] = credential_tag
        if secret_key is not UNSET:
            field_dict["secretKey"] = secret_key
        if description is not UNSET:
            field_dict["description"] = description
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if appliances is not UNSET:
            field_dict["appliances"] = appliances

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_key = d.pop("accessKey")

        _account_uid = d.pop("accountUid", UNSET)
        account_uid: Union[Unset, UUID]
        if isinstance(_account_uid, Unset):
            account_uid = UNSET
        else:
            account_uid = UUID(_account_uid)

        _credential_tag = d.pop("credentialTag", UNSET)
        credential_tag: Union[Unset, UUID]
        if isinstance(_credential_tag, Unset):
            credential_tag = UNSET
        else:
            credential_tag = UUID(_credential_tag)

        secret_key = d.pop("secretKey", UNSET)

        description = d.pop("description", UNSET)

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

        public_cloud_aws_account = cls(
            access_key=access_key,
            account_uid=account_uid,
            credential_tag=credential_tag,
            secret_key=secret_key,
            description=description,
            created_by=created_by,
            site_uid=site_uid,
            organization_uid=organization_uid,
            appliances=appliances,
        )

        public_cloud_aws_account.additional_properties = d
        return public_cloud_aws_account

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
