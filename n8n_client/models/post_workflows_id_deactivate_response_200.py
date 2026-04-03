from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_workflows_id_deactivate_response_200_active_version_type_0 import (
        PostWorkflowsIdDeactivateResponse200ActiveVersionType0,
    )
    from ..models.post_workflows_id_deactivate_response_200_connections import (
        PostWorkflowsIdDeactivateResponse200Connections,
    )
    from ..models.post_workflows_id_deactivate_response_200_meta_type_0 import (
        PostWorkflowsIdDeactivateResponse200MetaType0,
    )
    from ..models.post_workflows_id_deactivate_response_200_nodes_item import (
        PostWorkflowsIdDeactivateResponse200NodesItem,
    )
    from ..models.post_workflows_id_deactivate_response_200_pin_data_type_0 import (
        PostWorkflowsIdDeactivateResponse200PinDataType0,
    )
    from ..models.post_workflows_id_deactivate_response_200_settings import PostWorkflowsIdDeactivateResponse200Settings
    from ..models.post_workflows_id_deactivate_response_200_shared_item import (
        PostWorkflowsIdDeactivateResponse200SharedItem,
    )
    from ..models.post_workflows_id_deactivate_response_200_static_data_type_1_type_0 import (
        PostWorkflowsIdDeactivateResponse200StaticDataType1Type0,
    )
    from ..models.post_workflows_id_deactivate_response_200_tags_item import (
        PostWorkflowsIdDeactivateResponse200TagsItem,
    )


T = TypeVar("T", bound="PostWorkflowsIdDeactivateResponse200")


