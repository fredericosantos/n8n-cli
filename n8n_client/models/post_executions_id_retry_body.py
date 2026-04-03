from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostExecutionsIdRetryBody")


@_attrs_define
class PostExecutionsIdRetryBody:
    """
    Attributes:
        load_workflow (bool | Unset): Whether to load the currently saved workflow to execute instead of the one saved
            at the time of the execution. If set to true, it will retry with the latest version of the workflow.
    """

    load_workflow: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        load_workflow = self.load_workflow

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if load_workflow is not UNSET:
            field_dict["loadWorkflow"] = load_workflow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        load_workflow = d.pop("loadWorkflow", UNSET)

        post_executions_id_retry_body = cls(
            load_workflow=load_workflow,
        )

        post_executions_id_retry_body.additional_properties = d
        return post_executions_id_retry_body

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
