from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.post_executions_stop_body_status_item import PostExecutionsStopBodyStatusItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostExecutionsStopBody")


@_attrs_define
class PostExecutionsStopBody:
    """
    Attributes:
        status (list[PostExecutionsStopBodyStatusItem]): Array of execution statuses to stop. Must include at least one
            status. Example: ['queued', 'running', 'waiting'].
        workflow_id (str | Unset): Optional workflow ID to filter executions. If not provided, will stop executions
            across all accessible workflows. Example: 2tUt1wbLX592XDdX.
        started_after (datetime.datetime | Unset): Only stop executions that started after this time. Example:
            2024-01-01T00:00:00.000Z.
        started_before (datetime.datetime | Unset): Only stop executions that started before this time. Example:
            2024-12-31T23:59:59.999Z.
    """

    status: list[PostExecutionsStopBodyStatusItem]
    workflow_id: str | Unset = UNSET
    started_after: datetime.datetime | Unset = UNSET
    started_before: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = []
        for status_item_data in self.status:
            status_item = status_item_data.value
            status.append(status_item)

        workflow_id = self.workflow_id

        started_after: str | Unset = UNSET
        if not isinstance(self.started_after, Unset):
            started_after = self.started_after.isoformat()

        started_before: str | Unset = UNSET
        if not isinstance(self.started_before, Unset):
            started_before = self.started_before.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if started_after is not UNSET:
            field_dict["startedAfter"] = started_after
        if started_before is not UNSET:
            field_dict["startedBefore"] = started_before

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = []
        _status = d.pop("status")
        for status_item_data in _status:
            status_item = PostExecutionsStopBodyStatusItem(status_item_data)

            status.append(status_item)

        workflow_id = d.pop("workflowId", UNSET)

        _started_after = d.pop("startedAfter", UNSET)
        started_after: datetime.datetime | Unset
        if isinstance(_started_after, Unset):
            started_after = UNSET
        else:
            started_after = isoparse(_started_after)

        _started_before = d.pop("startedBefore", UNSET)
        started_before: datetime.datetime | Unset
        if isinstance(_started_before, Unset):
            started_before = UNSET
        else:
            started_before = isoparse(_started_before)

        post_executions_stop_body = cls(
            status=status,
            workflow_id=workflow_id,
            started_after=started_after,
            started_before=started_before,
        )

        post_executions_stop_body.additional_properties = d
        return post_executions_stop_body

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
