from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_data_table_rows_response_200 import GetDataTableRowsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    data_table_id: str,
    *,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["filter"] = filter_

    params["sortBy"] = sort_by

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/data-tables/{data_table_id}/rows".format(
            data_table_id=quote(str(data_table_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetDataTableRowsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetDataTableRowsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
) -> Response[Any | GetDataTableRowsResponse200]:
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
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[Any | GetDataTableRowsResponse200]:
    """Retrieve rows from a data table

     Query and retrieve rows from a data table with optional filtering, sorting, and pagination.

    Args:
        data_table_id (str):
        limit (float | Unset):  Default: 100.0. Example: 100.
        cursor (str | Unset):
        filter_ (str | Unset):
        sort_by (str | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDataTableRowsResponse200]
    """

    kwargs = _get_kwargs(
        data_table_id=data_table_id,
        limit=limit,
        cursor=cursor,
        filter_=filter_,
        sort_by=sort_by,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_table_id: str,
    *,
    client: AuthenticatedClient,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Any | GetDataTableRowsResponse200 | None:
    """Retrieve rows from a data table

     Query and retrieve rows from a data table with optional filtering, sorting, and pagination.

    Args:
        data_table_id (str):
        limit (float | Unset):  Default: 100.0. Example: 100.
        cursor (str | Unset):
        filter_ (str | Unset):
        sort_by (str | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDataTableRowsResponse200
    """

    return sync_detailed(
        data_table_id=data_table_id,
        client=client,
        limit=limit,
        cursor=cursor,
        filter_=filter_,
        sort_by=sort_by,
        search=search,
    ).parsed


async def asyncio_detailed(
    data_table_id: str,
    *,
    client: AuthenticatedClient,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Response[Any | GetDataTableRowsResponse200]:
    """Retrieve rows from a data table

     Query and retrieve rows from a data table with optional filtering, sorting, and pagination.

    Args:
        data_table_id (str):
        limit (float | Unset):  Default: 100.0. Example: 100.
        cursor (str | Unset):
        filter_ (str | Unset):
        sort_by (str | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetDataTableRowsResponse200]
    """

    kwargs = _get_kwargs(
        data_table_id=data_table_id,
        limit=limit,
        cursor=cursor,
        filter_=filter_,
        sort_by=sort_by,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_table_id: str,
    *,
    client: AuthenticatedClient,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    sort_by: str | Unset = UNSET,
    search: str | Unset = UNSET,
) -> Any | GetDataTableRowsResponse200 | None:
    """Retrieve rows from a data table

     Query and retrieve rows from a data table with optional filtering, sorting, and pagination.

    Args:
        data_table_id (str):
        limit (float | Unset):  Default: 100.0. Example: 100.
        cursor (str | Unset):
        filter_ (str | Unset):
        sort_by (str | Unset):
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetDataTableRowsResponse200
    """

    return (
        await asyncio_detailed(
            data_table_id=data_table_id,
            client=client,
            limit=limit,
            cursor=cursor,
            filter_=filter_,
            sort_by=sort_by,
            search=search,
        )
    ).parsed
