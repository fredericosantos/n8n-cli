from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_projects_project_id_users_response_200 import GetProjectsProjectIdUsersResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/users".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetProjectsProjectIdUsersResponse200 | None:
    if response.status_code == 200:
        response_200 = GetProjectsProjectIdUsersResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetProjectsProjectIdUsersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
) -> Response[Any | GetProjectsProjectIdUsersResponse200]:
    """List project members

     Returns a list of all members of a project including their role. Requires user:list scope.

    Args:
        project_id (str):
        limit (float | Unset):  Default: 100.0. Example: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetProjectsProjectIdUsersResponse200]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
) -> Any | GetProjectsProjectIdUsersResponse200 | None:
    """List project members

     Returns a list of all members of a project including their role. Requires user:list scope.

    Args:
        project_id (str):
        limit (float | Unset):  Default: 100.0. Example: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetProjectsProjectIdUsersResponse200
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
) -> Response[Any | GetProjectsProjectIdUsersResponse200]:
    """List project members

     Returns a list of all members of a project including their role. Requires user:list scope.

    Args:
        project_id (str):
        limit (float | Unset):  Default: 100.0. Example: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetProjectsProjectIdUsersResponse200]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
) -> Any | GetProjectsProjectIdUsersResponse200 | None:
    """List project members

     Returns a list of all members of a project including their role. Requires user:list scope.

    Args:
        project_id (str):
        limit (float | Unset):  Default: 100.0. Example: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetProjectsProjectIdUsersResponse200
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
