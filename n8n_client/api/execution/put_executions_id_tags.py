from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_executions_id_tags_body_item import PutExecutionsIdTagsBodyItem
from ...models.put_executions_id_tags_response_200_item import PutExecutionsIdTagsResponse200Item
from ...types import Response


def _get_kwargs(
    id: float,
    *,
    body: list[PutExecutionsIdTagsBodyItem],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/executions/{id}/tags".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[PutExecutionsIdTagsResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PutExecutionsIdTagsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | list[PutExecutionsIdTagsResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: float,
    *,
    client: AuthenticatedClient | Client,
    body: list[PutExecutionsIdTagsBodyItem],
) -> Response[Any | list[PutExecutionsIdTagsResponse200Item]]:
    """Update tags of an execution

     Update annotation tags of an execution.

    Args:
        id (float):
        body (list[PutExecutionsIdTagsBodyItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[PutExecutionsIdTagsResponse200Item]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: float,
    *,
    client: AuthenticatedClient | Client,
    body: list[PutExecutionsIdTagsBodyItem],
) -> Any | list[PutExecutionsIdTagsResponse200Item] | None:
    """Update tags of an execution

     Update annotation tags of an execution.

    Args:
        id (float):
        body (list[PutExecutionsIdTagsBodyItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[PutExecutionsIdTagsResponse200Item]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: float,
    *,
    client: AuthenticatedClient | Client,
    body: list[PutExecutionsIdTagsBodyItem],
) -> Response[Any | list[PutExecutionsIdTagsResponse200Item]]:
    """Update tags of an execution

     Update annotation tags of an execution.

    Args:
        id (float):
        body (list[PutExecutionsIdTagsBodyItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[PutExecutionsIdTagsResponse200Item]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: float,
    *,
    client: AuthenticatedClient | Client,
    body: list[PutExecutionsIdTagsBodyItem],
) -> Any | list[PutExecutionsIdTagsResponse200Item] | None:
    """Update tags of an execution

     Update annotation tags of an execution.

    Args:
        id (float):
        body (list[PutExecutionsIdTagsBodyItem]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[PutExecutionsIdTagsResponse200Item]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
