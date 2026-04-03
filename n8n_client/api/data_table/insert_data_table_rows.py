from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.insert_data_table_rows_body import InsertDataTableRowsBody
from ...models.insert_data_table_rows_response_200_type_0 import InsertDataTableRowsResponse200Type0
from ...models.insert_data_table_rows_response_200_type_2_item import InsertDataTableRowsResponse200Type2Item
from ...types import Response


def _get_kwargs(
    data_table_id: str,
    *,
    body: InsertDataTableRowsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/data-tables/{data_table_id}/rows".format(
            data_table_id=quote(str(data_table_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | InsertDataTableRowsResponse200Type0 | list[InsertDataTableRowsResponse200Type2Item] | list[int] | None:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> InsertDataTableRowsResponse200Type0 | list[InsertDataTableRowsResponse200Type2Item] | list[int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = InsertDataTableRowsResponse200Type0.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_1 = cast(list[int], data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            response_200_type_2 = []
            _response_200_type_2 = data
            for response_200_type_2_item_data in _response_200_type_2:
                response_200_type_2_item = InsertDataTableRowsResponse200Type2Item.from_dict(
                    response_200_type_2_item_data
                )

                response_200_type_2.append(response_200_type_2_item)

            return response_200_type_2

        response_200 = _parse_response_200(response.json())

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
) -> Response[Any | InsertDataTableRowsResponse200Type0 | list[InsertDataTableRowsResponse200Type2Item] | list[int]]:
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
    body: InsertDataTableRowsBody,
) -> Response[Any | InsertDataTableRowsResponse200Type0 | list[InsertDataTableRowsResponse200Type2Item] | list[int]]:
    """Insert rows into a data table

     Insert one or more rows into a data table.

    Args:
        data_table_id (str):
        body (InsertDataTableRowsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InsertDataTableRowsResponse200Type0 | list[InsertDataTableRowsResponse200Type2Item] | list[int]]
    """

    kwargs = _get_kwargs(
        data_table_id=data_table_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_table_id: str,
    *,
    client: AuthenticatedClient,
    body: InsertDataTableRowsBody,
) -> Any | InsertDataTableRowsResponse200Type0 | list[InsertDataTableRowsResponse200Type2Item] | list[int] | None:
    """Insert rows into a data table

     Insert one or more rows into a data table.

    Args:
        data_table_id (str):
        body (InsertDataTableRowsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InsertDataTableRowsResponse200Type0 | list[InsertDataTableRowsResponse200Type2Item] | list[int]
    """

    return sync_detailed(
        data_table_id=data_table_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    data_table_id: str,
    *,
    client: AuthenticatedClient,
    body: InsertDataTableRowsBody,
) -> Response[Any | InsertDataTableRowsResponse200Type0 | list[InsertDataTableRowsResponse200Type2Item] | list[int]]:
    """Insert rows into a data table

     Insert one or more rows into a data table.

    Args:
        data_table_id (str):
        body (InsertDataTableRowsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InsertDataTableRowsResponse200Type0 | list[InsertDataTableRowsResponse200Type2Item] | list[int]]
    """

    kwargs = _get_kwargs(
        data_table_id=data_table_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_table_id: str,
    *,
    client: AuthenticatedClient,
    body: InsertDataTableRowsBody,
) -> Any | InsertDataTableRowsResponse200Type0 | list[InsertDataTableRowsResponse200Type2Item] | list[int] | None:
    """Insert rows into a data table

     Insert one or more rows into a data table.

    Args:
        data_table_id (str):
        body (InsertDataTableRowsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InsertDataTableRowsResponse200Type0 | list[InsertDataTableRowsResponse200Type2Item] | list[int]
    """

    return (
        await asyncio_detailed(
            data_table_id=data_table_id,
            client=client,
            body=body,
        )
    ).parsed
