from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.get_executions_response_200_data_item_mode import GetExecutionsResponse200DataItemMode
from ..models.get_executions_response_200_data_item_status import GetExecutionsResponse200DataItemStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_executions_response_200_data_item_custom_data import GetExecutionsResponse200DataItemCustomData
    from ..models.get_executions_response_200_data_item_data import GetExecutionsResponse200DataItemData


T = TypeVar("T", bound="GetExecutionsResponse200DataItem")


@_attrs_define
class GetExecutionsResponse200DataItem:
    """
    Attributes:
        id (float | Unset):  Example: 1000.
        data (GetExecutionsResponse200DataItemData | Unset): Detailed execution data. Only included when `includeData`
            is `true`.
        finished (bool | Unset):  Example: True.
        mode (GetExecutionsResponse200DataItemMode | Unset):
        retry_of (float | None | Unset):
        retry_success_id (float | None | Unset):  Example: 2.
        started_at (datetime.datetime | Unset):
        stopped_at (datetime.datetime | None | Unset): The time at which the execution stopped. Will only be null for
            executions that still have the status 'running'.
        workflow_id (float | Unset):  Example: 1000.
        wait_till (datetime.datetime | None | Unset):
        custom_data (GetExecutionsResponse200DataItemCustomData | Unset):
        status (GetExecutionsResponse200DataItemStatus | Unset):
    """

    id: float | Unset = UNSET
    data: GetExecutionsResponse200DataItemData | Unset = UNSET
    finished: bool | Unset = UNSET
    mode: GetExecutionsResponse200DataItemMode | Unset = UNSET
    retry_of: float | None | Unset = UNSET
    retry_success_id: float | None | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    stopped_at: datetime.datetime | None | Unset = UNSET
    workflow_id: float | Unset = UNSET
    wait_till: datetime.datetime | None | Unset = UNSET
    custom_data: GetExecutionsResponse200DataItemCustomData | Unset = UNSET
    status: GetExecutionsResponse200DataItemStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        finished = self.finished

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        retry_of: float | None | Unset
        if isinstance(self.retry_of, Unset):
            retry_of = UNSET
        else:
            retry_of = self.retry_of

        retry_success_id: float | None | Unset
        if isinstance(self.retry_success_id, Unset):
            retry_success_id = UNSET
        else:
            retry_success_id = self.retry_success_id

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        stopped_at: None | str | Unset
        if isinstance(self.stopped_at, Unset):
            stopped_at = UNSET
        elif isinstance(self.stopped_at, datetime.datetime):
            stopped_at = self.stopped_at.isoformat()
        else:
            stopped_at = self.stopped_at

        workflow_id = self.workflow_id

        wait_till: None | str | Unset
        if isinstance(self.wait_till, Unset):
            wait_till = UNSET
        elif isinstance(self.wait_till, datetime.datetime):
            wait_till = self.wait_till.isoformat()
        else:
            wait_till = self.wait_till

        custom_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_data, Unset):
            custom_data = self.custom_data.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if data is not UNSET:
            field_dict["data"] = data
        if finished is not UNSET:
            field_dict["finished"] = finished
        if mode is not UNSET:
            field_dict["mode"] = mode
        if retry_of is not UNSET:
            field_dict["retryOf"] = retry_of
        if retry_success_id is not UNSET:
            field_dict["retrySuccessId"] = retry_success_id
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if stopped_at is not UNSET:
            field_dict["stoppedAt"] = stopped_at
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if wait_till is not UNSET:
            field_dict["waitTill"] = wait_till
        if custom_data is not UNSET:
            field_dict["customData"] = custom_data
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_executions_response_200_data_item_custom_data import (
            GetExecutionsResponse200DataItemCustomData,
        )
        from ..models.get_executions_response_200_data_item_data import GetExecutionsResponse200DataItemData

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _data = d.pop("data", UNSET)
        data: GetExecutionsResponse200DataItemData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GetExecutionsResponse200DataItemData.from_dict(_data)

        finished = d.pop("finished", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: GetExecutionsResponse200DataItemMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = GetExecutionsResponse200DataItemMode(_mode)

        def _parse_retry_of(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        retry_of = _parse_retry_of(d.pop("retryOf", UNSET))

        def _parse_retry_success_id(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        retry_success_id = _parse_retry_success_id(d.pop("retrySuccessId", UNSET))

        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        def _parse_stopped_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                stopped_at_type_0 = isoparse(data)

                return stopped_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        stopped_at = _parse_stopped_at(d.pop("stoppedAt", UNSET))

        workflow_id = d.pop("workflowId", UNSET)

        def _parse_wait_till(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                wait_till_type_0 = isoparse(data)

                return wait_till_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        wait_till = _parse_wait_till(d.pop("waitTill", UNSET))

        _custom_data = d.pop("customData", UNSET)
        custom_data: GetExecutionsResponse200DataItemCustomData | Unset
        if isinstance(_custom_data, Unset):
            custom_data = UNSET
        else:
            custom_data = GetExecutionsResponse200DataItemCustomData.from_dict(_custom_data)

        _status = d.pop("status", UNSET)
        status: GetExecutionsResponse200DataItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetExecutionsResponse200DataItemStatus(_status)

        get_executions_response_200_data_item = cls(
            id=id,
            data=data,
            finished=finished,
            mode=mode,
            retry_of=retry_of,
            retry_success_id=retry_success_id,
            started_at=started_at,
            stopped_at=stopped_at,
            workflow_id=workflow_id,
            wait_till=wait_till,
            custom_data=custom_data,
            status=status,
        )

        get_executions_response_200_data_item.additional_properties = d
        return get_executions_response_200_data_item

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
