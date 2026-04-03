from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_data_table_rows_body_filter_type import UpdateDataTableRowsBodyFilterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_data_table_rows_body_filter_filters_item import UpdateDataTableRowsBodyFilterFiltersItem


T = TypeVar("T", bound="UpdateDataTableRowsBodyFilter")


@_attrs_define
class UpdateDataTableRowsBodyFilter:
    """Filter conditions to match rows for update

    Attributes:
        filters (list[UpdateDataTableRowsBodyFilterFiltersItem]):
        type_ (UpdateDataTableRowsBodyFilterType | Unset):  Default: UpdateDataTableRowsBodyFilterType.AND.
    """

    filters: list[UpdateDataTableRowsBodyFilterFiltersItem]
    type_: UpdateDataTableRowsBodyFilterType | Unset = UpdateDataTableRowsBodyFilterType.AND
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_data_table_rows_body_filter_filters_item import UpdateDataTableRowsBodyFilterFiltersItem

        d = dict(src_dict)
        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = UpdateDataTableRowsBodyFilterFiltersItem.from_dict(filters_item_data)

            filters.append(filters_item)

        _type_ = d.pop("type", UNSET)
        type_: UpdateDataTableRowsBodyFilterType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UpdateDataTableRowsBodyFilterType(_type_)

        update_data_table_rows_body_filter = cls(
            filters=filters,
            type_=type_,
        )

        update_data_table_rows_body_filter.additional_properties = d
        return update_data_table_rows_body_filter

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
