from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_discover_response_200_data_resources_additional_property_endpoints_item_request_schema import (
        GetDiscoverResponse200DataResourcesAdditionalPropertyEndpointsItemRequestSchema,
    )


T = TypeVar("T", bound="GetDiscoverResponse200DataResourcesAdditionalPropertyEndpointsItem")


@_attrs_define
class GetDiscoverResponse200DataResourcesAdditionalPropertyEndpointsItem:
    """
    Attributes:
        method (str | Unset):
        path (str | Unset):
        operation_id (str | Unset):
        request_schema (GetDiscoverResponse200DataResourcesAdditionalPropertyEndpointsItemRequestSchema | Unset):
            Request body schema (only present when include=schemas and the endpoint accepts a request body).
    """

    method: str | Unset = UNSET
    path: str | Unset = UNSET
    operation_id: str | Unset = UNSET
    request_schema: GetDiscoverResponse200DataResourcesAdditionalPropertyEndpointsItemRequestSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method

        path = self.path

        operation_id = self.operation_id

        request_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request_schema, Unset):
            request_schema = self.request_schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if path is not UNSET:
            field_dict["path"] = path
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id
        if request_schema is not UNSET:
            field_dict["requestSchema"] = request_schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_discover_response_200_data_resources_additional_property_endpoints_item_request_schema import (
            GetDiscoverResponse200DataResourcesAdditionalPropertyEndpointsItemRequestSchema,
        )

        d = dict(src_dict)
        method = d.pop("method", UNSET)

        path = d.pop("path", UNSET)

        operation_id = d.pop("operationId", UNSET)

        _request_schema = d.pop("requestSchema", UNSET)
        request_schema: GetDiscoverResponse200DataResourcesAdditionalPropertyEndpointsItemRequestSchema | Unset
        if isinstance(_request_schema, Unset):
            request_schema = UNSET
        else:
            request_schema = GetDiscoverResponse200DataResourcesAdditionalPropertyEndpointsItemRequestSchema.from_dict(
                _request_schema
            )

        get_discover_response_200_data_resources_additional_property_endpoints_item = cls(
            method=method,
            path=path,
            operation_id=operation_id,
            request_schema=request_schema,
        )

        get_discover_response_200_data_resources_additional_property_endpoints_item.additional_properties = d
        return get_discover_response_200_data_resources_additional_property_endpoints_item

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
