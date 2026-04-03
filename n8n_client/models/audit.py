from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_credentials_risk_report import AuditCredentialsRiskReport
    from ..models.audit_database_risk_report import AuditDatabaseRiskReport
    from ..models.audit_filesystem_risk_report import AuditFilesystemRiskReport
    from ..models.audit_instance_risk_report import AuditInstanceRiskReport
    from ..models.audit_nodes_risk_report import AuditNodesRiskReport


T = TypeVar("T", bound="Audit")


@_attrs_define
class Audit:
    """
    Attributes:
        credentials_risk_report (AuditCredentialsRiskReport | Unset):  Example: {'risk': 'credentials', 'sections':
            [{'title': 'Credentials not used in any workflow', 'description': 'These credentials are not used in any
            workflow. Keeping unused credentials in your instance is an unneeded security risk.', 'recommendation':
            'Consider deleting these credentials if you no longer need them.', 'location': [{'kind': 'credential', 'id':
            '1', 'name': 'My Test Account'}]}]}.
        database_risk_report (AuditDatabaseRiskReport | Unset):  Example: {'risk': 'database', 'sections': [{'title':
            'Expressions in "Execute Query" fields in SQL nodes', 'description': 'This SQL node has an expression in the
            "Query" field of an "Execute Query" operation. Building a SQL query with an expression may lead to a SQL
            injection attack.', 'recommendation': 'Consider using the "Query Parameters" field to pass parameters to the
            query', 'or validating the input of the expression in the "Query" field.': None, 'location': [{'kind': 'node',
            'workflowId': '1', 'workflowName': 'My Workflow', 'nodeId': '51eb5852-ce0b-4806-b4ff-e41322a4041a', 'nodeName':
            'MySQL', 'nodeType': 'n8n-nodes-base.mySql'}]}]}.
        filesystem_risk_report (AuditFilesystemRiskReport | Unset):  Example: {'risk': 'filesystem', 'sections':
            [{'title': 'Nodes that interact with the filesystem', 'description': 'This node reads from and writes to any
            accessible file in the host filesystem. Sensitive file content may be manipulated through a node operation.',
            'recommendation': 'Consider protecting any sensitive files in the host filesystem', 'or refactoring the workflow
            so that it does not require host filesystem interaction.': None, 'location': [{'kind': 'node', 'workflowId':
            '1', 'workflowName': 'My Workflow', 'nodeId': '51eb5852-ce0b-4806-b4ff-e41322a4041a', 'nodeName': 'Ready Binary
            file', 'nodeType': 'n8n-nodes-base.readBinaryFile'}]}]}.
        nodes_risk_report (AuditNodesRiskReport | Unset):  Example: {'risk': 'nodes', 'sections': [{'title': 'Community
            nodes', 'description': 'This node is sourced from the community. Community nodes are not vetted by the n8n team
            and have full access to the host system.', 'recommendation': 'Consider reviewing the source code in any
            community nodes installed in this n8n instance', 'and uninstalling any community nodes no longer used.': None,
            'location': [{'kind': 'community', 'nodeType': 'n8n-nodes-test.test', 'packageUrl':
            'https://www.npmjs.com/package/n8n-nodes-test'}]}]}.
        instance_risk_report (AuditInstanceRiskReport | Unset):  Example: {'risk': 'execution', 'sections': [{'title':
            'Unprotected webhooks in instance', 'description': 'These webhook nodes have the "Authentication" field set to
            "None" and are not directly connected to a node to validate the payload. Every unprotected webhook allows your
            workflow to be called by any third party who knows the webhook URL.', 'recommendation': 'Consider setting the
            "Authentication" field to an option other than "None"', 'or validating the payload with one of the following
            nodes.': None, 'location': [{'kind': 'community', 'nodeType': 'n8n-nodes-test.test', 'packageUrl':
            'https://www.npmjs.com/package/n8n-nodes-test'}]}]}.
    """

    credentials_risk_report: AuditCredentialsRiskReport | Unset = UNSET
    database_risk_report: AuditDatabaseRiskReport | Unset = UNSET
    filesystem_risk_report: AuditFilesystemRiskReport | Unset = UNSET
    nodes_risk_report: AuditNodesRiskReport | Unset = UNSET
    instance_risk_report: AuditInstanceRiskReport | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credentials_risk_report: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credentials_risk_report, Unset):
            credentials_risk_report = self.credentials_risk_report.to_dict()

        database_risk_report: dict[str, Any] | Unset = UNSET
        if not isinstance(self.database_risk_report, Unset):
            database_risk_report = self.database_risk_report.to_dict()

        filesystem_risk_report: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filesystem_risk_report, Unset):
            filesystem_risk_report = self.filesystem_risk_report.to_dict()

        nodes_risk_report: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nodes_risk_report, Unset):
            nodes_risk_report = self.nodes_risk_report.to_dict()

        instance_risk_report: dict[str, Any] | Unset = UNSET
        if not isinstance(self.instance_risk_report, Unset):
            instance_risk_report = self.instance_risk_report.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials_risk_report is not UNSET:
            field_dict["Credentials Risk Report"] = credentials_risk_report
        if database_risk_report is not UNSET:
            field_dict["Database Risk Report"] = database_risk_report
        if filesystem_risk_report is not UNSET:
            field_dict["Filesystem Risk Report"] = filesystem_risk_report
        if nodes_risk_report is not UNSET:
            field_dict["Nodes Risk Report"] = nodes_risk_report
        if instance_risk_report is not UNSET:
            field_dict["Instance Risk Report"] = instance_risk_report

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_credentials_risk_report import AuditCredentialsRiskReport
        from ..models.audit_database_risk_report import AuditDatabaseRiskReport
        from ..models.audit_filesystem_risk_report import AuditFilesystemRiskReport
        from ..models.audit_instance_risk_report import AuditInstanceRiskReport
        from ..models.audit_nodes_risk_report import AuditNodesRiskReport

        d = dict(src_dict)
        _credentials_risk_report = d.pop("Credentials Risk Report", UNSET)
        credentials_risk_report: AuditCredentialsRiskReport | Unset
        if isinstance(_credentials_risk_report, Unset):
            credentials_risk_report = UNSET
        else:
            credentials_risk_report = AuditCredentialsRiskReport.from_dict(_credentials_risk_report)

        _database_risk_report = d.pop("Database Risk Report", UNSET)
        database_risk_report: AuditDatabaseRiskReport | Unset
        if isinstance(_database_risk_report, Unset):
            database_risk_report = UNSET
        else:
            database_risk_report = AuditDatabaseRiskReport.from_dict(_database_risk_report)

        _filesystem_risk_report = d.pop("Filesystem Risk Report", UNSET)
        filesystem_risk_report: AuditFilesystemRiskReport | Unset
        if isinstance(_filesystem_risk_report, Unset):
            filesystem_risk_report = UNSET
        else:
            filesystem_risk_report = AuditFilesystemRiskReport.from_dict(_filesystem_risk_report)

        _nodes_risk_report = d.pop("Nodes Risk Report", UNSET)
        nodes_risk_report: AuditNodesRiskReport | Unset
        if isinstance(_nodes_risk_report, Unset):
            nodes_risk_report = UNSET
        else:
            nodes_risk_report = AuditNodesRiskReport.from_dict(_nodes_risk_report)

        _instance_risk_report = d.pop("Instance Risk Report", UNSET)
        instance_risk_report: AuditInstanceRiskReport | Unset
        if isinstance(_instance_risk_report, Unset):
            instance_risk_report = UNSET
        else:
            instance_risk_report = AuditInstanceRiskReport.from_dict(_instance_risk_report)

        audit = cls(
            credentials_risk_report=credentials_risk_report,
            database_risk_report=database_risk_report,
            filesystem_risk_report=filesystem_risk_report,
            nodes_risk_report=nodes_risk_report,
            instance_risk_report=instance_risk_report,
        )

        audit.additional_properties = d
        return audit

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
