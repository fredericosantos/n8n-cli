"""n8n CLI — command-line interface for the n8n Public API."""

from __future__ import annotations

from typing import Annotated, Optional

import typer

from n8n_cli.config import get_client, save_config
from n8n_cli.output import output, set_json_mode

app = typer.Typer(name="n8n", help="CLI for the n8n Public API.", no_args_is_help=True)


# ---------------------------------------------------------------------------
# Global options callback
# ---------------------------------------------------------------------------
@app.callback()
def main(
    table: Annotated[bool, typer.Option("--table", "-t", help="Output as rich table instead of JSON.")] = False,
):
    if table:
        set_json_mode(False)


# ---------------------------------------------------------------------------
# configure
# ---------------------------------------------------------------------------
@app.command()
def configure(
    base_url: Annotated[str, typer.Option(prompt="n8n base URL (e.g. https://n8n.example.com)")],
    api_key: Annotated[str, typer.Option(prompt="API key", hide_input=True)],
):
    """Save n8n connection settings."""
    save_config(base_url, api_key)
    typer.echo("Configuration saved.")


# ---------------------------------------------------------------------------
# discover
# ---------------------------------------------------------------------------
@app.command()
def discover():
    """Discover available API capabilities."""
    from n8n_client.api.discover import get_discover

    with get_client() as c:
        output(get_discover.sync(client=c))


# ---------------------------------------------------------------------------
# workflows
# ---------------------------------------------------------------------------
wf_app = typer.Typer(name="workflows", help="Manage workflows.", no_args_is_help=True)
app.add_typer(wf_app)


@wf_app.command("list")
def wf_list(
    active: Annotated[Optional[bool], typer.Option(help="Filter by active status.")] = None,
    tags: Annotated[Optional[str], typer.Option(help="Comma-separated tag names.")] = None,
    name: Annotated[Optional[str], typer.Option(help="Filter by workflow name.")] = None,
    limit: Annotated[int, typer.Option(help="Max results.")] = 100,
):
    """List all workflows."""
    from n8n_client.api.workflow import get_workflows
    from n8n_client.types import UNSET

    with get_client() as c:
        output(
            get_workflows.sync(
                client=c,
                active=active if active is not None else UNSET,
                tags=tags or UNSET,
                name=name or UNSET,
                limit=float(limit),
            ),
            columns=["id", "name", "active", "updatedAt"],
        )


@wf_app.command("get")
def wf_get(id: Annotated[str, typer.Argument(help="Workflow ID.")]):
    """Get a workflow by ID."""
    from n8n_client.api.workflow import get_workflows_id

    with get_client() as c:
        output(get_workflows_id.sync(client=c, id=id))


@wf_app.command("activate")
def wf_activate(id: Annotated[str, typer.Argument(help="Workflow ID.")]):
    """Activate a workflow."""
    from n8n_client.api.workflow import post_workflows_id_activate

    with get_client() as c:
        output(post_workflows_id_activate.sync(client=c, id=id))


@wf_app.command("deactivate")
def wf_deactivate(id: Annotated[str, typer.Argument(help="Workflow ID.")]):
    """Deactivate a workflow."""
    from n8n_client.api.workflow import post_workflows_id_deactivate

    with get_client() as c:
        output(post_workflows_id_deactivate.sync(client=c, id=id))


@wf_app.command("delete")
def wf_delete(id: Annotated[str, typer.Argument(help="Workflow ID.")]):
    """Delete a workflow."""
    from n8n_client.api.workflow import delete_workflows_id

    with get_client() as c:
        delete_workflows_id.sync(client=c, id=id)
        typer.echo(f"Workflow {id} deleted.")


@wf_app.command("archive")
def wf_archive(id: Annotated[str, typer.Argument(help="Workflow ID.")]):
    """Archive a workflow."""
    from n8n_client.api.workflow import post_workflows_id_archive

    with get_client() as c:
        output(post_workflows_id_archive.sync(client=c, id=id))


