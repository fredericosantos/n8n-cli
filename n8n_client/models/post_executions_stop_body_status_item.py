from enum import Enum


class PostExecutionsStopBodyStatusItem(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
