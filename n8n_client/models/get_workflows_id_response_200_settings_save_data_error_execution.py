from enum import Enum


class GetWorkflowsIdResponse200SettingsSaveDataErrorExecution(str, Enum):
    ALL = "all"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
