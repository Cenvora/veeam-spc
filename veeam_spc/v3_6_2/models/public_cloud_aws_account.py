from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
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
        account_uid (UUID | Unset): UID assigned to an AWS account.
        credential_tag (UUID | Unset): UID assigned to an account in AWS.
        secret_key (None | str | Unset): AWS access secret key.
        description (None | str | Unset): Description of an AWS account.
        created_by (str | Unset): Name of a user that created an AWS account.
        site_uid (UUID | Unset): UID assigned to a Veeam Cloud Connect site on which an AWS account is registered.
        organization_uid (UUID | Unset): UID assigned to an organization associated with an AWS account.
        appliances (list[UUID] | None | Unset): Array of UIDs assigned to associated Veeam Backup for Public Clouds
            appliances.
    """

    access_key: str
    account_uid: UUID | Unset = UNSET
    credential_tag: UUID | Unset = UNSET
    secret_key: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    created_by: str | Unset = UNSET
    site_uid: UUID | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    appliances: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_key = self.access_key

        account_uid: str | Unset = UNSET
        if not isinstance(self.account_uid, Unset):
            account_uid = str(self.account_uid)

        credential_tag: str | Unset = UNSET
        if not isinstance(self.credential_tag, Unset):
            credential_tag = str(self.credential_tag)

        secret_key: None | str | Unset
        if isinstance(self.secret_key, Unset):
            secret_key = UNSET
        else:
            secret_key = self.secret_key

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        created_by = self.created_by

        site_uid: str | Unset = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        organization_uid: str | Unset = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        appliances: list[str] | None | Unset
        if isinstance(self.appliances, Unset):
            appliances = UNSET
        elif isinstance(self.appliances, list):
            appliances = []
            for appliances_type_0_item_data in self.appliances:
                appliances_type_0_item = str(appliances_type_0_item_data)
                appliances.append(appliances_type_0_item)

        else:
            appliances = self.appliances

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
        account_uid: UUID | Unset
        if isinstance(_account_uid, Unset):
            account_uid = UNSET
        else:
            account_uid = UUID(_account_uid)

        _credential_tag = d.pop("credentialTag", UNSET)
        credential_tag: UUID | Unset
        if isinstance(_credential_tag, Unset):
            credential_tag = UNSET
        else:
            credential_tag = UUID(_credential_tag)

        def _parse_secret_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secret_key = _parse_secret_key(d.pop("secretKey", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        created_by = d.pop("createdBy", UNSET)

        _site_uid = d.pop("siteUid", UNSET)
        site_uid: UUID | Unset
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: UUID | Unset
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        def _parse_appliances(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                appliances_type_0 = []
                _appliances_type_0 = data
                for appliances_type_0_item_data in _appliances_type_0:
                    appliances_type_0_item = UUID(appliances_type_0_item_data)

                    appliances_type_0.append(appliances_type_0_item)

                return appliances_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        appliances = _parse_appliances(d.pop("appliances", UNSET))

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
