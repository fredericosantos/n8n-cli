from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSourceControlPullResponse200Variables")


@_attrs_define
class PostSourceControlPullResponse200Variables:
    """
    Attributes:
        added (list[str] | Unset):
        changed (list[str] | Unset):
    """

    added: list[str] | Unset = UNSET
    changed: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added: list[str] | Unset = UNSET
        if not isinstance(self.added, Unset):
            added = self.added

        changed: list[str] | Unset = UNSET
        if not isinstance(self.changed, Unset):
            changed = self.changed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if added is not UNSET:
            field_dict["added"] = added
        if changed is not UNSET:
            field_dict["changed"] = changed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        added = cast(list[str], d.pop("added", UNSET))

        changed = cast(list[str], d.pop("changed", UNSET))

        post_source_control_pull_response_200_variables = cls(
            added=added,
            changed=changed,
        )

        post_source_control_pull_response_200_variables.additional_properties = d
        return post_source_control_pull_response_200_variables

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
