from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VariableCreate")


@_attrs_define
class VariableCreate:
    """
    Attributes:
        key (str):
        value (str):  Example: test.
        id (str | Unset):
        type_ (str | Unset):
        project_id (None | str | Unset):  Example: VmwOO9HeTEj20kxM.
    """

    key: str
    value: str
    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    project_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        id = self.id

        type_ = self.type_

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

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
        if project_id is not UNSET:
            field_dict["projectId"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        value = d.pop("value")

        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("projectId", UNSET))

        variable_create = cls(
            key=key,
            value=value,
            id=id,
            type_=type_,
            project_id=project_id,
        )

        return variable_create
