from enum import Enum


class GetWorkflowsResponse200DataItemSettingsSaveDataErrorExecution(str, Enum):
    ALL = "all"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
