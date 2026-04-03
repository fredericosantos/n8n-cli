from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_data_table_response_201_columns_item_type import CreateDataTableResponse201ColumnsItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateDataTableResponse201ColumnsItem")


@_attrs_define
class CreateDataTableResponse201ColumnsItem:
    """
    Attributes:
        id (str | Unset): Column ID
        name (str | Unset): Column name
        type_ (CreateDataTableResponse201ColumnsItemType | Unset): Column data type
        index (int | Unset): Column position
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: CreateDataTableResponse201ColumnsItemType | Unset = UNSET
    index: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        index = self.index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if index is not UNSET:
            field_dict["index"] = index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CreateDataTableResponse201ColumnsItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CreateDataTableResponse201ColumnsItemType(_type_)

        index = d.pop("index", UNSET)

        create_data_table_response_201_columns_item = cls(
            id=id,
            name=name,
            type_=type_,
            index=index,
        )

        create_data_table_response_201_columns_item.additional_properties = d
        return create_data_table_response_201_columns_item

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
