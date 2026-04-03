from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_audit_body_additional_options import PostAuditBodyAdditionalOptions


T = TypeVar("T", bound="PostAuditBody")


@_attrs_define
class PostAuditBody:
    """
    Attributes:
        additional_options (PostAuditBodyAdditionalOptions | Unset):
    """

    additional_options: PostAuditBodyAdditionalOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_options, Unset):
            additional_options = self.additional_options.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_options is not UNSET:
            field_dict["additionalOptions"] = additional_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_audit_body_additional_options import PostAuditBodyAdditionalOptions

        d = dict(src_dict)
        _additional_options = d.pop("additionalOptions", UNSET)
        additional_options: PostAuditBodyAdditionalOptions | Unset
        if isinstance(_additional_options, Unset):
            additional_options = UNSET
        else:
            additional_options = PostAuditBodyAdditionalOptions.from_dict(_additional_options)

        post_audit_body = cls(
            additional_options=additional_options,
        )

        post_audit_body.additional_properties = d
        return post_audit_body

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
