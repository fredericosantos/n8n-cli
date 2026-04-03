from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_community_packages_name_body import PatchCommunityPackagesNameBody
from ...models.patch_community_packages_name_response_200 import PatchCommunityPackagesNameResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    body: PatchCommunityPackagesNameBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/community-packages/{name}".format(
            name=quote(str(name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PatchCommunityPackagesNameResponse200 | None:
    if response.status_code == 200:
        response_200 = PatchCommunityPackagesNameResponse200.from_dict(response.json())

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
) -> Response[Any | PatchCommunityPackagesNameResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    body: PatchCommunityPackagesNameBody | Unset = UNSET,
) -> Response[Any | PatchCommunityPackagesNameResponse200]:
    """Update a community package

     Update an installed community package to a new version.

    Args:
        name (str):
        body (PatchCommunityPackagesNameBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchCommunityPackagesNameResponse200]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient,
    body: PatchCommunityPackagesNameBody | Unset = UNSET,
) -> Any | PatchCommunityPackagesNameResponse200 | None:
    """Update a community package

     Update an installed community package to a new version.

    Args:
        name (str):
        body (PatchCommunityPackagesNameBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchCommunityPackagesNameResponse200
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    body: PatchCommunityPackagesNameBody | Unset = UNSET,
) -> Response[Any | PatchCommunityPackagesNameResponse200]:
    """Update a community package

     Update an installed community package to a new version.

    Args:
        name (str):
        body (PatchCommunityPackagesNameBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchCommunityPackagesNameResponse200]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    body: PatchCommunityPackagesNameBody | Unset = UNSET,
) -> Any | PatchCommunityPackagesNameResponse200 | None:
    """Update a community package

     Update an installed community package to a new version.

    Args:
        name (str):
        body (PatchCommunityPackagesNameBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchCommunityPackagesNameResponse200
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
        )
    ).parsed