@wf_app.command("unarchive")
def wf_unarchive(id: Annotated[str, typer.Argument(help="Workflow ID.")]):
    """Unarchive a workflow."""
    from n8n_client.api.workflow import post_workflows_id_unarchive

    with get_client() as c:
        output(post_workflows_id_unarchive.sync(client=c, id=id))


@wf_app.command("transfer")
def wf_transfer(
    id: Annotated[str, typer.Argument(help="Workflow ID.")],
    project_id: Annotated[str, typer.Option("--project", help="Destination project ID.")],
):
    """Transfer a workflow to another project."""
    from n8n_client.api.workflow import put_workflows_id_transfer

    with get_client() as c:
        put_workflows_id_transfer.sync(client=c, id=id)
        typer.echo(f"Workflow {id} transferred.")


@wf_app.command("tags")
def wf_tags(id: Annotated[str, typer.Argument(help="Workflow ID.")]):
    """Get tags for a workflow."""
    from n8n_client.api.workflow import get_workflows_id_tags

    with get_client() as c:
        output(get_workflows_id_tags.sync(client=c, id=id))


# ---------------------------------------------------------------------------
# executions
# ---------------------------------------------------------------------------
exec_app = typer.Typer(name="executions", help="Manage executions.", no_args_is_help=True)
app.add_typer(exec_app)


@exec_app.command("list")
def exec_list(
    workflow_id: Annotated[Optional[str], typer.Option("--workflow", help="Filter by workflow ID.")] = None,
    status: Annotated[Optional[str], typer.Option(help="Filter by status.")] = None,
    limit: Annotated[int, typer.Option(help="Max results.")] = 100,
):
    """List all executions."""
    from n8n_client.api.execution import get_executions
    from n8n_client.types import UNSET

    with get_client() as c:
        output(
            get_executions.sync(
                client=c,
                workflow_id=workflow_id or UNSET,
                status=status or UNSET,
                limit=float(limit),
            ),
            columns=["id", "workflowId", "status", "startedAt", "stoppedAt"],
        )


@exec_app.command("get")
def exec_get(id: Annotated[str, typer.Argument(help="Execution ID.")]):
    """Get an execution by ID."""
    from n8n_client.api.execution import get_executions_id

    with get_client() as c:
        output(get_executions_id.sync(client=c, id=id))


@exec_app.command("delete")
def exec_delete(id: Annotated[str, typer.Argument(help="Execution ID.")]):
    """Delete an execution."""
    from n8n_client.api.execution import delete_executions_id

    with get_client() as c:
        delete_executions_id.sync(client=c, id=id)
        typer.echo(f"Execution {id} deleted.")


@exec_app.command("stop")
def exec_stop(id: Annotated[str, typer.Argument(help="Execution ID.")]):
    """Stop a running execution."""
    from n8n_client.api.execution import post_executions_id_stop

    with get_client() as c:
        output(post_executions_id_stop.sync(client=c, id=id))


@exec_app.command("retry")
def exec_retry(id: Annotated[str, typer.Argument(help="Execution ID.")]):
    """Retry a failed execution."""
    from n8n_client.api.execution import post_executions_id_retry

    with get_client() as c:
        output(post_executions_id_retry.sync(client=c, id=id))


@exec_app.command("tags")
def exec_tags(id: Annotated[str, typer.Argument(help="Execution ID.")]):
    """Get tags for an execution."""
    from n8n_client.api.execution import get_executions_id_tags

    with get_client() as c:
        output(get_executions_id_tags.sync(client=c, id=id))


# ---------------------------------------------------------------------------
# credentials
# ---------------------------------------------------------------------------
cred_app = typer.Typer(name="credentials", help="Manage credentials.", no_args_is_help=True)
app.add_typer(cred_app)


@cred_app.command("list")
def cred_list(limit: Annotated[int, typer.Option(help="Max results.")] = 100):
    """List all credentials."""
    from n8n_client.api.credential import get_credentials

    with get_client() as c:
        output(
            get_credentials.sync(client=c, limit=float(limit)),
            columns=["id", "name", "type", "createdAt"],
        )


@cred_app.command("delete")
def cred_delete(id: Annotated[str, typer.Argument(help="Credential ID.")]):
    """Delete a credential."""
    from n8n_client.api.credential import delete_credential

    with get_client() as c:
        delete_credential.sync(client=c, id=id)
        typer.echo(f"Credential {id} deleted.")


