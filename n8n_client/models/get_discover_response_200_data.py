from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_discover_response_200_data_filters import GetDiscoverResponse200DataFilters
    from ..models.get_discover_response_200_data_resources import GetDiscoverResponse200DataResources


T = TypeVar("T", bound="GetDiscoverResponse200Data")


@_attrs_define
class GetDiscoverResponse200Data:
    """
    Attributes:
        scopes (list[str] | Unset): The API key's active scopes
        resources (GetDiscoverResponse200DataResources | Unset):
        filters (GetDiscoverResponse200DataFilters | Unset): Available query parameter filters. The values arrays
            reflect what the caller's scopes permit.
        spec_url (str | Unset): URL to the full OpenAPI specification
    """

    scopes: list[str] | Unset = UNSET
    resources: GetDiscoverResponse200DataResources | Unset = UNSET
    filters: GetDiscoverResponse200DataFilters | Unset = UNSET
    spec_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes

        resources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        spec_url = self.spec_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if resources is not UNSET:
            field_dict["resources"] = resources
        if filters is not UNSET:
            field_dict["filters"] = filters
        if spec_url is not UNSET:
            field_dict["specUrl"] = spec_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_discover_response_200_data_filters import GetDiscoverResponse200DataFilters
        from ..models.get_discover_response_200_data_resources import GetDiscoverResponse200DataResources

        d = dict(src_dict)
        scopes = cast(list[str], d.pop("scopes", UNSET))

        _resources = d.pop("resources", UNSET)
        resources: GetDiscoverResponse200DataResources | Unset
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = GetDiscoverResponse200DataResources.from_dict(_resources)

        _filters = d.pop("filters", UNSET)
        filters: GetDiscoverResponse200DataFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = GetDiscoverResponse200DataFilters.from_dict(_filters)

        spec_url = d.pop("specUrl", UNSET)

        get_discover_response_200_data = cls(
            scopes=scopes,
            resources=resources,
            filters=filters,
            spec_url=spec_url,
        )

        get_discover_response_200_data.additional_properties = d
        return get_discover_response_200_data

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
