from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_credential_body_data import UpdateCredentialBodyData


T = TypeVar("T", bound="UpdateCredentialBody")


@_attrs_define
class UpdateCredentialBody:
    """
    Attributes:
        name (str | Unset): The name of the credential Example: Updated Credential Name.
        type_ (str | Unset): The credential type. If changing type, data must also be provided. Example: githubApi.
        data (UpdateCredentialBodyData | Unset): The credential data. Required when changing credential type. Example:
            {'accessToken': 'new_token_value'}.
        is_global (bool | Unset): Whether this credential is available globally
        is_resolvable (bool | Unset): Whether this credential has resolvable fields
        is_partial_data (bool | Unset): If true, unredacts and merges existing credential data with the provided data.
            If false, replaces the entire data object. Default: False.
    """

    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    data: UpdateCredentialBodyData | Unset = UNSET
    is_global: bool | Unset = UNSET
    is_resolvable: bool | Unset = UNSET
    is_partial_data: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        is_global = self.is_global

        is_resolvable = self.is_resolvable

        is_partial_data = self.is_partial_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if data is not UNSET:
            field_dict["data"] = data
        if is_global is not UNSET:
            field_dict["isGlobal"] = is_global
        if is_resolvable is not UNSET:
            field_dict["isResolvable"] = is_resolvable
        if is_partial_data is not UNSET:
            field_dict["isPartialData"] = is_partial_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_credential_body_data import UpdateCredentialBodyData

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        _data = d.pop("data", UNSET)
        data: UpdateCredentialBodyData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = UpdateCredentialBodyData.from_dict(_data)

        is_global = d.pop("isGlobal", UNSET)

        is_resolvable = d.pop("isResolvable", UNSET)

        is_partial_data = d.pop("isPartialData", UNSET)

        update_credential_body = cls(
            name=name,
            type_=type_,
            data=data,
            is_global=is_global,
            is_resolvable=is_resolvable,
            is_partial_data=is_partial_data,
        )

        update_credential_body.additional_properties = d
        return update_credential_body

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
