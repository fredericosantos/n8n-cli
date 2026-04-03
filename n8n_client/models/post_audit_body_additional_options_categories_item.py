from enum import Enum


class PostAuditBodyAdditionalOptionsCategoriesItem(str, Enum):
    CREDENTIALS = "credentials"
    DATABASE = "database"
    FILESYSTEM = "filesystem"
    INSTANCE = "instance"
    NODES = "nodes"

    def __str__(self) -> str:
        return str(self.value)
