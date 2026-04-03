from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.create_data_table_response_201_columns_item import CreateDataTableResponse201ColumnsItem


T = TypeVar("T", bound="CreateDataTableResponse201")


@_attrs_define
class CreateDataTableResponse201:
    """
    Attributes:
        id (str): Unique identifier for the data table
        name (str): Name of the data table
        columns (list[CreateDataTableResponse201ColumnsItem]): Column definitions
        project_id (str): ID of the project this table belongs to
        created_at (datetime.datetime): Timestamp when the table was created
        updated_at (datetime.datetime): Timestamp when the table was last updated
    """

    id: str
    name: str
    columns: list[CreateDataTableResponse201ColumnsItem]
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
        from ..models.create_data_table_response_201_columns_item import CreateDataTableResponse201ColumnsItem

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = CreateDataTableResponse201ColumnsItem.from_dict(columns_item_data)

            columns.append(columns_item)

        project_id = d.pop("projectId")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        create_data_table_response_201 = cls(
            id=id,
            name=name,
            columns=columns,
            project_id=project_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        create_data_table_response_201.additional_properties = d
        return create_data_table_response_201

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
