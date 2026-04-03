from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_result_tags_mappings_item import ImportResultTagsMappingsItem
    from ..models.import_result_tags_tags_item import ImportResultTagsTagsItem


T = TypeVar("T", bound="ImportResultTags")


@_attrs_define
class ImportResultTags:
    """
    Attributes:
        tags (list[ImportResultTagsTagsItem] | Unset):
        mappings (list[ImportResultTagsMappingsItem] | Unset):
    """

    tags: list[ImportResultTagsTagsItem] | Unset = UNSET
    mappings: list[ImportResultTagsMappingsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        mappings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mappings, Unset):
            mappings = []
            for mappings_item_data in self.mappings:
                mappings_item = mappings_item_data.to_dict()
                mappings.append(mappings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags
        if mappings is not UNSET:
            field_dict["mappings"] = mappings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_result_tags_mappings_item import ImportResultTagsMappingsItem
        from ..models.import_result_tags_tags_item import ImportResultTagsTagsItem

        d = dict(src_dict)
        _tags = d.pop("tags", UNSET)
        tags: list[ImportResultTagsTagsItem] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = ImportResultTagsTagsItem.from_dict(tags_item_data)

                tags.append(tags_item)

        _mappings = d.pop("mappings", UNSET)
        mappings: list[ImportResultTagsMappingsItem] | Unset = UNSET
        if _mappings is not UNSET:
            mappings = []
            for mappings_item_data in _mappings:
                mappings_item = ImportResultTagsMappingsItem.from_dict(mappings_item_data)

                mappings.append(mappings_item)

        import_result_tags = cls(
            tags=tags,
            mappings=mappings,
        )

        import_result_tags.additional_properties = d
        return import_result_tags

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
