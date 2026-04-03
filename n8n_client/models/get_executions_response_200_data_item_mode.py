from enum import Enum


class GetExecutionsResponse200DataItemMode(str, Enum):
    CHAT = "chat"
    CLI = "cli"
    ERROR = "error"
    EVALUATION = "evaluation"
    INTEGRATED = "integrated"
    INTERNAL = "internal"
    MANUAL = "manual"
    RETRY = "retry"
    TRIGGER = "trigger"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
