from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PutExecutionsIdTagsBodyItem")


@_attrs_define
class PutExecutionsIdTagsBodyItem:
    """
    Attributes:
        id (str):  Example: 2tUt1wbLX592XDdX.
    """

    id: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        put_executions_id_tags_body_item = cls(
            id=id,
        )

        return put_executions_id_tags_body_item
