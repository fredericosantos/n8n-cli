from enum import Enum


class PostWorkflowsIdActivateResponse200SettingsSaveDataErrorExecution(str, Enum):
    ALL = "all"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
