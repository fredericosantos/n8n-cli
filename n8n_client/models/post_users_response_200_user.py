from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUsersResponse200User")


@_attrs_define
class PostUsersResponse200User:
    """
    Attributes:
        id (str | Unset):
        email (str | Unset):
        invite_accept_url (str | Unset):
        email_sent (bool | Unset):
    """

    id: str | Unset = UNSET
    email: str | Unset = UNSET
    invite_accept_url: str | Unset = UNSET
    email_sent: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        invite_accept_url = self.invite_accept_url

        email_sent = self.email_sent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if invite_accept_url is not UNSET:
            field_dict["inviteAcceptUrl"] = invite_accept_url
        if email_sent is not UNSET:
            field_dict["emailSent"] = email_sent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        email = d.pop("email", UNSET)

        invite_accept_url = d.pop("inviteAcceptUrl", UNSET)

        email_sent = d.pop("emailSent", UNSET)

        post_users_response_200_user = cls(
            id=id,
            email=email,
            invite_accept_url=invite_accept_url,
            email_sent=email_sent,
        )

        post_users_response_200_user.additional_properties = d
        return post_users_response_200_user

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
