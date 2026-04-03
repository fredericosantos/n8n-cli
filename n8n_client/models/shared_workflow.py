from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shared_workflow_project import SharedWorkflowProject


T = TypeVar("T", bound="SharedWorkflow")


@_attrs_define
class SharedWorkflow:
    """
    Attributes:
        role (str | Unset):  Example: workflow:owner.
        workflow_id (str | Unset):  Example: 2tUt1wbLX592XDdX.
        project_id (str | Unset):  Example: 2tUt1wbLX592XDdX.
        project (SharedWorkflowProject | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    role: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    project: SharedWorkflowProject | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        workflow_id = self.workflow_id

        project_id = self.project_id

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if project is not UNSET:
            field_dict["project"] = project
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shared_workflow_project import SharedWorkflowProject

        d = dict(src_dict)
        role = d.pop("role", UNSET)

        workflow_id = d.pop("workflowId", UNSET)

        project_id = d.pop("projectId", UNSET)

        _project = d.pop("project", UNSET)
        project: SharedWorkflowProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = SharedWorkflowProject.from_dict(_project)

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

        shared_workflow = cls(
            role=role,
            workflow_id=workflow_id,
            project_id=project_id,
            project=project,
            created_at=created_at,
            updated_at=updated_at,
        )

        return shared_workflow
