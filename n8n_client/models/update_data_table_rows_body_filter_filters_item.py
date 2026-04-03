from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_data_table_rows_body_filter_filters_item_condition import (
    UpdateDataTableRowsBodyFilterFiltersItemCondition,
)

T = TypeVar("T", bound="UpdateDataTableRowsBodyFilterFiltersItem")


@_attrs_define
class UpdateDataTableRowsBodyFilterFiltersItem:
    """
    Attributes:
        column_name (str):
        condition (UpdateDataTableRowsBodyFilterFiltersItemCondition):
        value (Any):
    """

    column_name: str
    condition: UpdateDataTableRowsBodyFilterFiltersItemCondition
    value: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column_name = self.column_name

        condition = self.condition.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "columnName": column_name,
                "condition": condition,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column_name = d.pop("columnName")

        condition = UpdateDataTableRowsBodyFilterFiltersItemCondition(d.pop("condition"))

        value = d.pop("value")

        update_data_table_rows_body_filter_filters_item = cls(
            column_name=column_name,
            condition=condition,
            value=value,
        )

        update_data_table_rows_body_filter_filters_item.additional_properties = d
        return update_data_table_rows_body_filter_filters_item

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
