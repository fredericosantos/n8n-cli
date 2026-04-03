"""Tests for config loading and client creation."""

import json

from n8n_cli.config import get_client, save_config


def test_save_and_load_config(tmp_path, monkeypatch):
    config_path = tmp_path / "config.json"
    monkeypatch.setattr("n8n_cli.config.CONFIG_PATH", config_path)
    monkeypatch.delenv("N8N_BASE_URL", raising=False)
    monkeypatch.delenv("N8N_API_KEY", raising=False)

    save_config("http://localhost:5678", "test-key")

    assert config_path.exists()
    cfg = json.loads(config_path.read_text())
    assert cfg["base_url"] == "http://localhost:5678"
    assert cfg["api_key"] == "test-key"

    client = get_client()
    assert "localhost:5678" in str(client._base_url)


def test_env_vars_take_precedence(tmp_path, monkeypatch):
    config_path = tmp_path / "config.json"
    monkeypatch.setattr("n8n_cli.config.CONFIG_PATH", config_path)
    save_config("http://from-file:5678", "file-key")

    monkeypatch.setenv("N8N_BASE_URL", "http://from-env:5678")
    monkeypatch.setenv("N8N_API_KEY", "env-key")

    client = get_client()
    assert "from-env" in str(client._base_url)
