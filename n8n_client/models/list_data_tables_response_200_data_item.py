from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.list_data_tables_response_200_data_item_columns_item import (
        ListDataTablesResponse200DataItemColumnsItem,
    )


T = TypeVar("T", bound="ListDataTablesResponse200DataItem")


@_attrs_define
class ListDataTablesResponse200DataItem:
    """
    Attributes:
        id (str): Unique identifier for the data table
        name (str): Name of the data table
        columns (list[ListDataTablesResponse200DataItemColumnsItem]): Column definitions
        project_id (str): ID of the project this table belongs to
        created_at (datetime.datetime): Timestamp when the table was created
        updated_at (datetime.datetime): Timestamp when the table was last updated
    """

    id: str
    name: str
    columns: list[ListDataTablesResponse200DataItemColumnsItem]
    project_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)

        project_id = self.project_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "columns": columns,
                "projectId": project_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_data_tables_response_200_data_item_columns_item import (
            ListDataTablesResponse200DataItemColumnsItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = ListDataTablesResponse200DataItemColumnsItem.from_dict(columns_item_data)

            columns.append(columns_item)

        project_id = d.pop("projectId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        list_data_tables_response_200_data_item = cls(
            id=id,
            name=name,
            columns=columns,
            project_id=project_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        list_data_tables_response_200_data_item.additional_properties = d
        return list_data_tables_response_200_data_item

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
