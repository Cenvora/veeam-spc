from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reseller_status import ResellerStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_for_organization_children import EmbeddedForOrganizationChildren
    from ..models.reseller_services import ResellerServices


T = TypeVar("T", bound="Reseller")


@_attrs_define
class Reseller:
    """
    Attributes:
        instance_uid (Union[Unset, UUID]): UID assigned to a reseller.
        pro_partner_id (Union[Unset, str]): ProPartner Portal ID assigned to a reseller.
        name (Union[Unset, str]): Name of a reseller.
            > Can be changed using the `PatchOrganization` operation.
        status (Union[Unset, ResellerStatus]): Reseller status. Default: ResellerStatus.ACTIVE.
        is_rest_access_enabled (Union[Unset, bool]): Indicates whether access to REST API is enabled for a reseller.
            Default: False.
        reseller_services (Union[Unset, ResellerServices]):
        field_embedded (Union[Unset, EmbeddedForOrganizationChildren]): Resource representation of the related
            organization entity.
    """

    instance_uid: Union[Unset, UUID] = UNSET
    pro_partner_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, ResellerStatus] = ResellerStatus.ACTIVE
    is_rest_access_enabled: Union[Unset, bool] = False
    reseller_services: Union[Unset, "ResellerServices"] = UNSET
    field_embedded: Union[Unset, "EmbeddedForOrganizationChildren"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        pro_partner_id = self.pro_partner_id

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        is_rest_access_enabled = self.is_rest_access_enabled

        reseller_services: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reseller_services, Unset):
            reseller_services = self.reseller_services.to_dict()

        field_embedded: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if pro_partner_id is not UNSET:
            field_dict["proPartnerId"] = pro_partner_id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if is_rest_access_enabled is not UNSET:
            field_dict["isRestAccessEnabled"] = is_rest_access_enabled
        if reseller_services is not UNSET:
            field_dict["resellerServices"] = reseller_services
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_for_organization_children import EmbeddedForOrganizationChildren
        from ..models.reseller_services import ResellerServices

        d = dict(src_dict)
        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        pro_partner_id = d.pop("proPartnerId", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ResellerStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ResellerStatus(_status)

        is_rest_access_enabled = d.pop("isRestAccessEnabled", UNSET)

        _reseller_services = d.pop("resellerServices", UNSET)
        reseller_services: Union[Unset, ResellerServices]
        if isinstance(_reseller_services, Unset):
            reseller_services = UNSET
        else:
            reseller_services = ResellerServices.from_dict(_reseller_services)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, EmbeddedForOrganizationChildren]
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = EmbeddedForOrganizationChildren.from_dict(_field_embedded)

        reseller = cls(
            instance_uid=instance_uid,
            pro_partner_id=pro_partner_id,
            name=name,
            status=status,
            is_rest_access_enabled=is_rest_access_enabled,
            reseller_services=reseller_services,
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
