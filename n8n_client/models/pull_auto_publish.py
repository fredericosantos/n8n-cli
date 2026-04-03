from enum import Enum


class PullAutoPublish(str, Enum):
    ALL = "all"
    NONE = "none"
    PUBLISHED = "published"

    def __str__(self) -> str:
        return str(self.value)
