from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_data_table_response_200 import GetDataTableResponse200
from ...types import Response


def _get_kwargs(
    data_table_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/data-tables/{data_table_id}".format(
            data_table_id=quote(str(data_table_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetDataTableResponse200 | None:
    if response.status_code == 200:
        response_200 = GetDataTableResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetDataTableResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_table_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | GetDataTableResponse200]:
    """Get a data table

     Retrieve a specific data table by ID.

    Args:
        data_table_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDataTableResponse200]
    """

    kwargs = _get_kwargs(
        data_table_id=data_table_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_table_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | GetDataTableResponse200 | None:
    """Get a data table

     Retrieve a specific data table by ID.

    Args:
        data_table_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDataTableResponse200
    """

    return sync_detailed(
        data_table_id=data_table_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    data_table_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | GetDataTableResponse200]:
    """Get a data table

     Retrieve a specific data table by ID.

    Args:
        data_table_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDataTableResponse200]
    """

    kwargs = _get_kwargs(
        data_table_id=data_table_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_table_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | GetDataTableResponse200 | None:
    """Get a data table

     Retrieve a specific data table by ID.

    Args:
        data_table_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDataTableResponse200
    """

    return (
        await asyncio_detailed(
            data_table_id=data_table_id,
            client=client,
        )
    ).parsed
