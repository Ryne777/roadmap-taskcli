from datetime import datetime
import enum
from dataclasses import dataclass
from rich.console import Console, ConsoleOptions, RenderResult
from rich.table import Table


@enum.unique
class Status(enum.IntEnum):
    todo = 1
    in_progress = 2
    done = 3


class Base:
    """Base class"""

    id: int


@dataclass
class ToDo(Base):
    """
    ToDo class
    """

    def __init__(
        self,
        description: str,
        status: Status = Status.todo,
        start_at: datetime = datetime.now(),
        update_at: datetime = datetime.now(),
    ):
        self.description: str = description
        self.status: Status = status
        self.start_at: datetime = start_at
        self.update_at: datetime = update_at

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        yield f"[b]ToDo:[/b] #{self.id}"
        my_table = Table("Attribute", "Value")
        my_table.add_row("Description", self.description, style="magenta")
        my_table.add_row("Status", self.status.name, style="cyan")
        my_table.add_row(
            "Create at",
            self.start_at.strftime("%m/%d/%Y, %H:%M:%S"),
            style="green",
        )
        my_table.add_row(
            "Update at",
            self.update_at.strftime("%m/%d/%Y, %H:%M:%S"),
            style="blue",
        )

        yield my_table
