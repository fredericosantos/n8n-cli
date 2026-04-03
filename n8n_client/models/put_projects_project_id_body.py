from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutProjectsProjectIdBody")


@_attrs_define
class PutProjectsProjectIdBody:
    """
    Attributes:
        name (str):
        id (str | Unset):
        type_ (str | Unset):
    """

    name: str
    id: str | Unset = UNSET
    type_: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        put_projects_project_id_body = cls(
            name=name,
            id=id,
            type_=type_,
        )

        return put_projects_project_id_body
