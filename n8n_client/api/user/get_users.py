from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_response_200 import GetUsersResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
    include_role: bool | Unset = False,
    project_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["includeRole"] = include_role

    params["projectId"] = project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetUsersResponse200 | None:
    if response.status_code == 200:
        response_200 = GetUsersResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetUsersResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
    include_role: bool | Unset = False,
    project_id: str | Unset = UNSET,
) -> Response[Any | GetUsersResponse200]:
    """Retrieve all users

     Retrieve all users from your instance. Only available for the instance owner.

    Args:
        limit (float | Unset):  Default: 100.0. Example: 100.
        cursor (str | Unset):
        include_role (bool | Unset):  Default: False. Example: True.
        project_id (str | Unset):  Example: VmwOO9HeTEj20kxM.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUsersResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        include_role=include_role,
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
    include_role: bool | Unset = False,
    project_id: str | Unset = UNSET,
) -> Any | GetUsersResponse200 | None:
    """Retrieve all users

     Retrieve all users from your instance. Only available for the instance owner.

    Args:
        limit (float | Unset):  Default: 100.0. Example: 100.
        cursor (str | Unset):
        include_role (bool | Unset):  Default: False. Example: True.
        project_id (str | Unset):  Example: VmwOO9HeTEj20kxM.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUsersResponse200
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        include_role=include_role,
        project_id=project_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
    include_role: bool | Unset = False,
    project_id: str | Unset = UNSET,
) -> Response[Any | GetUsersResponse200]:
    """Retrieve all users

     Retrieve all users from your instance. Only available for the instance owner.

    Args:
        limit (float | Unset):  Default: 100.0. Example: 100.
        cursor (str | Unset):
        include_role (bool | Unset):  Default: False. Example: True.
        project_id (str | Unset):  Example: VmwOO9HeTEj20kxM.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUsersResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        include_role=include_role,
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
    include_role: bool | Unset = False,
    project_id: str | Unset = UNSET,
) -> Any | GetUsersResponse200 | None:
    """Retrieve all users

     Retrieve all users from your instance. Only available for the instance owner.

    Args:
        limit (float | Unset):  Default: 100.0. Example: 100.
        cursor (str | Unset):
        include_role (bool | Unset):  Default: False. Example: True.
        project_id (str | Unset):  Example: VmwOO9HeTEj20kxM.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUsersResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            include_role=include_role,
            project_id=project_id,
        )
    ).parsed
