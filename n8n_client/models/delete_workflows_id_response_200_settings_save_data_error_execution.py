from enum import Enum


class DeleteWorkflowsIdResponse200SettingsSaveDataErrorExecution(str, Enum):
    ALL = "all"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
