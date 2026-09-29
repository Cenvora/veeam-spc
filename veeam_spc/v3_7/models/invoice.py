from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
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
        name (str | Unset): Name of an organization.
        organization_uid (UUID | Unset): UID assigned to an organization.
        instance_uid (UUID | Unset): UID assigned to an invoice.
        amount (float | None | Unset): Total cost of consumed backup services
        currency_code (None | str | Unset): Currency code.
        subscription_plan_uid (None | Unset | UUID): UID assigned to a subscription plan.
        creation_date (datetime.datetime | Unset): Date and time when an invoice was generated.
        paid_date (datetime.datetime | None | Unset): Date and time when an invoice was marked as paid.
        due_date (datetime.datetime | None | Unset): Date and time by which a payment must be made.
        status (InvoiceStatus | Unset): Invoice status.
        type_ (InvoiceType | Unset): Type of an invoice.
    """

    data: InvoiceData
    name: str | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    instance_uid: UUID | Unset = UNSET
    amount: float | None | Unset = UNSET
    currency_code: None | str | Unset = UNSET
    subscription_plan_uid: None | Unset | UUID = UNSET
    creation_date: datetime.datetime | Unset = UNSET
    paid_date: datetime.datetime | None | Unset = UNSET
    due_date: datetime.datetime | None | Unset = UNSET
    status: InvoiceStatus | Unset = UNSET
    type_: InvoiceType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        name = self.name

        organization_uid: str | Unset = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        amount: float | None | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        currency_code: None | str | Unset
        if isinstance(self.currency_code, Unset):
            currency_code = UNSET
        else:
            currency_code = self.currency_code

        subscription_plan_uid: None | str | Unset
        if isinstance(self.subscription_plan_uid, Unset):
            subscription_plan_uid = UNSET
        elif isinstance(self.subscription_plan_uid, UUID):
            subscription_plan_uid = str(self.subscription_plan_uid)
        else:
            subscription_plan_uid = self.subscription_plan_uid

        creation_date: str | Unset = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        paid_date: None | str | Unset
        if isinstance(self.paid_date, Unset):
            paid_date = UNSET
        elif isinstance(self.paid_date, datetime.datetime):
            paid_date = self.paid_date.isoformat()
        else:
            paid_date = self.paid_date

        due_date: None | str | Unset
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.datetime):
            due_date = self.due_date.isoformat()
        else:
            due_date = self.due_date

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        type_: str | Unset = UNSET
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
        organization_uid: UUID | Unset
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        def _parse_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_currency_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_code = _parse_currency_code(d.pop("currencyCode", UNSET))

        def _parse_subscription_plan_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_plan_uid_type_0 = UUID(data)

                return subscription_plan_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        subscription_plan_uid = _parse_subscription_plan_uid(d.pop("subscriptionPlanUid", UNSET))

        _creation_date = d.pop("creationDate", UNSET)
        creation_date: datetime.datetime | Unset
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        def _parse_paid_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                paid_date_type_0 = isoparse(data)

                return paid_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        paid_date = _parse_paid_date(d.pop("paidDate", UNSET))

        def _parse_due_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_date_type_0 = isoparse(data)

                return due_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        due_date = _parse_due_date(d.pop("dueDate", UNSET))

        _status = d.pop("status", UNSET)
        status: InvoiceStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InvoiceStatus(_status)

        _type_ = d.pop("type", UNSET)
        type_: InvoiceType | Unset
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
