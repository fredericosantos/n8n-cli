from enum import Enum


class WorkflowSettingsSaveDataSuccessExecution(str, Enum):
    ALL = "all"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
