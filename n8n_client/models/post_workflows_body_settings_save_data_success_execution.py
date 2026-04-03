from enum import Enum


class PostWorkflowsBodySettingsSaveDataSuccessExecution(str, Enum):
    ALL = "all"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
