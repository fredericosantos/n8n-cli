"""Smoke tests for the n8n CLI."""

from typer.testing import CliRunner

from n8n_cli.main import app

runner = CliRunner()


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "n8n Public API" in result.output


def test_workflows_help():
    result = runner.invoke(app, ["workflows", "--help"])
    assert result.exit_code == 0
    assert "list" in result.output
    assert "get" in result.output
    assert "activate" in result.output


def test_credentials_help():
    result = runner.invoke(app, ["credentials", "--help"])
    assert result.exit_code == 0
    assert "list" in result.output
    assert "schema" in result.output


def test_no_config_shows_error(monkeypatch, tmp_path):
    monkeypatch.delenv("N8N_BASE_URL", raising=False)
    monkeypatch.delenv("N8N_API_KEY", raising=False)
    monkeypatch.setattr("n8n_cli.config.CONFIG_PATH", tmp_path / "nonexistent.json")
    result = runner.invoke(app, ["workflows", "list"])
    assert result.exit_code != 0
