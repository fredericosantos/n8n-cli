from enum import Enum


class InsertRowsRequestReturnType(str, Enum):
    ALL = "all"
    COUNT = "count"
    ID = "id"

    def __str__(self) -> str:
        return str(self.value)
