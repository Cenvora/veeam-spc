from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alarm_category import AlarmCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alarm_knowledge import AlarmKnowledge


T = TypeVar("T", bound="Alarm")


@_attrs_define
class Alarm:
    """
    Example:
        {'instanceUid': 'fcdb7145-3634-4d34-99fd-138879cd9c2c', 'name': 'Job state', 'category': 'BackupVmJob',
            'organizationUid': '39f65b4c-a7d2-451e-936d-aeae418b53e1', 'internalId': 1, 'knowledge': {'summary': 'Job is in
            a disabled state for more than an allowed time period.', 'cause': 'Veeam Backup & Replication server allows to
            disable scheduled backup jobs during maintenance windows. If backup job stays in a disabled state for more than
            an allowed time period, it should be enabled back.', 'resolution': 'Open Veeam Backup & Replication console and
            enable all disabled backup jobs.'}, 'isPredifined': True, 'isEnabled': False}

    Attributes:
        name (str): Name of an alarm template.
        is_enabled (bool):  Indicates whether an alarm template is enabled.
        instance_uid (Union[Unset, UUID]): UID assigned to an alarm template.
        category (Union[Unset, AlarmCategory]): Category of an alarm template.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        internal_id (Union[Unset, int]): ID assigned to an alarm template in Veeam Service Provider Console internal
            alarm database.
        knowledge (Union[Unset, AlarmKnowledge]): Knowledge base for an alarm template.
        is_predifined (Union[Unset, bool]): Indicates whether an alarm template is predefined.
    """

    name: str
    is_enabled: bool
    instance_uid: Union[Unset, UUID] = UNSET
    category: Union[Unset, AlarmCategory] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    internal_id: Union[Unset, int] = UNSET
    knowledge: Union[Unset, "AlarmKnowledge"] = UNSET
    is_predifined: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        is_enabled = self.is_enabled

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        internal_id = self.internal_id

        knowledge: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.knowledge, Unset):
            knowledge = self.knowledge.to_dict()

        is_predifined = self.is_predifined

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "isEnabled": is_enabled,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if category is not UNSET:
            field_dict["category"] = category
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if internal_id is not UNSET:
            field_dict["internalId"] = internal_id
        if knowledge is not UNSET:
            field_dict["knowledge"] = knowledge
        if is_predifined is not UNSET:
            field_dict["isPredifined"] = is_predifined

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alarm_knowledge import AlarmKnowledge

        d = dict(src_dict)
        name = d.pop("name")

        is_enabled = d.pop("isEnabled")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _category = d.pop("category", UNSET)
        category: Union[Unset, AlarmCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = AlarmCategory(_category)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        internal_id = d.pop("internalId", UNSET)

        _knowledge = d.pop("knowledge", UNSET)
        knowledge: Union[Unset, AlarmKnowledge]
        if isinstance(_knowledge, Unset):
            knowledge = UNSET
        else:
            knowledge = AlarmKnowledge.from_dict(_knowledge)

        is_predifined = d.pop("isPredifined", UNSET)

        alarm = cls(
            name=name,
            is_enabled=is_enabled,
            instance_uid=instance_uid,
            category=category,
            organization_uid=organization_uid,
            internal_id=internal_id,
            knowledge=knowledge,
            is_predifined=is_predifined,
        )

        alarm.additional_properties = d
        return alarm

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
