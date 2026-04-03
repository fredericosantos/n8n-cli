from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetDiscoverResponse200DataResourcesAdditionalPropertyEndpointsItemRequestSchema")


@_attrs_define
class GetDiscoverResponse200DataResourcesAdditionalPropertyEndpointsItemRequestSchema:
    """Request body schema (only present when include=schemas and the endpoint accepts a request body)."""

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        get_discover_response_200_data_resources_additional_property_endpoints_item_request_schema = cls()

        get_discover_response_200_data_resources_additional_property_endpoints_item_request_schema.additional_properties = d
        return get_discover_response_200_data_resources_additional_property_endpoints_item_request_schema

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
