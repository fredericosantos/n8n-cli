from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditFilesystemRiskReport")


@_attrs_define
class AuditFilesystemRiskReport:
    """
    Example:
        {'risk': 'filesystem', 'sections': [{'title': 'Nodes that interact with the filesystem', 'description': 'This
            node reads from and writes to any accessible file in the host filesystem. Sensitive file content may be
            manipulated through a node operation.', 'recommendation': 'Consider protecting any sensitive files in the host
            filesystem', 'or refactoring the workflow so that it does not require host filesystem interaction.': None,
            'location': [{'kind': 'node', 'workflowId': '1', 'workflowName': 'My Workflow', 'nodeId':
            '51eb5852-ce0b-4806-b4ff-e41322a4041a', 'nodeName': 'Ready Binary file', 'nodeType': 'n8n-nodes-
            base.readBinaryFile'}]}]}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audit_filesystem_risk_report = cls()

        audit_filesystem_risk_report.additional_properties = d
        return audit_filesystem_risk_report

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
