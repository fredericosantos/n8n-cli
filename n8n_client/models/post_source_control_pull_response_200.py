from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_source_control_pull_response_200_credentials_item import (
        PostSourceControlPullResponse200CredentialsItem,
    )
    from ..models.post_source_control_pull_response_200_tags import PostSourceControlPullResponse200Tags
    from ..models.post_source_control_pull_response_200_variables import PostSourceControlPullResponse200Variables
    from ..models.post_source_control_pull_response_200_workflows_item import (
        PostSourceControlPullResponse200WorkflowsItem,
    )


T = TypeVar("T", bound="PostSourceControlPullResponse200")


@_attrs_define
class PostSourceControlPullResponse200:
    """
    Attributes:
        variables (PostSourceControlPullResponse200Variables | Unset):
        credentials (list[PostSourceControlPullResponse200CredentialsItem] | Unset):
        workflows (list[PostSourceControlPullResponse200WorkflowsItem] | Unset):
        tags (PostSourceControlPullResponse200Tags | Unset):
    """

    variables: PostSourceControlPullResponse200Variables | Unset = UNSET
    credentials: list[PostSourceControlPullResponse200CredentialsItem] | Unset = UNSET
    workflows: list[PostSourceControlPullResponse200WorkflowsItem] | Unset = UNSET
    tags: PostSourceControlPullResponse200Tags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()

        credentials: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = []
            for credentials_item_data in self.credentials:
                credentials_item = credentials_item_data.to_dict()
                credentials.append(credentials_item)

        workflows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.workflows, Unset):
            workflows = []
            for workflows_item_data in self.workflows:
                workflows_item = workflows_item_data.to_dict()
                workflows.append(workflows_item)

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if variables is not UNSET:
            field_dict["variables"] = variables
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if workflows is not UNSET:
            field_dict["workflows"] = workflows
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_source_control_pull_response_200_credentials_item import (
            PostSourceControlPullResponse200CredentialsItem,
        )
        from ..models.post_source_control_pull_response_200_tags import PostSourceControlPullResponse200Tags
        from ..models.post_source_control_pull_response_200_variables import PostSourceControlPullResponse200Variables
        from ..models.post_source_control_pull_response_200_workflows_item import (
            PostSourceControlPullResponse200WorkflowsItem,
        )

        d = dict(src_dict)
        _variables = d.pop("variables", UNSET)
        variables: PostSourceControlPullResponse200Variables | Unset
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = PostSourceControlPullResponse200Variables.from_dict(_variables)

        _credentials = d.pop("credentials", UNSET)
        credentials: list[PostSourceControlPullResponse200CredentialsItem] | Unset = UNSET
        if _credentials is not UNSET:
            credentials = []
            for credentials_item_data in _credentials:
                credentials_item = PostSourceControlPullResponse200CredentialsItem.from_dict(credentials_item_data)

                credentials.append(credentials_item)

        _workflows = d.pop("workflows", UNSET)
        workflows: list[PostSourceControlPullResponse200WorkflowsItem] | Unset = UNSET
        if _workflows is not UNSET:
            workflows = []
            for workflows_item_data in _workflows:
                workflows_item = PostSourceControlPullResponse200WorkflowsItem.from_dict(workflows_item_data)

                workflows.append(workflows_item)

        _tags = d.pop("tags", UNSET)
        tags: PostSourceControlPullResponse200Tags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = PostSourceControlPullResponse200Tags.from_dict(_tags)

        post_source_control_pull_response_200 = cls(
            variables=variables,
            credentials=credentials,
            workflows=workflows,
            tags=tags,
        )

        post_source_control_pull_response_200.additional_properties = d
        return post_source_control_pull_response_200

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
