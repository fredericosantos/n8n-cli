from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostWorkflowsBodyActiveVersionType0NodesItemCredentials")


@_attrs_define
class PostWorkflowsBodyActiveVersionType0NodesItemCredentials:
    """
    Example:
        {'jiraSoftwareCloudApi': {'id': '35', 'name': 'jiraApi'}}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        post_workflows_body_active_version_type_0_nodes_item_credentials = cls()

        post_workflows_body_active_version_type_0_nodes_item_credentials.additional_properties = d
        return post_workflows_body_active_version_type_0_nodes_item_credentials

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
