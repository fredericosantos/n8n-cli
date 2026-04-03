# n8n CLI — Agent Reference

CLI and Python client for the n8n Public API. Use this to manage workflows, credentials, executions, and all other n8n resources programmatically.

## Quick start

```bash
# Set connection (env vars or config file)
export N8N_BASE_URL=http://localhost:5678
export N8N_API_KEY=<api-key>

# Run commands
n8n workflows list          # JSON output (default)
n8n -t workflows list       # table output
n8n workflows get <id>      # single workflow details
```

## Authentication

n8n uses API key auth via `X-N8N-API-KEY` header. Generate a key at: **n8n UI → Settings → API → Create API Key**.

Config priority: env vars (`N8N_BASE_URL`, `N8N_API_KEY`) > config file (`~/.config/n8n-cli/config.json`).

## Available commands

```
n8n workflows    list | get <id> | activate <id> | deactivate <id> | delete <id> | archive <id> | unarchive <id> | transfer <id> --project <pid> | tags <id>
n8n executions   list [--workflow <id>] [--status <s>] | get <id> | delete <id> | stop <id> | retry <id> | tags <id>
n8n credentials  list | delete <id> | schema <type> | transfer <id> --project <pid>
n8n tags         list | get <id> | delete <id>
n8n users        list | get <id> | delete <id>
n8n variables    list | delete <id>
n8n projects     list | delete <id> | users <id>
n8n packages     list | uninstall <name>
n8n data-tables  list | get <id> | delete <id> | rows <id>
n8n source-control pull
n8n audit
n8n discover
```

## Output format

- **Default: JSON** — pipe to `jq`, parse programmatically
- **`-t` / `--table`** — rich formatted tables for human reading

## Python library usage

The generated client in `n8n_client/` can be imported directly:

```python
from n8n_client.client import AuthenticatedClient
from n8n_client.api.workflow import get_workflows

client = AuthenticatedClient(
    base_url="https://n8n.example.com/api/v1",
    token="your-api-key",
    auth_header_name="X-N8N-API-KEY",
    prefix="",
)
with client as c:
    result = get_workflows.sync(client=c)
```

Each API module exposes: `sync()`, `sync_detailed()`, `asyncio()`, `asyncio_detailed()`.

## API coverage

Built from n8n OpenAPI spec v1.1.0. Covers all 41 public API endpoints across 12 resource types. Some endpoints (variables, source-control) require paid n8n licenses.

## Project structure

```
n8n_cli/         CLI layer (typer)
  main.py        All commands
  config.py      Auth & connection config
  output.py      JSON/table formatting
n8n_client/      Generated API client (httpx + attrs)
  api/           One module per resource (workflow, credential, etc.)
  models/        Typed request/response models
  client.py      AuthenticatedClient class
```
