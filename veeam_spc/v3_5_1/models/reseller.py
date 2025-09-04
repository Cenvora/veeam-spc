from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reseller_permissions_item import ResellerPermissionsItem
from ..models.reseller_status import ResellerStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_organization_children_type_0 import EmbeddedForOrganizationChildrenType0
    from ..models.reseller_quota import ResellerQuota


T = TypeVar("T", bound="Reseller")


@_attrs_define
class Reseller:
    """
    Attributes:
        quota (ResellerQuota):
        instance_uid (Union[Unset, UUID]): UID assigned to a reseller.
        pro_partner_id (Union[None, Unset, str]): ProPartner Portal ID assigned to a reseller.
        name (Union[Unset, str]): Name of a reseller.
            > Can be changed using the `PatchOrganization` operation.
        status (Union[Unset, ResellerStatus]): Reseller status. Default: ResellerStatus.ACTIVE.
        permissions (Union[Unset, list[ResellerPermissionsItem]]): Array of the Veeam Service Provider Console
            components that a reseller can access.
        field_embedded (Union['EmbeddedForOrganizationChildrenType0', None, Unset]): Resource representation of the
            related organization entity.
    """

    quota: "ResellerQuota"
    instance_uid: Union[Unset, UUID] = UNSET
    pro_partner_id: Union[None, Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, ResellerStatus] = ResellerStatus.ACTIVE
    permissions: Union[Unset, list[ResellerPermissionsItem]] = UNSET
    field_embedded: Union["EmbeddedForOrganizationChildrenType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.embedded_for_organization_children_type_0 import EmbeddedForOrganizationChildrenType0

        quota = self.quota.to_dict()

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        pro_partner_id: Union[None, Unset, str]
        if isinstance(self.pro_partner_id, Unset):
            pro_partner_id = UNSET
        else:
            pro_partner_id = self.pro_partner_id

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.value
                permissions.append(permissions_item)

        field_embedded: Union[None, Unset, dict[str, Any]]
        if isinstance(self.field_embedded, Unset):
            field_embedded = UNSET
        elif isinstance(self.field_embedded, EmbeddedForOrganizationChildrenType0):
            field_embedded = self.field_embedded.to_dict()
        else:
            field_embedded = self.field_embedded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quota": quota,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if pro_partner_id is not UNSET:
            field_dict["proPartnerId"] = pro_partner_id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_for_organization_children_type_0 import EmbeddedForOrganizationChildrenType0
        from ..models.reseller_quota import ResellerQuota

        d = dict(src_dict)
        quota = ResellerQuota.from_dict(d.pop("quota"))

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        def _parse_pro_partner_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pro_partner_id = _parse_pro_partner_id(d.pop("proPartnerId", UNSET))

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ResellerStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ResellerStatus(_status)

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = ResellerPermissionsItem(permissions_item_data)

            permissions.append(permissions_item)

        def _parse_field_embedded(data: object) -> Union["EmbeddedForOrganizationChildrenType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_embedded_for_organization_children_type_0 = (
                    EmbeddedForOrganizationChildrenType0.from_dict(data)
                )

                return componentsschemas_embedded_for_organization_children_type_0
            except:  # noqa: E722
                pass
            return cast(Union["EmbeddedForOrganizationChildrenType0", None, Unset], data)

        field_embedded = _parse_field_embedded(d.pop("_embedded", UNSET))

        reseller = cls(
            quota=quota,
            instance_uid=instance_uid,
            pro_partner_id=pro_partner_id,
            name=name,
            status=status,
            permissions=permissions,
            field_embedded=field_embedded,
        )

        reseller.additional_properties = d
        return reseller

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
