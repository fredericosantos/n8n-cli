from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_result_credentials_item import ImportResultCredentialsItem
    from ..models.import_result_tags import ImportResultTags
    from ..models.import_result_variables import ImportResultVariables
    from ..models.import_result_workflows_item import ImportResultWorkflowsItem


T = TypeVar("T", bound="ImportResult")


@_attrs_define
class ImportResult:
    """
    Attributes:
        variables (ImportResultVariables | Unset):
        credentials (list[ImportResultCredentialsItem] | Unset):
        workflows (list[ImportResultWorkflowsItem] | Unset):
        tags (ImportResultTags | Unset):
    """

    variables: ImportResultVariables | Unset = UNSET
    credentials: list[ImportResultCredentialsItem] | Unset = UNSET
    workflows: list[ImportResultWorkflowsItem] | Unset = UNSET
    tags: ImportResultTags | Unset = UNSET
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
        from ..models.import_result_credentials_item import ImportResultCredentialsItem
        from ..models.import_result_tags import ImportResultTags
        from ..models.import_result_variables import ImportResultVariables
        from ..models.import_result_workflows_item import ImportResultWorkflowsItem

        d = dict(src_dict)
        _variables = d.pop("variables", UNSET)
        variables: ImportResultVariables | Unset
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = ImportResultVariables.from_dict(_variables)

        _credentials = d.pop("credentials", UNSET)
        credentials: list[ImportResultCredentialsItem] | Unset = UNSET
        if _credentials is not UNSET:
            credentials = []
            for credentials_item_data in _credentials:
                credentials_item = ImportResultCredentialsItem.from_dict(credentials_item_data)

                credentials.append(credentials_item)

        _workflows = d.pop("workflows", UNSET)
        workflows: list[ImportResultWorkflowsItem] | Unset = UNSET
        if _workflows is not UNSET:
            workflows = []
            for workflows_item_data in _workflows:
                workflows_item = ImportResultWorkflowsItem.from_dict(workflows_item_data)

                workflows.append(workflows_item)

        _tags = d.pop("tags", UNSET)
        tags: ImportResultTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = ImportResultTags.from_dict(_tags)

        import_result = cls(
            variables=variables,
            credentials=credentials,
            workflows=workflows,
            tags=tags,
        )

        import_result.additional_properties = d
        return import_result

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
