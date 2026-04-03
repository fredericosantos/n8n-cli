from enum import Enum


class GetDiscoverInclude(str, Enum):
    SCHEMAS = "schemas"

    def __str__(self) -> str:
        return str(self.value)
