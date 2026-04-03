from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchCommunityPackagesNameResponse200InstalledNodesItem")


@_attrs_define
class PatchCommunityPackagesNameResponse200InstalledNodesItem:
    """
    Attributes:
        name (str | Unset):
        type_ (str | Unset):
        latest_version (float | Unset):
    """

    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    latest_version: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        latest_version = self.latest_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if latest_version is not UNSET:
            field_dict["latestVersion"] = latest_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        latest_version = d.pop("latestVersion", UNSET)

        patch_community_packages_name_response_200_installed_nodes_item = cls(
            name=name,
            type_=type_,
            latest_version=latest_version,
        )

        patch_community_packages_name_response_200_installed_nodes_item.additional_properties = d
        return patch_community_packages_name_response_200_installed_nodes_item

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
