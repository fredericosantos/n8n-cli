from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditNodesRiskReport")


@_attrs_define
class AuditNodesRiskReport:
    """
    Example:
        {'risk': 'nodes', 'sections': [{'title': 'Community nodes', 'description': 'This node is sourced from the
            community. Community nodes are not vetted by the n8n team and have full access to the host system.',
            'recommendation': 'Consider reviewing the source code in any community nodes installed in this n8n instance',
            'and uninstalling any community nodes no longer used.': None, 'location': [{'kind': 'community', 'nodeType':
            'n8n-nodes-test.test', 'packageUrl': 'https://www.npmjs.com/package/n8n-nodes-test'}]}]}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audit_nodes_risk_report = cls()

        audit_nodes_risk_report.additional_properties = d
        return audit_nodes_risk_report

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
