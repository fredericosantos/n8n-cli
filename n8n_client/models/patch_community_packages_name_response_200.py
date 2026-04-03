from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_community_packages_name_response_200_installed_nodes_item import (
        PatchCommunityPackagesNameResponse200InstalledNodesItem,
    )


T = TypeVar("T", bound="PatchCommunityPackagesNameResponse200")


@_attrs_define
class PatchCommunityPackagesNameResponse200:
    """
    Attributes:
        package_name (str | Unset): npm package name
        installed_version (str | Unset): Currently installed version
        author_name (str | Unset): Package author name
        author_email (str | Unset): Package author email
        installed_nodes (list[PatchCommunityPackagesNameResponse200InstalledNodesItem] | Unset): Nodes included in this
            package
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        update_available (str | Unset): Version available for update, if any
        failed_loading (bool | Unset): Whether the package failed to load
    """

    package_name: str | Unset = UNSET
    installed_version: str | Unset = UNSET
    author_name: str | Unset = UNSET
    author_email: str | Unset = UNSET
    installed_nodes: list[PatchCommunityPackagesNameResponse200InstalledNodesItem] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    update_available: str | Unset = UNSET
    failed_loading: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_name = self.package_name

        installed_version = self.installed_version

        author_name = self.author_name

        author_email = self.author_email

        installed_nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.installed_nodes, Unset):
            installed_nodes = []
            for installed_nodes_item_data in self.installed_nodes:
                installed_nodes_item = installed_nodes_item_data.to_dict()
                installed_nodes.append(installed_nodes_item)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        update_available = self.update_available

        failed_loading = self.failed_loading

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if installed_version is not UNSET:
            field_dict["installedVersion"] = installed_version
        if author_name is not UNSET:
            field_dict["authorName"] = author_name
        if author_email is not UNSET:
            field_dict["authorEmail"] = author_email
        if installed_nodes is not UNSET:
            field_dict["installedNodes"] = installed_nodes
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if update_available is not UNSET:
            field_dict["updateAvailable"] = update_available
        if failed_loading is not UNSET:
            field_dict["failedLoading"] = failed_loading

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_community_packages_name_response_200_installed_nodes_item import (
            PatchCommunityPackagesNameResponse200InstalledNodesItem,
        )

        d = dict(src_dict)
        package_name = d.pop("packageName", UNSET)

        installed_version = d.pop("installedVersion", UNSET)

        author_name = d.pop("authorName", UNSET)

        author_email = d.pop("authorEmail", UNSET)

        _installed_nodes = d.pop("installedNodes", UNSET)
        installed_nodes: list[PatchCommunityPackagesNameResponse200InstalledNodesItem] | Unset = UNSET
        if _installed_nodes is not UNSET:
            installed_nodes = []
            for installed_nodes_item_data in _installed_nodes:
                installed_nodes_item = PatchCommunityPackagesNameResponse200InstalledNodesItem.from_dict(
                    installed_nodes_item_data
                )

                installed_nodes.append(installed_nodes_item)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        update_available = d.pop("updateAvailable", UNSET)

        failed_loading = d.pop("failedLoading", UNSET)

        patch_community_packages_name_response_200 = cls(
            package_name=package_name,
            installed_version=installed_version,
            author_name=author_name,
            author_email=author_email,
            installed_nodes=installed_nodes,
            created_at=created_at,
            updated_at=updated_at,
            update_available=update_available,
            failed_loading=failed_loading,
        )

        patch_community_packages_name_response_200.additional_properties = d
        return patch_community_packages_name_response_200

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
