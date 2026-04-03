from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.upsert_row_request_filter_type import UpsertRowRequestFilterType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.upsert_row_request_filter_filters_item import UpsertRowRequestFilterFiltersItem


T = TypeVar("T", bound="UpsertRowRequestFilter")


@_attrs_define
class UpsertRowRequestFilter:
    """Filter conditions to match existing row. If no row matches, a new row is inserted.

    Attributes:
        filters (list[UpsertRowRequestFilterFiltersItem]):
        type_ (UpsertRowRequestFilterType | Unset):  Default: UpsertRowRequestFilterType.AND.
    """

    filters: list[UpsertRowRequestFilterFiltersItem]
    type_: UpsertRowRequestFilterType | Unset = UpsertRowRequestFilterType.AND
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
        from ..models.upsert_row_request_filter_filters_item import UpsertRowRequestFilterFiltersItem

        d = dict(src_dict)
        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = UpsertRowRequestFilterFiltersItem.from_dict(filters_item_data)

            filters.append(filters_item)

        _type_ = d.pop("type", UNSET)
        type_: UpsertRowRequestFilterType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UpsertRowRequestFilterType(_type_)

        upsert_row_request_filter = cls(
            filters=filters,
            type_=type_,
        )

        upsert_row_request_filter.additional_properties = d
        return upsert_row_request_filter

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
