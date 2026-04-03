from enum import Enum


class PostSourceControlPullBodyAutoPublish(str, Enum):
    ALL = "all"
    NONE = "none"
    PUBLISHED = "published"

    def __str__(self) -> str:
        return str(self.value)
