from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_workflows_response_200 import GetWorkflowsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    active: bool | Unset = UNSET,
    tags: str | Unset = UNSET,
    name: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    exclude_pinned_data: bool | Unset = UNSET,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["active"] = active

    params["tags"] = tags

    params["name"] = name

    params["projectId"] = project_id

    params["excludePinnedData"] = exclude_pinned_data

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workflows",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetWorkflowsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetWorkflowsResponse200.from_dict(response.json())

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
) -> Response[Any | GetWorkflowsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    active: bool | Unset = UNSET,
    tags: str | Unset = UNSET,
    name: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    exclude_pinned_data: bool | Unset = UNSET,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
) -> Response[Any | GetWorkflowsResponse200]:
    """Retrieve all workflows

     Retrieve all workflows from your instance.

    Args:
        active (bool | Unset):  Example: True.
        tags (str | Unset):  Example: test,production.
        name (str | Unset):  Example: My Workflow.
        project_id (str | Unset):  Example: VmwOO9HeTEj20kxM.
        exclude_pinned_data (bool | Unset):  Example: True.
        limit (float | Unset):  Default: 100.0. Example: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetWorkflowsResponse200]
    """

    kwargs = _get_kwargs(
        active=active,
        tags=tags,
        name=name,
        project_id=project_id,
        exclude_pinned_data=exclude_pinned_data,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    active: bool | Unset = UNSET,
    tags: str | Unset = UNSET,
    name: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    exclude_pinned_data: bool | Unset = UNSET,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
) -> Any | GetWorkflowsResponse200 | None:
    """Retrieve all workflows

     Retrieve all workflows from your instance.

    Args:
        active (bool | Unset):  Example: True.
        tags (str | Unset):  Example: test,production.
        name (str | Unset):  Example: My Workflow.
        project_id (str | Unset):  Example: VmwOO9HeTEj20kxM.
        exclude_pinned_data (bool | Unset):  Example: True.
        limit (float | Unset):  Default: 100.0. Example: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetWorkflowsResponse200
    """

    return sync_detailed(
        client=client,
        active=active,
        tags=tags,
        name=name,
        project_id=project_id,
        exclude_pinned_data=exclude_pinned_data,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    active: bool | Unset = UNSET,
    tags: str | Unset = UNSET,
    name: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    exclude_pinned_data: bool | Unset = UNSET,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
) -> Response[Any | GetWorkflowsResponse200]:
    """Retrieve all workflows

     Retrieve all workflows from your instance.

    Args:
        active (bool | Unset):  Example: True.
        tags (str | Unset):  Example: test,production.
        name (str | Unset):  Example: My Workflow.
        project_id (str | Unset):  Example: VmwOO9HeTEj20kxM.
        exclude_pinned_data (bool | Unset):  Example: True.
        limit (float | Unset):  Default: 100.0. Example: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetWorkflowsResponse200]
    """

    kwargs = _get_kwargs(
        active=active,
        tags=tags,
        name=name,
        project_id=project_id,
        exclude_pinned_data=exclude_pinned_data,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    active: bool | Unset = UNSET,
    tags: str | Unset = UNSET,
    name: str | Unset = UNSET,
    project_id: str | Unset = UNSET,
    exclude_pinned_data: bool | Unset = UNSET,
    limit: float | Unset = 100.0,
    cursor: str | Unset = UNSET,
) -> Any | GetWorkflowsResponse200 | None:
    """Retrieve all workflows

     Retrieve all workflows from your instance.

    Args:
        active (bool | Unset):  Example: True.
        tags (str | Unset):  Example: test,production.
        name (str | Unset):  Example: My Workflow.
        project_id (str | Unset):  Example: VmwOO9HeTEj20kxM.
        exclude_pinned_data (bool | Unset):  Example: True.
        limit (float | Unset):  Default: 100.0. Example: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetWorkflowsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            active=active,
            tags=tags,
            name=name,
            project_id=project_id,
            exclude_pinned_data=exclude_pinned_data,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
