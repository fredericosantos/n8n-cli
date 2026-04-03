from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostWorkflowsIdActivateBody")


@_attrs_define
class PostWorkflowsIdActivateBody:
    """
    Attributes:
        version_id (str | Unset): The specific version ID to activate or publish. If not provided, the latest version is
            used.
        name (str | Unset): Optional name for the workflow version during activation.
        description (str | Unset): Optional description for the workflow version during activation.
    """

    version_id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version_id = self.version_id

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version_id = d.pop("versionId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        post_workflows_id_activate_body = cls(
            version_id=version_id,
            name=name,
            description=description,
        )

        post_workflows_id_activate_body.additional_properties = d
        return post_workflows_id_activate_body

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
