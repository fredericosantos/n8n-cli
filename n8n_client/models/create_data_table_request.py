from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_data_table_request_columns_item import CreateDataTableRequestColumnsItem


T = TypeVar("T", bound="CreateDataTableRequest")


@_attrs_define
class CreateDataTableRequest:
    """
    Attributes:
        name (str): Name of the data table
        columns (list[CreateDataTableRequestColumnsItem]): Column definitions for the table
    """

    name: str
    columns: list[CreateDataTableRequestColumnsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "columns": columns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_data_table_request_columns_item import CreateDataTableRequestColumnsItem

        d = dict(src_dict)
        name = d.pop("name")

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = CreateDataTableRequestColumnsItem.from_dict(columns_item_data)

            columns.append(columns_item)

        create_data_table_request = cls(
            name=name,
            columns=columns,
        )

        create_data_table_request.additional_properties = d
        return create_data_table_request

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
