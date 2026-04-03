from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credential_data import CredentialData


T = TypeVar("T", bound="Credential")


@_attrs_define
class Credential:
    """
    Attributes:
        name (str):  Example: Joe's Github Credentials.
        type_ (str):  Example: githubApi.
        data (CredentialData):  Example: {'accessToken': 'ada612vad6fa5df4adf5a5dsf4389adsf76da7s'}.
        id (str | Unset):  Example: R2DjclaysHbqn778.
        is_resolvable (bool | Unset): Whether this credential has resolvable fields
        created_at (datetime.datetime | Unset):  Example: 2022-04-29T11:02:29.842Z.
        updated_at (datetime.datetime | Unset):  Example: 2022-04-29T11:02:29.842Z.
    """

    name: str
    type_: str
    data: CredentialData
    id: str | Unset = UNSET
    is_resolvable: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        data = self.data.to_dict()

        id = self.id

        is_resolvable = self.is_resolvable

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "data": data,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if is_resolvable is not UNSET:
            field_dict["isResolvable"] = is_resolvable
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_data import CredentialData

        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        data = CredentialData.from_dict(d.pop("data"))

        id = d.pop("id", UNSET)

        is_resolvable = d.pop("isResolvable", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        credential = cls(
            name=name,
            type_=type_,
            data=data,
            id=id,
            is_resolvable=is_resolvable,
            created_at=created_at,
            updated_at=updated_at,
        )

        credential.additional_properties = d
        return credential

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
