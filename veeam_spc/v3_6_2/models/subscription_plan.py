from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscription_plan_tax_type import SubscriptionPlanTaxType
from ..models.subscription_plan_type import SubscriptionPlanType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription_plan_cloud_backup import SubscriptionPlanCloudBackup
    from ..models.subscription_plan_cloud_replication import SubscriptionPlanCloudReplication
    from ..models.subscription_plan_external_plugin import SubscriptionPlanExternalPlugin
    from ..models.subscription_plan_file_share_backup import SubscriptionPlanFileShareBackup
    from ..models.subscription_plan_licenses import SubscriptionPlanLicenses
    from ..models.subscription_plan_managed_backup import SubscriptionPlanManagedBackup
    from ..models.subscription_plan_public_cloud import SubscriptionPlanPublicCloud
    from ..models.subscription_plan_vb_365 import SubscriptionPlanVb365


T = TypeVar("T", bound="SubscriptionPlan")


@_attrs_define
class SubscriptionPlan:
    """
    Attributes:
        name (str): Name of a subscription plan.
        currency (str): Currency chosen for a subscription plan.
        tax_type (SubscriptionPlanTaxType): Tax type specified for a subscription plan.
        tax_percent (float): Tax amount, in percent.
        discount_percent (float): Discount amount, in percent.
        instance_uid (UUID | Unset): UID assigned to a subscription plan.
        organization_uid (None | Unset | UUID): Name of an organization whose user created a subscription plan.
        type_ (SubscriptionPlanType | Unset): Type of subscription plan.
        description (None | str | Unset): Description of a subscription plan.
        managed_backup (SubscriptionPlanManagedBackup | Unset):
        public_cloud (SubscriptionPlanPublicCloud | Unset):
        vb365 (SubscriptionPlanVb365 | Unset):
        cloud_replication (SubscriptionPlanCloudReplication | Unset):
        file_share_backup (SubscriptionPlanFileShareBackup | Unset):
        cloud_backup (SubscriptionPlanCloudBackup | Unset):
        licenses (SubscriptionPlanLicenses | Unset):
        external_plugins (list[SubscriptionPlanExternalPlugin] | Unset): Array of charges for usage of services provided
            with external plugin functionality.
    """

    name: str
    currency: str
    tax_type: SubscriptionPlanTaxType
    tax_percent: float
    discount_percent: float
    instance_uid: UUID | Unset = UNSET
    organization_uid: None | Unset | UUID = UNSET
    type_: SubscriptionPlanType | Unset = UNSET
    description: None | str | Unset = UNSET
    managed_backup: SubscriptionPlanManagedBackup | Unset = UNSET
    public_cloud: SubscriptionPlanPublicCloud | Unset = UNSET
    vb365: SubscriptionPlanVb365 | Unset = UNSET
    cloud_replication: SubscriptionPlanCloudReplication | Unset = UNSET
    file_share_backup: SubscriptionPlanFileShareBackup | Unset = UNSET
    cloud_backup: SubscriptionPlanCloudBackup | Unset = UNSET
    licenses: SubscriptionPlanLicenses | Unset = UNSET
    external_plugins: list[SubscriptionPlanExternalPlugin] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        currency = self.currency

        tax_type = self.tax_type.value

        tax_percent = self.tax_percent

        discount_percent = self.discount_percent

        instance_uid: str | Unset = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        organization_uid: None | str | Unset
        if isinstance(self.organization_uid, Unset):
            organization_uid = UNSET
        elif isinstance(self.organization_uid, UUID):
            organization_uid = str(self.organization_uid)
        else:
            organization_uid = self.organization_uid

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        managed_backup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.managed_backup, Unset):
            managed_backup = self.managed_backup.to_dict()

        public_cloud: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_cloud, Unset):
            public_cloud = self.public_cloud.to_dict()

        vb365: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vb365, Unset):
            vb365 = self.vb365.to_dict()

        cloud_replication: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud_replication, Unset):
            cloud_replication = self.cloud_replication.to_dict()

        file_share_backup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_share_backup, Unset):
            file_share_backup = self.file_share_backup.to_dict()

        cloud_backup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud_backup, Unset):
            cloud_backup = self.cloud_backup.to_dict()

        licenses: dict[str, Any] | Unset = UNSET
        if not isinstance(self.licenses, Unset):
            licenses = self.licenses.to_dict()

        external_plugins: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.external_plugins, Unset):
            external_plugins = []
            for external_plugins_item_data in self.external_plugins:
                external_plugins_item = external_plugins_item_data.to_dict()
                external_plugins.append(external_plugins_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "currency": currency,
                "taxType": tax_type,
                "taxPercent": tax_percent,
                "discountPercent": discount_percent,
            }
        )
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description
        if managed_backup is not UNSET:
            field_dict["managedBackup"] = managed_backup
        if public_cloud is not UNSET:
            field_dict["publicCloud"] = public_cloud
        if vb365 is not UNSET:
            field_dict["vb365"] = vb365
        if cloud_replication is not UNSET:
            field_dict["cloudReplication"] = cloud_replication
        if file_share_backup is not UNSET:
            field_dict["fileShareBackup"] = file_share_backup
        if cloud_backup is not UNSET:
            field_dict["cloudBackup"] = cloud_backup
        if licenses is not UNSET:
            field_dict["licenses"] = licenses
        if external_plugins is not UNSET:
            field_dict["externalPlugins"] = external_plugins

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_plan_cloud_backup import SubscriptionPlanCloudBackup
        from ..models.subscription_plan_cloud_replication import SubscriptionPlanCloudReplication
        from ..models.subscription_plan_external_plugin import SubscriptionPlanExternalPlugin
        from ..models.subscription_plan_file_share_backup import SubscriptionPlanFileShareBackup
        from ..models.subscription_plan_licenses import SubscriptionPlanLicenses
        from ..models.subscription_plan_managed_backup import SubscriptionPlanManagedBackup
        from ..models.subscription_plan_public_cloud import SubscriptionPlanPublicCloud
        from ..models.subscription_plan_vb_365 import SubscriptionPlanVb365

        d = dict(src_dict)
        name = d.pop("name")

        currency = d.pop("currency")

        tax_type = SubscriptionPlanTaxType(d.pop("taxType"))

        tax_percent = d.pop("taxPercent")

        discount_percent = d.pop("discountPercent")

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: UUID | Unset
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        def _parse_organization_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_uid_type_0 = UUID(data)

                return organization_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_uid = _parse_organization_uid(d.pop("organizationUid", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: SubscriptionPlanType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SubscriptionPlanType(_type_)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _managed_backup = d.pop("managedBackup", UNSET)
        managed_backup: SubscriptionPlanManagedBackup | Unset
        if isinstance(_managed_backup, Unset):
            managed_backup = UNSET
        else:
            managed_backup = SubscriptionPlanManagedBackup.from_dict(_managed_backup)

        _public_cloud = d.pop("publicCloud", UNSET)
        public_cloud: SubscriptionPlanPublicCloud | Unset
        if isinstance(_public_cloud, Unset):
            public_cloud = UNSET
        else:
            public_cloud = SubscriptionPlanPublicCloud.from_dict(_public_cloud)

        _vb365 = d.pop("vb365", UNSET)
        vb365: SubscriptionPlanVb365 | Unset
        if isinstance(_vb365, Unset):
            vb365 = UNSET
        else:
            vb365 = SubscriptionPlanVb365.from_dict(_vb365)

        _cloud_replication = d.pop("cloudReplication", UNSET)
        cloud_replication: SubscriptionPlanCloudReplication | Unset
        if isinstance(_cloud_replication, Unset):
            cloud_replication = UNSET
        else:
            cloud_replication = SubscriptionPlanCloudReplication.from_dict(_cloud_replication)

        _file_share_backup = d.pop("fileShareBackup", UNSET)
        file_share_backup: SubscriptionPlanFileShareBackup | Unset
        if isinstance(_file_share_backup, Unset):
            file_share_backup = UNSET
        else:
            file_share_backup = SubscriptionPlanFileShareBackup.from_dict(_file_share_backup)

        _cloud_backup = d.pop("cloudBackup", UNSET)
        cloud_backup: SubscriptionPlanCloudBackup | Unset
        if isinstance(_cloud_backup, Unset):
            cloud_backup = UNSET
        else:
            cloud_backup = SubscriptionPlanCloudBackup.from_dict(_cloud_backup)

        _licenses = d.pop("licenses", UNSET)
        licenses: SubscriptionPlanLicenses | Unset
        if isinstance(_licenses, Unset):
            licenses = UNSET
        else:
            licenses = SubscriptionPlanLicenses.from_dict(_licenses)

        _external_plugins = d.pop("externalPlugins", UNSET)
        external_plugins: list[SubscriptionPlanExternalPlugin] | Unset = UNSET
        if _external_plugins is not UNSET:
            external_plugins = []
            for external_plugins_item_data in _external_plugins:
                external_plugins_item = SubscriptionPlanExternalPlugin.from_dict(external_plugins_item_data)

                external_plugins.append(external_plugins_item)

        subscription_plan = cls(
            name=name,
            currency=currency,
            tax_type=tax_type,
            tax_percent=tax_percent,
            discount_percent=discount_percent,
            instance_uid=instance_uid,
            organization_uid=organization_uid,
            type_=type_,
            description=description,
            managed_backup=managed_backup,
            public_cloud=public_cloud,
            vb365=vb365,
            cloud_replication=cloud_replication,
            file_share_backup=file_share_backup,
            cloud_backup=cloud_backup,
            licenses=licenses,
            external_plugins=external_plugins,
        )

        subscription_plan.additional_properties = d
        return subscription_plan

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
