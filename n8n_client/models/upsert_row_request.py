from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.upsert_row_request_data import UpsertRowRequestData
    from ..models.upsert_row_request_filter import UpsertRowRequestFilter


T = TypeVar("T", bound="UpsertRowRequest")


@_attrs_define
class UpsertRowRequest:
    """
    Attributes:
        filter_ (UpsertRowRequestFilter): Filter conditions to match existing row. If no row matches, a new row is
            inserted.
        data (UpsertRowRequestData): Column values for the row
        return_data (bool | Unset): If true, return the upserted row; if false, return true on success Default: False.
        dry_run (bool | Unset): If true, preview changes without persisting them Default: False.
    """

    filter_: UpsertRowRequestFilter
    data: UpsertRowRequestData
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
        from ..models.upsert_row_request_data import UpsertRowRequestData
        from ..models.upsert_row_request_filter import UpsertRowRequestFilter

        d = dict(src_dict)
        filter_ = UpsertRowRequestFilter.from_dict(d.pop("filter"))

        data = UpsertRowRequestData.from_dict(d.pop("data"))

        return_data = d.pop("returnData", UNSET)

        dry_run = d.pop("dryRun", UNSET)

        upsert_row_request = cls(
            filter_=filter_,
            data=data,
            return_data=return_data,
            dry_run=dry_run,
        )

        upsert_row_request.additional_properties = d
        return upsert_row_request

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
