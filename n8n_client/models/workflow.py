from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.active_version_type_0 import ActiveVersionType0
    from ..models.node import Node
    from ..models.shared_workflow import SharedWorkflow
    from ..models.tag import Tag
    from ..models.workflow_connections import WorkflowConnections
    from ..models.workflow_meta_type_0 import WorkflowMetaType0
    from ..models.workflow_pin_data_type_0 import WorkflowPinDataType0
    from ..models.workflow_settings import WorkflowSettings
    from ..models.workflow_static_data_type_1_type_0 import WorkflowStaticDataType1Type0


T = TypeVar("T", bound="Workflow")


@_attrs_define
class Workflow:
    """
    Attributes:
        name (str):  Example: Workflow 1.
        nodes (list[Node]):
        connections (WorkflowConnections):  Example: {'Jira': {'main': [[{'node': 'Jira', 'type': 'main', 'index':
            0}]]}}.
        settings (WorkflowSettings):
        id (str | Unset):  Example: 2tUt1wbLX592XDdX.
        description (str | Unset): Description of the workflow Example: My workflow description.
        active (bool | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        is_archived (bool | Unset):
        version_id (str | Unset): Current version identifier used for optimistic locking
        trigger_count (int | Unset): Number of active trigger nodes in the workflow
        static_data (None | str | Unset | WorkflowStaticDataType1Type0):  Example: {'lastId': 1}.
        pin_data (None | Unset | WorkflowPinDataType0): Pinned sample data for nodes, keyed by node name
        meta (None | Unset | WorkflowMetaType0): Workflow metadata such as template information
        tags (list[Tag] | Unset):
        shared (list[SharedWorkflow] | Unset):
        active_version (ActiveVersionType0 | None | Unset):
    """

    name: str
    nodes: list[Node]
    connections: WorkflowConnections
    settings: WorkflowSettings
    id: str | Unset = UNSET
    description: str | Unset = UNSET
    active: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    is_archived: bool | Unset = UNSET
    version_id: str | Unset = UNSET
    trigger_count: int | Unset = UNSET
    static_data: None | str | Unset | WorkflowStaticDataType1Type0 = UNSET
    pin_data: None | Unset | WorkflowPinDataType0 = UNSET
    meta: None | Unset | WorkflowMetaType0 = UNSET
    tags: list[Tag] | Unset = UNSET
    shared: list[SharedWorkflow] | Unset = UNSET
    active_version: ActiveVersionType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.active_version_type_0 import ActiveVersionType0
        from ..models.workflow_meta_type_0 import WorkflowMetaType0
        from ..models.workflow_pin_data_type_0 import WorkflowPinDataType0
        from ..models.workflow_static_data_type_1_type_0 import WorkflowStaticDataType1Type0

        name = self.name

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        connections = self.connections.to_dict()

        settings = self.settings.to_dict()

        id = self.id

        description = self.description

        active = self.active

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        is_archived = self.is_archived

        version_id = self.version_id

        trigger_count = self.trigger_count

        static_data: dict[str, Any] | None | str | Unset
        if isinstance(self.static_data, Unset):
            static_data = UNSET
        elif isinstance(self.static_data, WorkflowStaticDataType1Type0):
            static_data = self.static_data.to_dict()
        else:
            static_data = self.static_data

        pin_data: dict[str, Any] | None | Unset
        if isinstance(self.pin_data, Unset):
            pin_data = UNSET
        elif isinstance(self.pin_data, WorkflowPinDataType0):
            pin_data = self.pin_data.to_dict()
        else:
            pin_data = self.pin_data

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, WorkflowMetaType0):
            meta = self.meta.to_dict()
        else:
            meta = self.meta

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        shared: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shared, Unset):
            shared = []
            for shared_item_data in self.shared:
                shared_item = shared_item_data.to_dict()
                shared.append(shared_item)

        active_version: dict[str, Any] | None | Unset
        if isinstance(self.active_version, Unset):
            active_version = UNSET
        elif isinstance(self.active_version, ActiveVersionType0):
            active_version = self.active_version.to_dict()
        else:
            active_version = self.active_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "nodes": nodes,
                "connections": connections,
                "settings": settings,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if active is not UNSET:
            field_dict["active"] = active
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if trigger_count is not UNSET:
            field_dict["triggerCount"] = trigger_count
        if static_data is not UNSET:
            field_dict["staticData"] = static_data
        if pin_data is not UNSET:
            field_dict["pinData"] = pin_data
        if meta is not UNSET:
            field_dict["meta"] = meta
        if tags is not UNSET:
            field_dict["tags"] = tags
        if shared is not UNSET:
            field_dict["shared"] = shared
        if active_version is not UNSET:
            field_dict["activeVersion"] = active_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.active_version_type_0 import ActiveVersionType0
        from ..models.node import Node
        from ..models.shared_workflow import SharedWorkflow
        from ..models.tag import Tag
        from ..models.workflow_connections import WorkflowConnections
        from ..models.workflow_meta_type_0 import WorkflowMetaType0
        from ..models.workflow_pin_data_type_0 import WorkflowPinDataType0
        from ..models.workflow_settings import WorkflowSettings
        from ..models.workflow_static_data_type_1_type_0 import WorkflowStaticDataType1Type0

        d = dict(src_dict)
        name = d.pop("name")

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = Node.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        connections = WorkflowConnections.from_dict(d.pop("connections"))

        settings = WorkflowSettings.from_dict(d.pop("settings"))

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        active = d.pop("active", UNSET)

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

        is_archived = d.pop("isArchived", UNSET)

        version_id = d.pop("versionId", UNSET)

        trigger_count = d.pop("triggerCount", UNSET)

        def _parse_static_data(data: object) -> None | str | Unset | WorkflowStaticDataType1Type0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                static_data_type_1_type_0 = WorkflowStaticDataType1Type0.from_dict(data)

                return static_data_type_1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | str | Unset | WorkflowStaticDataType1Type0, data)

        static_data = _parse_static_data(d.pop("staticData", UNSET))

        def _parse_pin_data(data: object) -> None | Unset | WorkflowPinDataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pin_data_type_0 = WorkflowPinDataType0.from_dict(data)

                return pin_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowPinDataType0, data)

        pin_data = _parse_pin_data(d.pop("pinData", UNSET))

        def _parse_meta(data: object) -> None | Unset | WorkflowMetaType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = WorkflowMetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WorkflowMetaType0, data)

        meta = _parse_meta(d.pop("meta", UNSET))

        _tags = d.pop("tags", UNSET)
        tags: list[Tag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = Tag.from_dict(tags_item_data)

                tags.append(tags_item)

        _shared = d.pop("shared", UNSET)
        shared: list[SharedWorkflow] | Unset = UNSET
        if _shared is not UNSET:
            shared = []
            for shared_item_data in _shared:
                shared_item = SharedWorkflow.from_dict(shared_item_data)

                shared.append(shared_item)

        def _parse_active_version(data: object) -> ActiveVersionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasactive_version_type_0 = ActiveVersionType0.from_dict(data)

                return componentsschemasactive_version_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActiveVersionType0 | None | Unset, data)

        active_version = _parse_active_version(d.pop("activeVersion", UNSET))

        workflow = cls(
            name=name,
            nodes=nodes,
            connections=connections,
            settings=settings,
            id=id,
            description=description,
            active=active,
            created_at=created_at,
            updated_at=updated_at,
            is_archived=is_archived,
            version_id=version_id,
            trigger_count=trigger_count,
            static_data=static_data,
            pin_data=pin_data,
            meta=meta,
            tags=tags,
            shared=shared,
            active_version=active_version,
        )

        return workflow
