from enum import Enum


class UpdateRowsRequestFilterType(str, Enum):
    AND = "and"
    OR = "or"

    def __str__(self) -> str:
        return str(self.value)
