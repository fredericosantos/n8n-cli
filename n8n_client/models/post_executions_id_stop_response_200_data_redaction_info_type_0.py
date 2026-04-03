from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostExecutionsIdStopResponse200DataRedactionInfoType0")


@_attrs_define
class PostExecutionsIdStopResponse200DataRedactionInfoType0:
    """Present when execution data has been redacted.

    Attributes:
        is_redacted (bool | Unset): Whether the execution data was redacted.
        reason (str | Unset): The reason for redaction.
        can_reveal (bool | Unset): Whether the current user has permission to reveal the redacted data.
    """

    is_redacted: bool | Unset = UNSET
    reason: str | Unset = UNSET
    can_reveal: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_redacted = self.is_redacted

        reason = self.reason

        can_reveal = self.can_reveal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_redacted is not UNSET:
            field_dict["isRedacted"] = is_redacted
        if reason is not UNSET:
            field_dict["reason"] = reason
        if can_reveal is not UNSET:
            field_dict["canReveal"] = can_reveal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_redacted = d.pop("isRedacted", UNSET)

        reason = d.pop("reason", UNSET)

        can_reveal = d.pop("canReveal", UNSET)

        post_executions_id_stop_response_200_data_redaction_info_type_0 = cls(
            is_redacted=is_redacted,
            reason=reason,
            can_reveal=can_reveal,
        )

        post_executions_id_stop_response_200_data_redaction_info_type_0.additional_properties = d
        return post_executions_id_stop_response_200_data_redaction_info_type_0

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
