from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_audit_body_additional_options_categories_item import PostAuditBodyAdditionalOptionsCategoriesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostAuditBodyAdditionalOptions")


@_attrs_define
class PostAuditBodyAdditionalOptions:
    """
    Attributes:
        days_abandoned_workflow (int | Unset): Days for a workflow to be considered abandoned if not executed
        categories (list[PostAuditBodyAdditionalOptionsCategoriesItem] | Unset):
    """

    days_abandoned_workflow: int | Unset = UNSET
    categories: list[PostAuditBodyAdditionalOptionsCategoriesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        days_abandoned_workflow = self.days_abandoned_workflow

        categories: list[str] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.value
                categories.append(categories_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if days_abandoned_workflow is not UNSET:
            field_dict["daysAbandonedWorkflow"] = days_abandoned_workflow
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        days_abandoned_workflow = d.pop("daysAbandonedWorkflow", UNSET)

        _categories = d.pop("categories", UNSET)
        categories: list[PostAuditBodyAdditionalOptionsCategoriesItem] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = PostAuditBodyAdditionalOptionsCategoriesItem(categories_item_data)

                categories.append(categories_item)

        post_audit_body_additional_options = cls(
            days_abandoned_workflow=days_abandoned_workflow,
            categories=categories,
        )

        post_audit_body_additional_options.additional_properties = d
        return post_audit_body_additional_options

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
