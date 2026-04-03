from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_workflows_response_200_active_version_type_0_connections import (
        PostWorkflowsResponse200ActiveVersionType0Connections,
    )
    from ..models.post_workflows_response_200_active_version_type_0_nodes_item import (
        PostWorkflowsResponse200ActiveVersionType0NodesItem,
    )


T = TypeVar("T", bound="PostWorkflowsResponse200ActiveVersionType0")


@_attrs_define
class PostWorkflowsResponse200ActiveVersionType0:
    """
    Attributes:
        version_id (str | Unset): Unique identifier for this workflow version Example:
            7c6b9e3f-8d4a-4b2c-9f1e-6a5d3b8c7e4f.
        workflow_id (str | Unset): The workflow this version belongs to Example: 2tUt1wbLX592XDdX.
        nodes (list[PostWorkflowsResponse200ActiveVersionType0NodesItem] | Unset):
        connections (PostWorkflowsResponse200ActiveVersionType0Connections | Unset):  Example: {'Jira': {'main':
            [[{'node': 'Jira', 'type': 'main', 'index': 0}]]}}.
        authors (str | Unset): Comma-separated list of author IDs who contributed to this version Example: 1,2,3.
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    version_id: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    nodes: list[PostWorkflowsResponse200ActiveVersionType0NodesItem] | Unset = UNSET
    connections: PostWorkflowsResponse200ActiveVersionType0Connections | Unset = UNSET
    authors: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        version_id = self.version_id

        workflow_id = self.workflow_id

        nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()
                nodes.append(nodes_item)

        connections: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connections, Unset):
            connections = self.connections.to_dict()

        authors = self.authors

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if connections is not UNSET:
            field_dict["connections"] = connections
        if authors is not UNSET:
            field_dict["authors"] = authors
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_workflows_response_200_active_version_type_0_connections import (
            PostWorkflowsResponse200ActiveVersionType0Connections,
        )
        from ..models.post_workflows_response_200_active_version_type_0_nodes_item import (
            PostWorkflowsResponse200ActiveVersionType0NodesItem,
        )

        d = dict(src_dict)
        version_id = d.pop("versionId", UNSET)

        workflow_id = d.pop("workflowId", UNSET)

        _nodes = d.pop("nodes", UNSET)
        nodes: list[PostWorkflowsResponse200ActiveVersionType0NodesItem] | Unset = UNSET
        if _nodes is not UNSET:
            nodes = []
            for nodes_item_data in _nodes:
                nodes_item = PostWorkflowsResponse200ActiveVersionType0NodesItem.from_dict(nodes_item_data)

                nodes.append(nodes_item)

        _connections = d.pop("connections", UNSET)
        connections: PostWorkflowsResponse200ActiveVersionType0Connections | Unset
        if isinstance(_connections, Unset):
            connections = UNSET
        else:
            connections = PostWorkflowsResponse200ActiveVersionType0Connections.from_dict(_connections)

        authors = d.pop("authors", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        post_workflows_response_200_active_version_type_0 = cls(
            version_id=version_id,
            workflow_id=workflow_id,
            nodes=nodes,
            connections=connections,
            authors=authors,
            created_at=created_at,
            updated_at=updated_at,
        )

        return post_workflows_response_200_active_version_type_0
