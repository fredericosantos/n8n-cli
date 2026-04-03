from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_variables_response_200_data_item_project import GetVariablesResponse200DataItemProject


T = TypeVar("T", bound="GetVariablesResponse200DataItem")


@_attrs_define
class GetVariablesResponse200DataItem:
    """
    Attributes:
        key (str):
        value (str):  Example: test.
        id (str | Unset):
        type_ (str | Unset):
        project (GetVariablesResponse200DataItemProject | Unset):
    """

    key: str
    value: str
    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    project: GetVariablesResponse200DataItemProject | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        id = self.id

        type_ = self.type_

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_variables_response_200_data_item_project import GetVariablesResponse200DataItemProject

        d = dict(src_dict)
        key = d.pop("key")

        value = d.pop("value")

        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        _project = d.pop("project", UNSET)
        project: GetVariablesResponse200DataItemProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = GetVariablesResponse200DataItemProject.from_dict(_project)

        get_variables_response_200_data_item = cls(
            key=key,
            value=value,
            id=id,
            type_=type_,
            project=project,
        )

        return get_variables_response_200_data_item
