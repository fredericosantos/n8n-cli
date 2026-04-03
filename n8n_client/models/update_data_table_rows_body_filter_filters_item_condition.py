from enum import Enum


class UpdateDataTableRowsBodyFilterFiltersItemCondition(str, Enum):
    EQ = "eq"
    GT = "gt"
    GTE = "gte"
    ILIKE = "ilike"
    LIKE = "like"
    LT = "lt"
    LTE = "lte"
    NEQ = "neq"

    def __str__(self) -> str:
        return str(self.value)
