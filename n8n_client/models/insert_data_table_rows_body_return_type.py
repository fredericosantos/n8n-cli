from enum import Enum


class InsertDataTableRowsBodyReturnType(str, Enum):
    ALL = "all"
    COUNT = "count"
    ID = "id"

    def __str__(self) -> str:
        return str(self.value)
