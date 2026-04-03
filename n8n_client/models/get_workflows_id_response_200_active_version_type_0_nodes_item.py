from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_workflows_id_response_200_active_version_type_0_nodes_item_credentials import (
        GetWorkflowsIdResponse200ActiveVersionType0NodesItemCredentials,
    )
    from ..models.get_workflows_id_response_200_active_version_type_0_nodes_item_parameters import (
        GetWorkflowsIdResponse200ActiveVersionType0NodesItemParameters,
    )


T = TypeVar("T", bound="GetWorkflowsIdResponse200ActiveVersionType0NodesItem")


@_attrs_define
class GetWorkflowsIdResponse200ActiveVersionType0NodesItem:
    """
    Attributes:
        id (str | Unset):  Example: 0f5532f9-36ba-4bef-86c7-30d607400b15.
        name (str | Unset):  Example: Jira.
        webhook_id (str | Unset):
        disabled (bool | Unset):
        notes_in_flow (bool | Unset):
        notes (str | Unset):
        type_ (str | Unset):  Example: n8n-nodes-base.jira.
        type_version (float | Unset):  Example: 1.
        execute_once (bool | Unset):
        always_output_data (bool | Unset):
        retry_on_fail (bool | Unset):
        max_tries (float | Unset):
        wait_between_tries (float | Unset):
        continue_on_fail (bool | Unset): use onError instead
        on_error (str | Unset):  Example: stopWorkflow.
        position (list[float] | Unset):  Example: [-100, 80].
        parameters (GetWorkflowsIdResponse200ActiveVersionType0NodesItemParameters | Unset):  Example:
            {'additionalProperties': {}}.
        credentials (GetWorkflowsIdResponse200ActiveVersionType0NodesItemCredentials | Unset):  Example:
            {'jiraSoftwareCloudApi': {'id': '35', 'name': 'jiraApi'}}.
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    webhook_id: str | Unset = UNSET
    disabled: bool | Unset = UNSET
    notes_in_flow: bool | Unset = UNSET
    notes: str | Unset = UNSET
    type_: str | Unset = UNSET
    type_version: float | Unset = UNSET
    execute_once: bool | Unset = UNSET
    always_output_data: bool | Unset = UNSET
    retry_on_fail: bool | Unset = UNSET
    max_tries: float | Unset = UNSET
    wait_between_tries: float | Unset = UNSET
    continue_on_fail: bool | Unset = UNSET
    on_error: str | Unset = UNSET
    position: list[float] | Unset = UNSET
    parameters: GetWorkflowsIdResponse200ActiveVersionType0NodesItemParameters | Unset = UNSET
    credentials: GetWorkflowsIdResponse200ActiveVersionType0NodesItemCredentials | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        webhook_id = self.webhook_id

        disabled = self.disabled

        notes_in_flow = self.notes_in_flow

        notes = self.notes

        type_ = self.type_

        type_version = self.type_version

        execute_once = self.execute_once

        always_output_data = self.always_output_data

        retry_on_fail = self.retry_on_fail

        max_tries = self.max_tries

        wait_between_tries = self.wait_between_tries

        continue_on_fail = self.continue_on_fail

        on_error = self.on_error

        position: list[float] | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if webhook_id is not UNSET:
            field_dict["webhookId"] = webhook_id
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if notes_in_flow is not UNSET:
            field_dict["notesInFlow"] = notes_in_flow
        if notes is not UNSET:
            field_dict["notes"] = notes
        if type_ is not UNSET:
            field_dict["type"] = type_
        if type_version is not UNSET:
            field_dict["typeVersion"] = type_version
        if execute_once is not UNSET:
            field_dict["executeOnce"] = execute_once
        if always_output_data is not UNSET:
            field_dict["alwaysOutputData"] = always_output_data
        if retry_on_fail is not UNSET:
            field_dict["retryOnFail"] = retry_on_fail
        if max_tries is not UNSET:
            field_dict["maxTries"] = max_tries
        if wait_between_tries is not UNSET:
            field_dict["waitBetweenTries"] = wait_between_tries
        if continue_on_fail is not UNSET:
            field_dict["continueOnFail"] = continue_on_fail
        if on_error is not UNSET:
            field_dict["onError"] = on_error
        if position is not UNSET:
            field_dict["position"] = position
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_workflows_id_response_200_active_version_type_0_nodes_item_credentials import (
            GetWorkflowsIdResponse200ActiveVersionType0NodesItemCredentials,
        )
        from ..models.get_workflows_id_response_200_active_version_type_0_nodes_item_parameters import (
            GetWorkflowsIdResponse200ActiveVersionType0NodesItemParameters,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        webhook_id = d.pop("webhookId", UNSET)

        disabled = d.pop("disabled", UNSET)

        notes_in_flow = d.pop("notesInFlow", UNSET)

        notes = d.pop("notes", UNSET)

        type_ = d.pop("type", UNSET)

        type_version = d.pop("typeVersion", UNSET)

        execute_once = d.pop("executeOnce", UNSET)

        always_output_data = d.pop("alwaysOutputData", UNSET)

        retry_on_fail = d.pop("retryOnFail", UNSET)

        max_tries = d.pop("maxTries", UNSET)

        wait_between_tries = d.pop("waitBetweenTries", UNSET)

        continue_on_fail = d.pop("continueOnFail", UNSET)

        on_error = d.pop("onError", UNSET)

        position = cast(list[float], d.pop("position", UNSET))

        _parameters = d.pop("parameters", UNSET)
        parameters: GetWorkflowsIdResponse200ActiveVersionType0NodesItemParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = GetWorkflowsIdResponse200ActiveVersionType0NodesItemParameters.from_dict(_parameters)

        _credentials = d.pop("credentials", UNSET)
        credentials: GetWorkflowsIdResponse200ActiveVersionType0NodesItemCredentials | Unset
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = GetWorkflowsIdResponse200ActiveVersionType0NodesItemCredentials.from_dict(_credentials)

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

        get_workflows_id_response_200_active_version_type_0_nodes_item = cls(
            id=id,
            name=name,
            webhook_id=webhook_id,
            disabled=disabled,
            notes_in_flow=notes_in_flow,
            notes=notes,
            type_=type_,
            type_version=type_version,
            execute_once=execute_once,
            always_output_data=always_output_data,
            retry_on_fail=retry_on_fail,
            max_tries=max_tries,
            wait_between_tries=wait_between_tries,
            continue_on_fail=continue_on_fail,
            on_error=on_error,
            position=position,
            parameters=parameters,
            credentials=credentials,
            created_at=created_at,
            updated_at=updated_at,
        )

        return get_workflows_id_response_200_active_version_type_0_nodes_item
