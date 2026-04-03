from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_users_response_200_user import PostUsersResponse200User


T = TypeVar("T", bound="PostUsersResponse200")


@_attrs_define
class PostUsersResponse200:
    """
    Attributes:
        user (PostUsersResponse200User | Unset):
        error (str | Unset):
    """

    user: PostUsersResponse200User | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_users_response_200_user import PostUsersResponse200User

        d = dict(src_dict)
        _user = d.pop("user", UNSET)
        user: PostUsersResponse200User | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PostUsersResponse200User.from_dict(_user)

        error = d.pop("error", UNSET)

        post_users_response_200 = cls(
            user=user,
            error=error,
        )

        post_users_response_200.additional_properties = d
        return post_users_response_200

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
