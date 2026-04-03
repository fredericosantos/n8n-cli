# n8n CLI

A command-line interface for the [n8n](https://n8n.io) Public API. Built from n8n's OpenAPI spec — every public endpoint is available as a CLI command.

## Install

```bash
# Clone and install
git clone https://github.com/fredericosantos/n8n-cli.git
cd n8n-cli
uv sync

# Or install directly
uv tool install git+https://github.com/fredericosantos/n8n-cli.git
```

Requires Python 3.13+.

## Setup

Generate an API key in your n8n instance: **Settings → API → Create API Key**.

Then configure:

```bash
n8n configure
# Prompts for base URL and API key
```

Or use environment variables:

```bash
export N8N_BASE_URL=https://n8n.example.com
export N8N_API_KEY=your-api-key
```

Config is saved to `~/.config/n8n-cli/config.json` (mode 600). Env vars take precedence.

## Usage

```bash
# List workflows
n8n workflows list

# Rich table output
n8n -t workflows list

# Get a specific workflow
n8n workflows get <id>

# Activate/deactivate
n8n workflows activate <id>
n8n workflows deactivate <id>

# List credentials
n8n credentials list

# List executions (filter by workflow)
n8n executions list --workflow <id>

# Security audit
n8n audit

# Discover API capabilities
n8n discover
```

### Output

JSON by default (pipe-friendly). Use `--table` / `-t` for formatted tables:

```bash
n8n -t workflows list
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃ id               ┃ name                   ┃ active ┃ updatedAt             ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ UBqa9n7OeJM4mUhD │ WF1: Process Booking   │ True   │ 2026-03-29T21:27:39   │
│ mqpclGn0E9O6tlxF │ WF3: Status Sync       │ True   │ 2026-03-29T22:01:24   │
└──────────────────┴────────────────────────┴────────┴───────────────────────┘
```

## Commands

| Command | Subcommands |
|---|---|
| `workflows` | list, get, activate, deactivate, delete, archive, unarchive, transfer, tags |
| `executions` | list, get, delete, stop, retry, tags |
| `credentials` | list, delete, schema, transfer |
| `tags` | list, get, delete |
| `users` | list, get, delete |
| `variables` | list, delete |
| `projects` | list, delete, users |
| `packages` | list, uninstall |
| `data-tables` | list, get, delete, rows |
| `source-control` | pull |
| `audit` | *(generates security report)* |
| `discover` | *(lists API capabilities)* |

## How it was built

1. Downloaded n8n's OpenAPI 3.0 spec from the [n8n repo](https://github.com/n8n-io/n8n/tree/master/packages/cli/src/public-api/v1)
2. Bundled the multi-file spec with `@redocly/cli`
3. Generated a typed Python client with `openapi-python-client`
4. Added a `typer` CLI layer on top

The generated client lives in `n8n_client/` and can be used as a Python library independently.

## Python library usage

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
    workflows = get_workflows.sync(client=c)
    for wf in workflows.data:
        print(wf.name, wf.active)
```

## License

MIT
