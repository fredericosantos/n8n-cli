from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.insert_data_table_rows_body_return_type import InsertDataTableRowsBodyReturnType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.insert_data_table_rows_body_data_item import InsertDataTableRowsBodyDataItem


T = TypeVar("T", bound="InsertDataTableRowsBody")


@_attrs_define
class InsertDataTableRowsBody:
    """
    Attributes:
        data (list[InsertDataTableRowsBodyDataItem]): Array of rows to insert. Each row is an object with column names
            as keys.
        return_type (InsertDataTableRowsBodyReturnType | Unset): - count: Return only the number of rows inserted
            - id: Return an array of inserted row IDs
            - all: Return the full row data for all inserted rows
             Default: InsertDataTableRowsBodyReturnType.COUNT.
    """

    data: list[InsertDataTableRowsBodyDataItem]
    return_type: InsertDataTableRowsBodyReturnType | Unset = InsertDataTableRowsBodyReturnType.COUNT
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        return_type: str | Unset = UNSET
        if not isinstance(self.return_type, Unset):
            return_type = self.return_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if return_type is not UNSET:
            field_dict["returnType"] = return_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.insert_data_table_rows_body_data_item import InsertDataTableRowsBodyDataItem

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = InsertDataTableRowsBodyDataItem.from_dict(data_item_data)

            data.append(data_item)

        _return_type = d.pop("returnType", UNSET)
        return_type: InsertDataTableRowsBodyReturnType | Unset
        if isinstance(_return_type, Unset):
            return_type = UNSET
        else:
            return_type = InsertDataTableRowsBodyReturnType(_return_type)

        insert_data_table_rows_body = cls(
            data=data,
            return_type=return_type,
        )

        insert_data_table_rows_body.additional_properties = d
        return insert_data_table_rows_body

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
