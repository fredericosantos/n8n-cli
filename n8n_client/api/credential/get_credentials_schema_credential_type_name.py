from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_credentials_schema_credential_type_name_response_200 import (
    GetCredentialsSchemaCredentialTypeNameResponse200,
)
from ...types import Response


def _get_kwargs(
    credential_type_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/credentials/schema/{credential_type_name}".format(
            credential_type_name=quote(str(credential_type_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetCredentialsSchemaCredentialTypeNameResponse200 | None:
    if response.status_code == 200:
        response_200 = GetCredentialsSchemaCredentialTypeNameResponse200.from_dict(response.json())

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
) -> Response[Any | GetCredentialsSchemaCredentialTypeNameResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    credential_type_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetCredentialsSchemaCredentialTypeNameResponse200]:
    """Show credential data schema

    Args:
        credential_type_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCredentialsSchemaCredentialTypeNameResponse200]
    """

    kwargs = _get_kwargs(
        credential_type_name=credential_type_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    credential_type_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetCredentialsSchemaCredentialTypeNameResponse200 | None:
    """Show credential data schema

    Args:
        credential_type_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCredentialsSchemaCredentialTypeNameResponse200
    """

    return sync_detailed(
        credential_type_name=credential_type_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    credential_type_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetCredentialsSchemaCredentialTypeNameResponse200]:
    """Show credential data schema

    Args:
        credential_type_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCredentialsSchemaCredentialTypeNameResponse200]
    """

    kwargs = _get_kwargs(
        credential_type_name=credential_type_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    credential_type_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetCredentialsSchemaCredentialTypeNameResponse200 | None:
    """Show credential data schema

    Args:
        credential_type_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCredentialsSchemaCredentialTypeNameResponse200
    """

    return (
        await asyncio_detailed(
            credential_type_name=credential_type_name,
            client=client,
        )
    ).parsed
