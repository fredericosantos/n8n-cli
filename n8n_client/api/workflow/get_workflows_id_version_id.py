from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_workflows_id_version_id_response_200 import GetWorkflowsIdVersionIdResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    version_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workflows/{id}/{version_id}".format(
            id=quote(str(id), safe=""),
            version_id=quote(str(version_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetWorkflowsIdVersionIdResponse200 | None:
    if response.status_code == 200:
        response_200 = GetWorkflowsIdVersionIdResponse200.from_dict(response.json())

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
) -> Response[Any | GetWorkflowsIdVersionIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetWorkflowsIdVersionIdResponse200]:
    """Retrieves a specific version of a workflow

     Retrieves a specific version of a workflow from workflow history.

    Args:
        id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetWorkflowsIdVersionIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        version_id=version_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetWorkflowsIdVersionIdResponse200 | None:
    """Retrieves a specific version of a workflow

     Retrieves a specific version of a workflow from workflow history.

    Args:
        id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetWorkflowsIdVersionIdResponse200
    """

    return sync_detailed(
        id=id,
        version_id=version_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetWorkflowsIdVersionIdResponse200]:
    """Retrieves a specific version of a workflow

     Retrieves a specific version of a workflow from workflow history.

    Args:
        id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetWorkflowsIdVersionIdResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        version_id=version_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetWorkflowsIdVersionIdResponse200 | None:
    """Retrieves a specific version of a workflow

     Retrieves a specific version of a workflow from workflow history.

    Args:
        id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetWorkflowsIdVersionIdResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            version_id=version_id,
            client=client,
        )
    ).parsed
