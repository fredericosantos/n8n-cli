from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.put_workflows_id_response_200_settings_caller_policy import PutWorkflowsIdResponse200SettingsCallerPolicy
from ..models.put_workflows_id_response_200_settings_save_data_error_execution import (
    PutWorkflowsIdResponse200SettingsSaveDataErrorExecution,
)
from ..models.put_workflows_id_response_200_settings_save_data_success_execution import (
    PutWorkflowsIdResponse200SettingsSaveDataSuccessExecution,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutWorkflowsIdResponse200Settings")


@_attrs_define
class PutWorkflowsIdResponse200Settings:
    """
    Attributes:
        save_execution_progress (bool | Unset):
        save_manual_executions (bool | Unset):
        save_data_error_execution (PutWorkflowsIdResponse200SettingsSaveDataErrorExecution | Unset):
        save_data_success_execution (PutWorkflowsIdResponse200SettingsSaveDataSuccessExecution | Unset):
        execution_timeout (float | Unset):  Example: 3600.
        error_workflow (str | Unset): The ID of the workflow that contains the error trigger node. Example:
            VzqKEW0ShTXA5vPj.
        timezone (str | Unset):  Example: America/New_York.
        execution_order (str | Unset):  Example: v1.
        caller_policy (PutWorkflowsIdResponse200SettingsCallerPolicy | Unset): Controls which workflows are allowed to
            call this workflow using the Execute Workflow node.

            Available options:
            - `any`: Any workflow can call this workflow (no restrictions)
            - `none`: No other workflows can call this workflow (completely blocked)
            - `workflowsFromSameOwner` (default): Only workflows owned by the same project can call this workflow
              * For personal projects: Only workflows created by the same user
              * For team projects: Only workflows within the same team project
            - `workflowsFromAList`: Only specific workflows listed in the `callerIds` field can call this workflow
              * Requires the `callerIds` field to specify which workflow IDs are allowed
              * See `callerIds` field documentation for usage
             Default: PutWorkflowsIdResponse200SettingsCallerPolicy.WORKFLOWSFROMSAMEOWNER. Example: workflowsFromSameOwner.
        caller_ids (str | Unset): Comma-separated list of workflow IDs allowed to call this workflow (only used with
            workflowsFromAList policy) Example: 14, 18, 23.
        time_saved_per_execution (float | Unset): Estimated time saved per execution in minutes
        available_in_mcp (bool | Unset): Controls whether this workflow is accessible via the Model Context Protocol
            (MCP).

            When enabled, this workflow can be called by MCP clients (AI assistants and other tools
            that support MCP). This allows external AI tools to discover and execute this workflow
            as part of their capabilities.

            Requirements for enabling MCP access:
            - The workflow must be active (not deactivated)
            - The workflow must contain at least one active Webhook node
            - Only webhook-triggered workflows can be exposed via MCP

            Security note: When a workflow is available in MCP, it can be discovered and executed
            by any MCP client that has the appropriate API credentials for your n8n instance.
             Default: False.
    """

    save_execution_progress: bool | Unset = UNSET
    save_manual_executions: bool | Unset = UNSET
    save_data_error_execution: PutWorkflowsIdResponse200SettingsSaveDataErrorExecution | Unset = UNSET
    save_data_success_execution: PutWorkflowsIdResponse200SettingsSaveDataSuccessExecution | Unset = UNSET
    execution_timeout: float | Unset = UNSET
    error_workflow: str | Unset = UNSET
    timezone: str | Unset = UNSET
    execution_order: str | Unset = UNSET
    caller_policy: PutWorkflowsIdResponse200SettingsCallerPolicy | Unset = (
        PutWorkflowsIdResponse200SettingsCallerPolicy.WORKFLOWSFROMSAMEOWNER
    )
    caller_ids: str | Unset = UNSET
    time_saved_per_execution: float | Unset = UNSET
    available_in_mcp: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        save_execution_progress = self.save_execution_progress

        save_manual_executions = self.save_manual_executions

        save_data_error_execution: str | Unset = UNSET
        if not isinstance(self.save_data_error_execution, Unset):
            save_data_error_execution = self.save_data_error_execution.value

        save_data_success_execution: str | Unset = UNSET
        if not isinstance(self.save_data_success_execution, Unset):
            save_data_success_execution = self.save_data_success_execution.value

        execution_timeout = self.execution_timeout

        error_workflow = self.error_workflow

        timezone = self.timezone

        execution_order = self.execution_order

        caller_policy: str | Unset = UNSET
        if not isinstance(self.caller_policy, Unset):
            caller_policy = self.caller_policy.value

        caller_ids = self.caller_ids

        time_saved_per_execution = self.time_saved_per_execution

        available_in_mcp = self.available_in_mcp

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if save_execution_progress is not UNSET:
            field_dict["saveExecutionProgress"] = save_execution_progress
        if save_manual_executions is not UNSET:
            field_dict["saveManualExecutions"] = save_manual_executions
        if save_data_error_execution is not UNSET:
            field_dict["saveDataErrorExecution"] = save_data_error_execution
        if save_data_success_execution is not UNSET:
            field_dict["saveDataSuccessExecution"] = save_data_success_execution
        if execution_timeout is not UNSET:
            field_dict["executionTimeout"] = execution_timeout
        if error_workflow is not UNSET:
            field_dict["errorWorkflow"] = error_workflow
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if execution_order is not UNSET:
            field_dict["executionOrder"] = execution_order
        if caller_policy is not UNSET:
            field_dict["callerPolicy"] = caller_policy
        if caller_ids is not UNSET:
            field_dict["callerIds"] = caller_ids
        if time_saved_per_execution is not UNSET:
            field_dict["timeSavedPerExecution"] = time_saved_per_execution
        if available_in_mcp is not UNSET:
            field_dict["availableInMCP"] = available_in_mcp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        save_execution_progress = d.pop("saveExecutionProgress", UNSET)

        save_manual_executions = d.pop("saveManualExecutions", UNSET)

        _save_data_error_execution = d.pop("saveDataErrorExecution", UNSET)
        save_data_error_execution: PutWorkflowsIdResponse200SettingsSaveDataErrorExecution | Unset
        if isinstance(_save_data_error_execution, Unset):
            save_data_error_execution = UNSET
        else:
            save_data_error_execution = PutWorkflowsIdResponse200SettingsSaveDataErrorExecution(
                _save_data_error_execution
            )

        _save_data_success_execution = d.pop("saveDataSuccessExecution", UNSET)
        save_data_success_execution: PutWorkflowsIdResponse200SettingsSaveDataSuccessExecution | Unset
        if isinstance(_save_data_success_execution, Unset):
            save_data_success_execution = UNSET
        else:
            save_data_success_execution = PutWorkflowsIdResponse200SettingsSaveDataSuccessExecution(
                _save_data_success_execution
            )

        execution_timeout = d.pop("executionTimeout", UNSET)

        error_workflow = d.pop("errorWorkflow", UNSET)

        timezone = d.pop("timezone", UNSET)

        execution_order = d.pop("executionOrder", UNSET)

        _caller_policy = d.pop("callerPolicy", UNSET)
        caller_policy: PutWorkflowsIdResponse200SettingsCallerPolicy | Unset
        if isinstance(_caller_policy, Unset):
            caller_policy = UNSET
        else:
            caller_policy = PutWorkflowsIdResponse200SettingsCallerPolicy(_caller_policy)

        caller_ids = d.pop("callerIds", UNSET)

        time_saved_per_execution = d.pop("timeSavedPerExecution", UNSET)

        available_in_mcp = d.pop("availableInMCP", UNSET)

        put_workflows_id_response_200_settings = cls(
            save_execution_progress=save_execution_progress,
            save_manual_executions=save_manual_executions,
            save_data_error_execution=save_data_error_execution,
            save_data_success_execution=save_data_success_execution,
            execution_timeout=execution_timeout,
            error_workflow=error_workflow,
            timezone=timezone,
            execution_order=execution_order,
            caller_policy=caller_policy,
            caller_ids=caller_ids,
            time_saved_per_execution=time_saved_per_execution,
            available_in_mcp=available_in_mcp,
        )

        return put_workflows_id_response_200_settings
