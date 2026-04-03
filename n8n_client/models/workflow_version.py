from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node import Node
    from ..models.workflow_version_connections import WorkflowVersionConnections


T = TypeVar("T", bound="WorkflowVersion")


@_attrs_define
class WorkflowVersion:
    """
    Attributes:
        version_id (str): The version ID of this workflow snapshot Example: abc123-def456.
        workflow_id (str): The workflow ID this version belongs to Example: 2tUt1wbLX592XDdX.
        nodes (list[Node]): Nodes as they were in this version
        connections (WorkflowVersionConnections): Connections as they were in this version Example: {'Jira': {'main':
            [[{'node': 'Jira', 'type': 'main', 'index': 0}]]}}.
        authors (str): Authors who created this version Example: John Doe.
        name (None | str | Unset): Workflow name at this version Example: Workflow 1.
        description (None | str | Unset): Workflow description at this version
        created_at (datetime.datetime | Unset): When this version was created
        updated_at (datetime.datetime | Unset): When this version was last updated
    """

    version_id: str
    workflow_id: str
    nodes: list[Node]
    connections: WorkflowVersionConnections
    authors: str
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        version_id = self.version_id

        workflow_id = self.workflow_id

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        connections = self.connections.to_dict()

        authors = self.authors

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "versionId": version_id,
                "workflowId": workflow_id,
                "nodes": nodes,
                "connections": connections,
                "authors": authors,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node import Node
        from ..models.workflow_version_connections import WorkflowVersionConnections

        d = dict(src_dict)
        version_id = d.pop("versionId")

        workflow_id = d.pop("workflowId")

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = Node.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        connections = WorkflowVersionConnections.from_dict(d.pop("connections"))

        authors = d.pop("authors")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        workflow_version = cls(
            version_id=version_id,
            workflow_id=workflow_id,
            nodes=nodes,
            connections=connections,
            authors=authors,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
        )

        return workflow_version
