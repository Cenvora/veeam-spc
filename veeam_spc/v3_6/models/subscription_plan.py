from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
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
        instance_uid (Union[Unset, UUID]): UID assigned to a subscription plan.
        organization_uid (Union[Unset, UUID]): Name of an organization whose user created a subscription plan.
        type_ (Union[Unset, SubscriptionPlanType]): Type of subscription plan.
        description (Union[Unset, str]): Description of a subscription plan.
        managed_backup (Union[Unset, SubscriptionPlanManagedBackup]):
        public_cloud (Union[Unset, SubscriptionPlanPublicCloud]):
        vb365 (Union[Unset, SubscriptionPlanVb365]):
        cloud_replication (Union[Unset, SubscriptionPlanCloudReplication]):
        file_share_backup (Union[Unset, SubscriptionPlanFileShareBackup]):
        cloud_backup (Union[Unset, SubscriptionPlanCloudBackup]):
        licenses (Union[Unset, SubscriptionPlanLicenses]):
        external_plugins (Union[Unset, list['SubscriptionPlanExternalPlugin']]): Array of charges for usage of services
            provided with external plugin functionality.
    """

    name: str
    currency: str
    tax_type: SubscriptionPlanTaxType
    tax_percent: float
    discount_percent: float
    instance_uid: Union[Unset, UUID] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    type_: Union[Unset, SubscriptionPlanType] = UNSET
    description: Union[Unset, str] = UNSET
    managed_backup: Union[Unset, "SubscriptionPlanManagedBackup"] = UNSET
    public_cloud: Union[Unset, "SubscriptionPlanPublicCloud"] = UNSET
    vb365: Union[Unset, "SubscriptionPlanVb365"] = UNSET
    cloud_replication: Union[Unset, "SubscriptionPlanCloudReplication"] = UNSET
    file_share_backup: Union[Unset, "SubscriptionPlanFileShareBackup"] = UNSET
    cloud_backup: Union[Unset, "SubscriptionPlanCloudBackup"] = UNSET
    licenses: Union[Unset, "SubscriptionPlanLicenses"] = UNSET
    external_plugins: Union[Unset, list["SubscriptionPlanExternalPlugin"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        currency = self.currency

        tax_type = self.tax_type.value

        tax_percent = self.tax_percent

        discount_percent = self.discount_percent

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        description = self.description

        managed_backup: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.managed_backup, Unset):
            managed_backup = self.managed_backup.to_dict()

        public_cloud: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.public_cloud, Unset):
            public_cloud = self.public_cloud.to_dict()

        vb365: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vb365, Unset):
            vb365 = self.vb365.to_dict()

        cloud_replication: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cloud_replication, Unset):
            cloud_replication = self.cloud_replication.to_dict()

        file_share_backup: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.file_share_backup, Unset):
            file_share_backup = self.file_share_backup.to_dict()

        cloud_backup: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cloud_backup, Unset):
            cloud_backup = self.cloud_backup.to_dict()

        licenses: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.licenses, Unset):
            licenses = self.licenses.to_dict()

        external_plugins: Union[Unset, list[dict[str, Any]]] = UNSET
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
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, SubscriptionPlanType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SubscriptionPlanType(_type_)

        description = d.pop("description", UNSET)

        _managed_backup = d.pop("managedBackup", UNSET)
        managed_backup: Union[Unset, SubscriptionPlanManagedBackup]
        if isinstance(_managed_backup, Unset):
            managed_backup = UNSET
        else:
            managed_backup = SubscriptionPlanManagedBackup.from_dict(_managed_backup)

        _public_cloud = d.pop("publicCloud", UNSET)
        public_cloud: Union[Unset, SubscriptionPlanPublicCloud]
        if isinstance(_public_cloud, Unset):
            public_cloud = UNSET
        else:
            public_cloud = SubscriptionPlanPublicCloud.from_dict(_public_cloud)

        _vb365 = d.pop("vb365", UNSET)
        vb365: Union[Unset, SubscriptionPlanVb365]
        if isinstance(_vb365, Unset):
            vb365 = UNSET
        else:
            vb365 = SubscriptionPlanVb365.from_dict(_vb365)

        _cloud_replication = d.pop("cloudReplication", UNSET)
        cloud_replication: Union[Unset, SubscriptionPlanCloudReplication]
        if isinstance(_cloud_replication, Unset):
            cloud_replication = UNSET
        else:
            cloud_replication = SubscriptionPlanCloudReplication.from_dict(_cloud_replication)

        _file_share_backup = d.pop("fileShareBackup", UNSET)
        file_share_backup: Union[Unset, SubscriptionPlanFileShareBackup]
        if isinstance(_file_share_backup, Unset):
            file_share_backup = UNSET
        else:
            file_share_backup = SubscriptionPlanFileShareBackup.from_dict(_file_share_backup)

        _cloud_backup = d.pop("cloudBackup", UNSET)
        cloud_backup: Union[Unset, SubscriptionPlanCloudBackup]
        if isinstance(_cloud_backup, Unset):
            cloud_backup = UNSET
        else:
            cloud_backup = SubscriptionPlanCloudBackup.from_dict(_cloud_backup)

        _licenses = d.pop("licenses", UNSET)
        licenses: Union[Unset, SubscriptionPlanLicenses]
        if isinstance(_licenses, Unset):
            licenses = UNSET
        else:
            licenses = SubscriptionPlanLicenses.from_dict(_licenses)

        external_plugins = []
        _external_plugins = d.pop("externalPlugins", UNSET)
        for external_plugins_item_data in _external_plugins or []:
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
