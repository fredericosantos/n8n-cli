from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_discover_response_200_data_resources_additional_property_endpoints_item import (
        GetDiscoverResponse200DataResourcesAdditionalPropertyEndpointsItem,
    )


T = TypeVar("T", bound="GetDiscoverResponse200DataResourcesAdditionalProperty")


@_attrs_define
class GetDiscoverResponse200DataResourcesAdditionalProperty:
    """
    Attributes:
        operations (list[str] | Unset):
        endpoints (list[GetDiscoverResponse200DataResourcesAdditionalPropertyEndpointsItem] | Unset):
    """

    operations: list[str] | Unset = UNSET
    endpoints: list[GetDiscoverResponse200DataResourcesAdditionalPropertyEndpointsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operations: list[str] | Unset = UNSET
        if not isinstance(self.operations, Unset):
            operations = self.operations

        endpoints: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.endpoints, Unset):
            endpoints = []
            for endpoints_item_data in self.endpoints:
                endpoints_item = endpoints_item_data.to_dict()
                endpoints.append(endpoints_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operations is not UNSET:
            field_dict["operations"] = operations
        if endpoints is not UNSET:
            field_dict["endpoints"] = endpoints

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_discover_response_200_data_resources_additional_property_endpoints_item import (
            GetDiscoverResponse200DataResourcesAdditionalPropertyEndpointsItem,
        )

        d = dict(src_dict)
        operations = cast(list[str], d.pop("operations", UNSET))

        _endpoints = d.pop("endpoints", UNSET)
        endpoints: list[GetDiscoverResponse200DataResourcesAdditionalPropertyEndpointsItem] | Unset = UNSET
        if _endpoints is not UNSET:
            endpoints = []
            for endpoints_item_data in _endpoints:
                endpoints_item = GetDiscoverResponse200DataResourcesAdditionalPropertyEndpointsItem.from_dict(
                    endpoints_item_data
                )

                endpoints.append(endpoints_item)

        get_discover_response_200_data_resources_additional_property = cls(
            operations=operations,
            endpoints=endpoints,
        )

        get_discover_response_200_data_resources_additional_property.additional_properties = d
        return get_discover_response_200_data_resources_additional_property

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