@cred_app.command("schema")
def cred_schema(
    type_name: Annotated[str, typer.Argument(help="Credential type name (e.g. 'gmailOAuth2Api').")],
):
    """Show the data schema for a credential type."""
    from n8n_client.api.credential import get_credentials_schema_credential_type_name

    with get_client() as c:
        output(get_credentials_schema_credential_type_name.sync(client=c, credential_type_name=type_name))


@cred_app.command("transfer")
def cred_transfer(
    id: Annotated[str, typer.Argument(help="Credential ID.")],
    project_id: Annotated[str, typer.Option("--project", help="Destination project ID.")],
):
    """Transfer a credential to another project."""
    from n8n_client.api.credential import put_credentials_id_transfer

    with get_client() as c:
        put_credentials_id_transfer.sync(client=c, id=id)
        typer.echo(f"Credential {id} transferred.")


# ---------------------------------------------------------------------------
# tags
# ---------------------------------------------------------------------------
tags_app = typer.Typer(name="tags", help="Manage tags.", no_args_is_help=True)
app.add_typer(tags_app)


@tags_app.command("list")
def tags_list(limit: Annotated[int, typer.Option(help="Max results.")] = 100):
    """List all tags."""
    from n8n_client.api.tags import get_tags

    with get_client() as c:
        output(get_tags.sync(client=c, limit=float(limit)), columns=["id", "name", "createdAt"])


@tags_app.command("get")
def tags_get(id: Annotated[str, typer.Argument(help="Tag ID.")]):
    """Get a tag by ID."""
    from n8n_client.api.tags import get_tags_id

    with get_client() as c:
        output(get_tags_id.sync(client=c, id=id))


@tags_app.command("delete")
def tags_delete(id: Annotated[str, typer.Argument(help="Tag ID.")]):
    """Delete a tag."""
    from n8n_client.api.tags import delete_tags_id

    with get_client() as c:
        delete_tags_id.sync(client=c, id=id)
        typer.echo(f"Tag {id} deleted.")


# ---------------------------------------------------------------------------
# users
# ---------------------------------------------------------------------------
users_app = typer.Typer(name="users", help="Manage users.", no_args_is_help=True)
app.add_typer(users_app)


@users_app.command("list")
def users_list(limit: Annotated[int, typer.Option(help="Max results.")] = 100):
    """List all users."""
    from n8n_client.api.user import get_users

    with get_client() as c:
        output(
            get_users.sync(client=c, limit=float(limit)),
            columns=["id", "email", "firstName", "lastName", "role", "isPending"],
        )


@users_app.command("get")
def users_get(id: Annotated[str, typer.Argument(help="User ID or email.")]):
    """Get a user by ID or email."""
    from n8n_client.api.user import get_users_id

    with get_client() as c:
        output(get_users_id.sync(client=c, id=id))


@users_app.command("delete")
def users_delete(id: Annotated[str, typer.Argument(help="User ID.")]):
    """Delete a user."""
    from n8n_client.api.user import delete_users_id

    with get_client() as c:
        delete_users_id.sync(client=c, id=id)
        typer.echo(f"User {id} deleted.")


# ---------------------------------------------------------------------------
# variables
# ---------------------------------------------------------------------------
var_app = typer.Typer(name="variables", help="Manage environment variables.", no_args_is_help=True)
app.add_typer(var_app)


@var_app.command("list")
def var_list(limit: Annotated[int, typer.Option(help="Max results.")] = 100):
    """List all variables."""
    from n8n_client.api.variables import get_variables

    with get_client() as c:
        output(get_variables.sync(client=c, limit=float(limit)), columns=["id", "key", "value"])


@var_app.command("delete")
def var_delete(id: Annotated[str, typer.Argument(help="Variable ID.")]):
    """Delete a variable."""
    from n8n_client.api.variables import delete_variables_id

    with get_client() as c:
        delete_variables_id.sync(client=c, id=id)
        typer.echo(f"Variable {id} deleted.")


