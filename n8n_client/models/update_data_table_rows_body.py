from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_data_table_rows_body_data import UpdateDataTableRowsBodyData
    from ..models.update_data_table_rows_body_filter import UpdateDataTableRowsBodyFilter


T = TypeVar("T", bound="UpdateDataTableRowsBody")


@_attrs_define
class UpdateDataTableRowsBody:
    """
    Attributes:
        filter_ (UpdateDataTableRowsBodyFilter): Filter conditions to match rows for update
        data (UpdateDataTableRowsBodyData): Column values to update
        return_data (bool | Unset): If true, return the updated rows; if false, return true on success Default: False.
        dry_run (bool | Unset): If true, preview changes without persisting them Default: False.
    """

    filter_: UpdateDataTableRowsBodyFilter
    data: UpdateDataTableRowsBodyData
    return_data: bool | Unset = False
    dry_run: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_ = self.filter_.to_dict()

        data = self.data.to_dict()

        return_data = self.return_data

        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter": filter_,
                "data": data,
            }
        )
        if return_data is not UNSET:
            field_dict["returnData"] = return_data
        if dry_run is not UNSET:
            field_dict["dryRun"] = dry_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_data_table_rows_body_data import UpdateDataTableRowsBodyData
        from ..models.update_data_table_rows_body_filter import UpdateDataTableRowsBodyFilter

        d = dict(src_dict)
        filter_ = UpdateDataTableRowsBodyFilter.from_dict(d.pop("filter"))

        data = UpdateDataTableRowsBodyData.from_dict(d.pop("data"))

        return_data = d.pop("returnData", UNSET)

        dry_run = d.pop("dryRun", UNSET)

        update_data_table_rows_body = cls(
            filter_=filter_,
            data=data,
            return_data=return_data,
            dry_run=dry_run,
        )

        update_data_table_rows_body.additional_properties = d
        return update_data_table_rows_body

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
