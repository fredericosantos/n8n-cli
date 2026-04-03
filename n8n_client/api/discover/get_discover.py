from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_discover_include import GetDiscoverInclude
from ...models.get_discover_response_200 import GetDiscoverResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: GetDiscoverInclude | Unset = UNSET,
    resource: str | Unset = UNSET,
    operation: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include: str | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = include.value

    params["include"] = json_include

    params["resource"] = resource

    params["operation"] = operation

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/discover",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetDiscoverResponse200 | None:
    if response.status_code == 200:
        response_200 = GetDiscoverResponse200.from_dict(response.json())

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
) -> Response[Any | GetDiscoverResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    include: GetDiscoverInclude | Unset = UNSET,
    resource: str | Unset = UNSET,
    operation: str | Unset = UNSET,
) -> Response[Any | GetDiscoverResponse200]:
    """Discover available API capabilities

     Returns a filtered capability map based on the caller's API key scopes. Each resource includes the
    operations and endpoints accessible to the authenticated API key. Use query parameters to narrow the
    response.

    Args:
        include (GetDiscoverInclude | Unset):
        resource (str | Unset):
        operation (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDiscoverResponse200]
    """

    kwargs = _get_kwargs(
        include=include,
        resource=resource,
        operation=operation,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    include: GetDiscoverInclude | Unset = UNSET,
    resource: str | Unset = UNSET,
    operation: str | Unset = UNSET,
) -> Any | GetDiscoverResponse200 | None:
    """Discover available API capabilities

     Returns a filtered capability map based on the caller's API key scopes. Each resource includes the
    operations and endpoints accessible to the authenticated API key. Use query parameters to narrow the
    response.

    Args:
        include (GetDiscoverInclude | Unset):
        resource (str | Unset):
        operation (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDiscoverResponse200
    """

    return sync_detailed(
        client=client,
        include=include,
        resource=resource,
        operation=operation,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    include: GetDiscoverInclude | Unset = UNSET,
    resource: str | Unset = UNSET,
    operation: str | Unset = UNSET,
) -> Response[Any | GetDiscoverResponse200]:
    """Discover available API capabilities

     Returns a filtered capability map based on the caller's API key scopes. Each resource includes the
    operations and endpoints accessible to the authenticated API key. Use query parameters to narrow the
    response.

    Args:
        include (GetDiscoverInclude | Unset):
        resource (str | Unset):
        operation (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDiscoverResponse200]
    """

    kwargs = _get_kwargs(
        include=include,
        resource=resource,
        operation=operation,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    include: GetDiscoverInclude | Unset = UNSET,
    resource: str | Unset = UNSET,
    operation: str | Unset = UNSET,
) -> Any | GetDiscoverResponse200 | None:
    """Discover available API capabilities

     Returns a filtered capability map based on the caller's API key scopes. Each resource includes the
    operations and endpoints accessible to the authenticated API key. Use query parameters to narrow the
    response.

    Args:
        include (GetDiscoverInclude | Unset):
        resource (str | Unset):
        operation (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDiscoverResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            resource=resource,
            operation=operation,
        )
    ).parsed
