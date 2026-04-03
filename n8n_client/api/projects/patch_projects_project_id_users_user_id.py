from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_projects_project_id_users_user_id_body import PatchProjectsProjectIdUsersUserIdBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    user_id: str,
    *,
    body: PatchProjectsProjectIdUsersUserIdBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/projects/{project_id}/users/{user_id}".format(
            project_id=quote(str(project_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchProjectsProjectIdUsersUserIdBody | Unset = UNSET,
) -> Response[Any]:
    """Change a user's role in a project

     Change a user's role in a project.

    Args:
        project_id (str):
        user_id (str):
        body (PatchProjectsProjectIdUsersUserIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchProjectsProjectIdUsersUserIdBody | Unset = UNSET,
) -> Response[Any]:
    """Change a user's role in a project

     Change a user's role in a project.

    Args:
        project_id (str):
        user_id (str):
        body (PatchProjectsProjectIdUsersUserIdBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
