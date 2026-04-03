from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_discover_response_200_data_filters_additional_property import (
        GetDiscoverResponse200DataFiltersAdditionalProperty,
    )


T = TypeVar("T", bound="GetDiscoverResponse200DataFilters")


@_attrs_define
class GetDiscoverResponse200DataFilters:
    """Available query parameter filters. The values arrays reflect what the caller's scopes permit."""

    additional_properties: dict[str, GetDiscoverResponse200DataFiltersAdditionalProperty] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_discover_response_200_data_filters_additional_property import (
            GetDiscoverResponse200DataFiltersAdditionalProperty,
        )

        d = dict(src_dict)
        get_discover_response_200_data_filters = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GetDiscoverResponse200DataFiltersAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        get_discover_response_200_data_filters.additional_properties = additional_properties
        return get_discover_response_200_data_filters

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> GetDiscoverResponse200DataFiltersAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: GetDiscoverResponse200DataFiltersAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
