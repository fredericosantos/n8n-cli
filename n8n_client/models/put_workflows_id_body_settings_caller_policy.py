from enum import Enum


class PutWorkflowsIdBodySettingsCallerPolicy(str, Enum):
    ANY = "any"
    NONE = "none"
    WORKFLOWSFROMALIST = "workflowsFromAList"
    WORKFLOWSFROMSAMEOWNER = "workflowsFromSameOwner"

    def __str__(self) -> str:
        return str(self.value)
