"""Configuration: load n8n connection settings from env vars or config file."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from n8n_client.client import AuthenticatedClient

CONFIG_PATH = Path.home() / ".config" / "n8n-cli" / "config.json"

# Env vars (take precedence over config file)
ENV_BASE_URL = "N8N_BASE_URL"
ENV_API_KEY = "N8N_API_KEY"


def _load_config() -> dict:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text())
    return {}


def save_config(base_url: str, api_key: str) -> None:
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(json.dumps({"base_url": base_url, "api_key": api_key}, indent=2))
    CONFIG_PATH.chmod(0o600)


def get_client() -> AuthenticatedClient:
    cfg = _load_config()
    base_url = os.environ.get(ENV_BASE_URL, cfg.get("base_url", ""))
    api_key = os.environ.get(ENV_API_KEY, cfg.get("api_key", ""))

    if not base_url or not api_key:
        print("Error: n8n connection not configured.", file=sys.stderr)
        print(f"  Set {ENV_BASE_URL} and {ENV_API_KEY} env vars, or run: n8n configure", file=sys.stderr)
        sys.exit(1)

    # n8n uses X-N8N-API-KEY header (not Bearer)
    return AuthenticatedClient(
        base_url=base_url.rstrip("/") + "/api/v1",
        token=api_key,
        auth_header_name="X-N8N-API-KEY",
        prefix="",
        raise_on_unexpected_status=False,
    )
