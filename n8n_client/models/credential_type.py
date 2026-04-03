from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialType")


@_attrs_define
class CredentialType:
    """
    Attributes:
        display_name (str | Unset):  Example: Email.
        name (str | Unset):  Example: email.
        type_ (str | Unset):  Example: string.
        default (str | Unset):  Example: string.
    """

    display_name: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    default: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        name = self.name

        type_ = self.type_

        default = self.default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        default = d.pop("default", UNSET)

        credential_type = cls(
            display_name=display_name,
            name=name,
            type_=type_,
            default=default,
        )

        credential_type.additional_properties = d
        return credential_type

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
