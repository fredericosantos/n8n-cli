from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_projects_project_id_users_body_relations_item import PostProjectsProjectIdUsersBodyRelationsItem


T = TypeVar("T", bound="PostProjectsProjectIdUsersBody")


@_attrs_define
class PostProjectsProjectIdUsersBody:
    """
    Attributes:
        relations (list[PostProjectsProjectIdUsersBodyRelationsItem]): A list of userIds and roles to add to the
            project.
    """

    relations: list[PostProjectsProjectIdUsersBodyRelationsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        relations = []
        for relations_item_data in self.relations:
            relations_item = relations_item_data.to_dict()
            relations.append(relations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "relations": relations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_projects_project_id_users_body_relations_item import (
            PostProjectsProjectIdUsersBodyRelationsItem,
        )

        d = dict(src_dict)
        relations = []
        _relations = d.pop("relations")
        for relations_item_data in _relations:
            relations_item = PostProjectsProjectIdUsersBodyRelationsItem.from_dict(relations_item_data)

            relations.append(relations_item)

        post_projects_project_id_users_body = cls(
            relations=relations,
        )

        post_projects_project_id_users_body.additional_properties = d
        return post_projects_project_id_users_body

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
