from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_data_table_rows_response_200_type_1_item import DeleteDataTableRowsResponse200Type1Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    data_table_id: str,
    *,
    filter_: str,
    return_data: bool | Unset = False,
    dry_run: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["filter"] = filter_

    params["returnData"] = return_data

    params["dryRun"] = dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/data-tables/{data_table_id}/rows/delete".format(
            data_table_id=quote(str(data_table_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | bool | list[DeleteDataTableRowsResponse200Type1Item] | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> bool | list[DeleteDataTableRowsResponse200Type1Item]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_1 = []
                _response_200_type_1 = data
                for response_200_type_1_item_data in _response_200_type_1:
                    response_200_type_1_item = DeleteDataTableRowsResponse200Type1Item.from_dict(
                        response_200_type_1_item_data
                    )

                    response_200_type_1.append(response_200_type_1_item)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | list[DeleteDataTableRowsResponse200Type1Item], data)

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
) -> Response[Any | bool | list[DeleteDataTableRowsResponse200Type1Item]]:
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
    filter_: str,
    return_data: bool | Unset = False,
    dry_run: bool | Unset = False,
) -> Response[Any | bool | list[DeleteDataTableRowsResponse200Type1Item]]:
    """Delete rows from a data table

     Delete rows matching filter conditions from a data table. Filter is required to prevent accidental
    deletion of all data.

    Args:
        data_table_id (str):
        filter_ (str):
        return_data (bool | Unset):  Default: False.
        dry_run (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | bool | list[DeleteDataTableRowsResponse200Type1Item]]
    """

    kwargs = _get_kwargs(
        data_table_id=data_table_id,
        filter_=filter_,
        return_data=return_data,
        dry_run=dry_run,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_table_id: str,
    *,
    client: AuthenticatedClient,
    filter_: str,
    return_data: bool | Unset = False,
    dry_run: bool | Unset = False,
) -> Any | bool | list[DeleteDataTableRowsResponse200Type1Item] | None:
    """Delete rows from a data table

     Delete rows matching filter conditions from a data table. Filter is required to prevent accidental
    deletion of all data.

    Args:
        data_table_id (str):
        filter_ (str):
        return_data (bool | Unset):  Default: False.
        dry_run (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | bool | list[DeleteDataTableRowsResponse200Type1Item]
    """

    return sync_detailed(
        data_table_id=data_table_id,
        client=client,
        filter_=filter_,
        return_data=return_data,
        dry_run=dry_run,
    ).parsed


async def asyncio_detailed(
    data_table_id: str,
    *,
    client: AuthenticatedClient,
    filter_: str,
    return_data: bool | Unset = False,
    dry_run: bool | Unset = False,
) -> Response[Any | bool | list[DeleteDataTableRowsResponse200Type1Item]]:
    """Delete rows from a data table

     Delete rows matching filter conditions from a data table. Filter is required to prevent accidental
    deletion of all data.

    Args:
        data_table_id (str):
        filter_ (str):
        return_data (bool | Unset):  Default: False.
        dry_run (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | bool | list[DeleteDataTableRowsResponse200Type1Item]]
    """

    kwargs = _get_kwargs(
        data_table_id=data_table_id,
        filter_=filter_,
        return_data=return_data,
        dry_run=dry_run,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_table_id: str,
    *,
    client: AuthenticatedClient,
    filter_: str,
    return_data: bool | Unset = False,
    dry_run: bool | Unset = False,
) -> Any | bool | list[DeleteDataTableRowsResponse200Type1Item] | None:
    """Delete rows from a data table

     Delete rows matching filter conditions from a data table. Filter is required to prevent accidental
    deletion of all data.

    Args:
        data_table_id (str):
        filter_ (str):
        return_data (bool | Unset):  Default: False.
        dry_run (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | bool | list[DeleteDataTableRowsResponse200Type1Item]
    """

    return (
        await asyncio_detailed(
            data_table_id=data_table_id,
            client=client,
            filter_=filter_,
            return_data=return_data,
            dry_run=dry_run,
        )
    ).parsed
