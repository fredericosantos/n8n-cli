from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.credential_shared_item import CredentialSharedItem


T = TypeVar("T", bound="CredentialListItem")


@_attrs_define
class CredentialListItem:
    """
    Attributes:
        id (str):  Example: vHxaz5UaCghVYl9C.
        name (str):  Example: John's Github account.
        type_ (str):  Example: githubApi.
        created_at (datetime.datetime):  Example: 2022-04-29T11:02:29.842Z.
        updated_at (datetime.datetime):  Example: 2022-04-29T11:02:29.842Z.
        shared (list[CredentialSharedItem]): Shared entries (project id, name, role, createdAt, updatedAt) from the
            credential's shared relation
    """

    id: str
    name: str
    type_: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    shared: list[CredentialSharedItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        shared = []
        for shared_item_data in self.shared:
            shared_item = shared_item_data.to_dict()
            shared.append(shared_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type_,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "shared": shared,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_shared_item import CredentialSharedItem

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        type_ = d.pop("type")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        shared = []
        _shared = d.pop("shared")
        for shared_item_data in _shared:
            shared_item = CredentialSharedItem.from_dict(shared_item_data)

            shared.append(shared_item)

        credential_list_item = cls(
            id=id,
            name=name,
            type_=type_,
            created_at=created_at,
            updated_at=updated_at,
            shared=shared,
        )

        credential_list_item.additional_properties = d
        return credential_list_item

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