# ---------------------------------------------------------------------------
# projects
# ---------------------------------------------------------------------------
proj_app = typer.Typer(name="projects", help="Manage projects.", no_args_is_help=True)
app.add_typer(proj_app)


@proj_app.command("list")
def proj_list():
    """List all projects."""
    from n8n_client.api.projects import get_projects

    with get_client() as c:
        output(get_projects.sync(client=c), columns=["id", "name", "type"])


@proj_app.command("delete")
def proj_delete(id: Annotated[str, typer.Argument(help="Project ID.")]):
    """Delete a project."""
    from n8n_client.api.projects import delete_projects_project_id

    with get_client() as c:
        delete_projects_project_id.sync(client=c, project_id=id)
        typer.echo(f"Project {id} deleted.")


@proj_app.command("users")
def proj_users(id: Annotated[str, typer.Argument(help="Project ID.")]):
    """List users in a project."""
    from n8n_client.api.projects import get_projects_project_id_users

    with get_client() as c:
        output(get_projects_project_id_users.sync(client=c, project_id=id))


# ---------------------------------------------------------------------------
# packages (community)
# ---------------------------------------------------------------------------
pkg_app = typer.Typer(name="packages", help="Manage community packages.", no_args_is_help=True)
app.add_typer(pkg_app)


@pkg_app.command("list")
def pkg_list():
    """List installed community packages."""
    from n8n_client.api.community_package import get_community_packages

    with get_client() as c:
        output(get_community_packages.sync(client=c), columns=["packageName", "installedVersion"])


@pkg_app.command("uninstall")
def pkg_uninstall(name: Annotated[str, typer.Argument(help="Package name.")]):
    """Uninstall a community package."""
    from n8n_client.api.community_package import delete_community_packages_name

    with get_client() as c:
        delete_community_packages_name.sync(client=c, name=name)
        typer.echo(f"Package {name} uninstalled.")


# ---------------------------------------------------------------------------
# source-control
# ---------------------------------------------------------------------------
sc_app = typer.Typer(name="source-control", help="Source control operations.", no_args_is_help=True)
app.add_typer(sc_app)


@sc_app.command("pull")
def sc_pull():
    """Pull changes from the remote repository."""
    from n8n_client.api.source_control import post_source_control_pull

    with get_client() as c:
        output(post_source_control_pull.sync(client=c))


# ---------------------------------------------------------------------------
# audit
# ---------------------------------------------------------------------------
@app.command()
def audit():
    """Generate a security audit report."""
    from n8n_client.api.audit import post_audit

    with get_client() as c:
        output(post_audit.sync(client=c))


# ---------------------------------------------------------------------------
# data-tables
# ---------------------------------------------------------------------------
dt_app = typer.Typer(name="data-tables", help="Manage data tables.", no_args_is_help=True)
app.add_typer(dt_app)


@dt_app.command("list")
def dt_list():
    """List all data tables."""
    from n8n_client.api.data_table import list_data_tables

    with get_client() as c:
        output(list_data_tables.sync(client=c), columns=["id", "name", "createdAt"])


@dt_app.command("get")
def dt_get(id: Annotated[str, typer.Argument(help="Data table ID.")]):
    """Get a data table by ID."""
    from n8n_client.api.data_table import get_data_table

    with get_client() as c:
        output(get_data_table.sync(client=c, data_table_id=id))


@dt_app.command("delete")
def dt_delete(id: Annotated[str, typer.Argument(help="Data table ID.")]):
    """Delete a data table."""
    from n8n_client.api.data_table import delete_data_table

    with get_client() as c:
        delete_data_table.sync(client=c, data_table_id=id)
        typer.echo(f"Data table {id} deleted.")


@dt_app.command("rows")
def dt_rows(
    id: Annotated[str, typer.Argument(help="Data table ID.")],
    limit: Annotated[int, typer.Option(help="Max results.")] = 100,
):
    """List rows in a data table."""
    from n8n_client.api.data_table import get_data_table_rows

    with get_client() as c:
        output(get_data_table_rows.sync(client=c, data_table_id=id, limit=float(limit)))


if __name__ == "__main__":
    app()
