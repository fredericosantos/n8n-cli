from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_source_control_pull_body_auto_publish import PostSourceControlPullBodyAutoPublish
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_source_control_pull_body_variables import PostSourceControlPullBodyVariables


T = TypeVar("T", bound="PostSourceControlPullBody")


@_attrs_define
class PostSourceControlPullBody:
    """
    Attributes:
        force (bool | Unset):  Example: True.
        auto_publish (PostSourceControlPullBodyAutoPublish | Unset): Controls automatic workflow publishing after
            import:
            - `none`: Keep workflows in their local published state (default)
            - `all`: Publish all imported workflows
            - `published`: Publish only workflows that were published locally before import
             Default: PostSourceControlPullBodyAutoPublish.NONE. Example: published.
        variables (PostSourceControlPullBodyVariables | Unset):  Example: {'foo': 'bar'}.
    """

    force: bool | Unset = UNSET
    auto_publish: PostSourceControlPullBodyAutoPublish | Unset = PostSourceControlPullBodyAutoPublish.NONE
    variables: PostSourceControlPullBodyVariables | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        force = self.force

        auto_publish: str | Unset = UNSET
        if not isinstance(self.auto_publish, Unset):
            auto_publish = self.auto_publish.value

        variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if force is not UNSET:
            field_dict["force"] = force
        if auto_publish is not UNSET:
            field_dict["autoPublish"] = auto_publish
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_source_control_pull_body_variables import PostSourceControlPullBodyVariables

        d = dict(src_dict)
        force = d.pop("force", UNSET)

        _auto_publish = d.pop("autoPublish", UNSET)
        auto_publish: PostSourceControlPullBodyAutoPublish | Unset
        if isinstance(_auto_publish, Unset):
            auto_publish = UNSET
        else:
            auto_publish = PostSourceControlPullBodyAutoPublish(_auto_publish)

        _variables = d.pop("variables", UNSET)
        variables: PostSourceControlPullBodyVariables | Unset
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = PostSourceControlPullBodyVariables.from_dict(_variables)

        post_source_control_pull_body = cls(
            force=force,
            auto_publish=auto_publish,
            variables=variables,
        )

        post_source_control_pull_body.additional_properties = d
        return post_source_control_pull_body

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
