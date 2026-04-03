"""Output formatting: JSON (default) or table."""

from __future__ import annotations

import json
import sys
from typing import Any

from rich.console import Console
from rich.table import Table

console = Console()

_json_mode = True


def set_json_mode(enabled: bool) -> None:
    global _json_mode
    _json_mode = enabled


def print_json(data: Any) -> None:
    if hasattr(data, "to_dict"):
        data = data.to_dict()
    json.dump(data, sys.stdout, indent=2, default=str)
    print()


def print_table(rows: list[dict], columns: list[str] | None = None) -> None:
    if not rows:
        console.print("[dim]No results[/dim]")
        return
    if columns is None:
        columns = list(rows[0].keys())
    table = Table()
    for col in columns:
        table.add_column(col)
    for row in rows:
        table.add_row(*[str(row.get(col, "")) for col in columns])
    console.print(table)


def output(data: Any, columns: list[str] | None = None) -> None:
    if data is None:
        console.print("[red]Error: API returned no data (check license or permissions).[/red]", file=sys.stderr)
        return
    if _json_mode:
        print_json(data)
        return
    if hasattr(data, "to_dict"):
        data = data.to_dict()
    if isinstance(data, dict) and "data" in data:
        rows = data["data"]
    elif isinstance(data, list):
        rows = data
    else:
        print_json(data)
        return
    if rows and isinstance(rows[0], dict):
        print_table(rows, columns)
    else:
        print_json(data)