@_attrs_define
class PostWorkflowsIdDeactivateResponse200:
    """
    Attributes:
        name (str):  Example: Workflow 1.
        nodes (list[PostWorkflowsIdDeactivateResponse200NodesItem]):
        connections (PostWorkflowsIdDeactivateResponse200Connections):  Example: {'Jira': {'main': [[{'node': 'Jira',
            'type': 'main', 'index': 0}]]}}.
        settings (PostWorkflowsIdDeactivateResponse200Settings):
        id (str | Unset):  Example: 2tUt1wbLX592XDdX.
        description (str | Unset): Description of the workflow Example: My workflow description.
        active (bool | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        is_archived (bool | Unset):
        version_id (str | Unset): Current version identifier used for optimistic locking
        trigger_count (int | Unset): Number of active trigger nodes in the workflow
        static_data (None | PostWorkflowsIdDeactivateResponse200StaticDataType1Type0 | str | Unset):  Example:
            {'lastId': 1}.
        pin_data (None | PostWorkflowsIdDeactivateResponse200PinDataType0 | Unset): Pinned sample data for nodes, keyed
            by node name
        meta (None | PostWorkflowsIdDeactivateResponse200MetaType0 | Unset): Workflow metadata such as template
            information
        tags (list[PostWorkflowsIdDeactivateResponse200TagsItem] | Unset):
        shared (list[PostWorkflowsIdDeactivateResponse200SharedItem] | Unset):
        active_version (None | PostWorkflowsIdDeactivateResponse200ActiveVersionType0 | Unset):
    """

    name: str
    nodes: list[PostWorkflowsIdDeactivateResponse200NodesItem]
    connections: PostWorkflowsIdDeactivateResponse200Connections
    settings: PostWorkflowsIdDeactivateResponse200Settings
    id: str | Unset = UNSET
    description: str | Unset = UNSET
    active: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    is_archived: bool | Unset = UNSET
    version_id: str | Unset = UNSET
    trigger_count: int | Unset = UNSET
    static_data: None | PostWorkflowsIdDeactivateResponse200StaticDataType1Type0 | str | Unset = UNSET
    pin_data: None | PostWorkflowsIdDeactivateResponse200PinDataType0 | Unset = UNSET
    meta: None | PostWorkflowsIdDeactivateResponse200MetaType0 | Unset = UNSET
    tags: list[PostWorkflowsIdDeactivateResponse200TagsItem] | Unset = UNSET
    shared: list[PostWorkflowsIdDeactivateResponse200SharedItem] | Unset = UNSET
    active_version: None | PostWorkflowsIdDeactivateResponse200ActiveVersionType0 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_workflows_id_deactivate_response_200_active_version_type_0 import (
            PostWorkflowsIdDeactivateResponse200ActiveVersionType0,
        )
        from ..models.post_workflows_id_deactivate_response_200_meta_type_0 import (
            PostWorkflowsIdDeactivateResponse200MetaType0,
        )
        from ..models.post_workflows_id_deactivate_response_200_pin_data_type_0 import (
            PostWorkflowsIdDeactivateResponse200PinDataType0,
        )
        from ..models.post_workflows_id_deactivate_response_200_static_data_type_1_type_0 import (
            PostWorkflowsIdDeactivateResponse200StaticDataType1Type0,
        )

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
        elif isinstance(self.static_data, PostWorkflowsIdDeactivateResponse200StaticDataType1Type0):
            static_data = self.static_data.to_dict()
        else:
            static_data = self.static_data

        pin_data: dict[str, Any] | None | Unset
        if isinstance(self.pin_data, Unset):
            pin_data = UNSET
        elif isinstance(self.pin_data, PostWorkflowsIdDeactivateResponse200PinDataType0):
            pin_data = self.pin_data.to_dict()
        else:
            pin_data = self.pin_data

        meta: dict[str, Any] | None | Unset
        if isinstance(self.meta, Unset):
            meta = UNSET
        elif isinstance(self.meta, PostWorkflowsIdDeactivateResponse200MetaType0):
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
        elif isinstance(self.active_version, PostWorkflowsIdDeactivateResponse200ActiveVersionType0):
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
        from ..models.post_workflows_id_deactivate_response_200_active_version_type_0 import (
            PostWorkflowsIdDeactivateResponse200ActiveVersionType0,
        )
        from ..models.post_workflows_id_deactivate_response_200_connections import (
            PostWorkflowsIdDeactivateResponse200Connections,
        )
        from ..models.post_workflows_id_deactivate_response_200_meta_type_0 import (
            PostWorkflowsIdDeactivateResponse200MetaType0,
        )
        from ..models.post_workflows_id_deactivate_response_200_nodes_item import (
            PostWorkflowsIdDeactivateResponse200NodesItem,
        )
        from ..models.post_workflows_id_deactivate_response_200_pin_data_type_0 import (
            PostWorkflowsIdDeactivateResponse200PinDataType0,
        )
        from ..models.post_workflows_id_deactivate_response_200_settings import (
            PostWorkflowsIdDeactivateResponse200Settings,
        )
        from ..models.post_workflows_id_deactivate_response_200_shared_item import (
            PostWorkflowsIdDeactivateResponse200SharedItem,
        )
        from ..models.post_workflows_id_deactivate_response_200_static_data_type_1_type_0 import (
            PostWorkflowsIdDeactivateResponse200StaticDataType1Type0,
        )
        from ..models.post_workflows_id_deactivate_response_200_tags_item import (
            PostWorkflowsIdDeactivateResponse200TagsItem,
        )

        d = dict(src_dict)
        name = d.pop("name")

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = PostWorkflowsIdDeactivateResponse200NodesItem.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        connections = PostWorkflowsIdDeactivateResponse200Connections.from_dict(d.pop("connections"))

        settings = PostWorkflowsIdDeactivateResponse200Settings.from_dict(d.pop("settings"))

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

        def _parse_static_data(
            data: object,
        ) -> None | PostWorkflowsIdDeactivateResponse200StaticDataType1Type0 | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                static_data_type_1_type_0 = PostWorkflowsIdDeactivateResponse200StaticDataType1Type0.from_dict(data)

                return static_data_type_1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostWorkflowsIdDeactivateResponse200StaticDataType1Type0 | str | Unset, data)

        static_data = _parse_static_data(d.pop("staticData", UNSET))

        def _parse_pin_data(data: object) -> None | PostWorkflowsIdDeactivateResponse200PinDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pin_data_type_0 = PostWorkflowsIdDeactivateResponse200PinDataType0.from_dict(data)

                return pin_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostWorkflowsIdDeactivateResponse200PinDataType0 | Unset, data)

        pin_data = _parse_pin_data(d.pop("pinData", UNSET))

        def _parse_meta(data: object) -> None | PostWorkflowsIdDeactivateResponse200MetaType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_type_0 = PostWorkflowsIdDeactivateResponse200MetaType0.from_dict(data)

                return meta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostWorkflowsIdDeactivateResponse200MetaType0 | Unset, data)

        meta = _parse_meta(d.pop("meta", UNSET))

        _tags = d.pop("tags", UNSET)
        tags: list[PostWorkflowsIdDeactivateResponse200TagsItem] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = PostWorkflowsIdDeactivateResponse200TagsItem.from_dict(tags_item_data)

                tags.append(tags_item)

        _shared = d.pop("shared", UNSET)
        shared: list[PostWorkflowsIdDeactivateResponse200SharedItem] | Unset = UNSET
        if _shared is not UNSET:
            shared = []
            for shared_item_data in _shared:
                shared_item = PostWorkflowsIdDeactivateResponse200SharedItem.from_dict(shared_item_data)

                shared.append(shared_item)

        def _parse_active_version(
            data: object,
        ) -> None | PostWorkflowsIdDeactivateResponse200ActiveVersionType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                active_version_type_0 = PostWorkflowsIdDeactivateResponse200ActiveVersionType0.from_dict(data)

                return active_version_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostWorkflowsIdDeactivateResponse200ActiveVersionType0 | Unset, data)

        active_version = _parse_active_version(d.pop("activeVersion", UNSET))

        post_workflows_id_deactivate_response_200 = cls(
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

        return post_workflows_id_deactivate_response_200
