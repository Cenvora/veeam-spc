import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.invoice_status import InvoiceStatus
from ..models.invoice_type import InvoiceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_data import InvoiceData


T = TypeVar("T", bound="Invoice")


@_attrs_define
class Invoice:
    """
    Attributes:
        data (InvoiceData): Invoice details.
        name (Union[Unset, str]): Name of an organization.
        organization_uid (Union[Unset, UUID]): UID assigned to an organization.
        instance_uid (Union[Unset, UUID]): UID assigned to an invoice.
        amount (Union[Unset, float]): Total cost of consumed backup services
        currency_code (Union[Unset, str]): Currency code.
        subscription_plan_uid (Union[Unset, UUID]): UID assigned to a subscription plan.
        creation_date (Union[Unset, datetime.datetime]): Date and time when an invoice was generated.
        paid_date (Union[Unset, datetime.datetime]): Date and time when an invoice was marked as paid.
        due_date (Union[Unset, datetime.datetime]): Date and time by which a payment must be made.
        status (Union[Unset, InvoiceStatus]): Invoice status.
        type_ (Union[Unset, InvoiceType]): Type of an invoice.
    """

    data: "InvoiceData"
    name: Union[Unset, str] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    instance_uid: Union[Unset, UUID] = UNSET
    amount: Union[Unset, float] = UNSET
    currency_code: Union[Unset, str] = UNSET
    subscription_plan_uid: Union[Unset, UUID] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    paid_date: Union[Unset, datetime.datetime] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, InvoiceStatus] = UNSET
    type_: Union[Unset, InvoiceType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        name = self.name

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        amount = self.amount

        currency_code = self.currency_code

        subscription_plan_uid: Union[Unset, str] = UNSET
        if not isinstance(self.subscription_plan_uid, Unset):
            subscription_plan_uid = str(self.subscription_plan_uid)

        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        paid_date: Union[Unset, str] = UNSET
        if not isinstance(self.paid_date, Unset):
            paid_date = self.paid_date.isoformat()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if subscription_plan_uid is not UNSET:
            field_dict["subscriptionPlanUid"] = subscription_plan_uid
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date
        if paid_date is not UNSET:
            field_dict["paidDate"] = paid_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_data import InvoiceData

        d = dict(src_dict)
        data = InvoiceData.from_dict(d.pop("data"))

        name = d.pop("name", UNSET)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        amount = d.pop("amount", UNSET)

        currency_code = d.pop("currencyCode", UNSET)

        _subscription_plan_uid = d.pop("subscriptionPlanUid", UNSET)
        subscription_plan_uid: Union[Unset, UUID]
        if isinstance(_subscription_plan_uid, Unset):
            subscription_plan_uid = UNSET
        else:
            subscription_plan_uid = UUID(_subscription_plan_uid)

        _creation_date = d.pop("creationDate", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        _paid_date = d.pop("paidDate", UNSET)
        paid_date: Union[Unset, datetime.datetime]
        if isinstance(_paid_date, Unset):
            paid_date = UNSET
        else:
            paid_date = isoparse(_paid_date)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        _status = d.pop("status", UNSET)
        status: Union[Unset, InvoiceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InvoiceStatus(_status)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, InvoiceType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = InvoiceType(_type_)

        invoice = cls(
            data=data,
            name=name,
            organization_uid=organization_uid,
            instance_uid=instance_uid,
            amount=amount,
            currency_code=currency_code,
            subscription_plan_uid=subscription_plan_uid,
            creation_date=creation_date,
            paid_date=paid_date,
            due_date=due_date,
            status=status,
            type_=type_,
        )

        invoice.additional_properties = d
        return invoice

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
