from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_workflows_id_response_200 import GetWorkflowsIdResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    exclude_pinned_data: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["excludePinnedData"] = exclude_pinned_data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workflows/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetWorkflowsIdResponse200 | None:
    if response.status_code == 200:
        response_200 = GetWorkflowsIdResponse200.from_dict(response.json())

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
) -> Response[Any | GetWorkflowsIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    exclude_pinned_data: bool | Unset = UNSET,
) -> Response[Any | GetWorkflowsIdResponse200]:
    """Retrieve a workflow

     Retrieve a workflow.

    Args:
        id (str):
        exclude_pinned_data (bool | Unset):  Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetWorkflowsIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        exclude_pinned_data=exclude_pinned_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    exclude_pinned_data: bool | Unset = UNSET,
) -> Any | GetWorkflowsIdResponse200 | None:
    """Retrieve a workflow

     Retrieve a workflow.

    Args:
        id (str):
        exclude_pinned_data (bool | Unset):  Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetWorkflowsIdResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        exclude_pinned_data=exclude_pinned_data,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    exclude_pinned_data: bool | Unset = UNSET,
) -> Response[Any | GetWorkflowsIdResponse200]:
    """Retrieve a workflow

     Retrieve a workflow.

    Args:
        id (str):
        exclude_pinned_data (bool | Unset):  Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetWorkflowsIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        exclude_pinned_data=exclude_pinned_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    exclude_pinned_data: bool | Unset = UNSET,
) -> Any | GetWorkflowsIdResponse200 | None:
    """Retrieve a workflow

     Retrieve a workflow.

    Args:
        id (str):
        exclude_pinned_data (bool | Unset):  Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetWorkflowsIdResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            exclude_pinned_data=exclude_pinned_data,
        )
    ).parsed
