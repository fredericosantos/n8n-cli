from enum import Enum


class GetVariablesState(str, Enum):
    EMPTY = "empty"

    def __str__(self) -> str:
        return str(self.value)
