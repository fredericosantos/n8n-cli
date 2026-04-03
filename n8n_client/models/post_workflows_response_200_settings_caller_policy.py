from enum import Enum


class PostWorkflowsResponse200SettingsCallerPolicy(str, Enum):
    ANY = "any"
    NONE = "none"
    WORKFLOWSFROMALIST = "workflowsFromAList"
    WORKFLOWSFROMSAMEOWNER = "workflowsFromSameOwner"

    def __str__(self) -> str:
        return str(self.value)
