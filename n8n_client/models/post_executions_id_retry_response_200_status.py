from enum import Enum


class PostExecutionsIdRetryResponse200Status(str, Enum):
    CANCELED = "canceled"
    CRASHED = "crashed"
    ERROR = "error"
    NEW = "new"
    RUNNING = "running"
    SUCCESS = "success"
    UNKNOWN = "unknown"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
