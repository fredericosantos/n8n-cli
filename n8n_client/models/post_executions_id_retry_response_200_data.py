from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_executions_id_retry_response_200_data_redaction_info_type_0 import (
        PostExecutionsIdRetryResponse200DataRedactionInfoType0,
    )


T = TypeVar("T", bound="PostExecutionsIdRetryResponse200Data")


@_attrs_define
class PostExecutionsIdRetryResponse200Data:
    """Detailed execution data. Only included when `includeData` is `true`.

    Attributes:
        redaction_info (None | PostExecutionsIdRetryResponse200DataRedactionInfoType0 | Unset): Present when execution
            data has been redacted.
    """

    redaction_info: None | PostExecutionsIdRetryResponse200DataRedactionInfoType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.post_executions_id_retry_response_200_data_redaction_info_type_0 import (
            PostExecutionsIdRetryResponse200DataRedactionInfoType0,
        )

        redaction_info: dict[str, Any] | None | Unset
        if isinstance(self.redaction_info, Unset):
            redaction_info = UNSET
        elif isinstance(self.redaction_info, PostExecutionsIdRetryResponse200DataRedactionInfoType0):
            redaction_info = self.redaction_info.to_dict()
        else:
            redaction_info = self.redaction_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if redaction_info is not UNSET:
            field_dict["redactionInfo"] = redaction_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_executions_id_retry_response_200_data_redaction_info_type_0 import (
            PostExecutionsIdRetryResponse200DataRedactionInfoType0,
        )

        d = dict(src_dict)

        def _parse_redaction_info(
            data: object,
        ) -> None | PostExecutionsIdRetryResponse200DataRedactionInfoType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                redaction_info_type_0 = PostExecutionsIdRetryResponse200DataRedactionInfoType0.from_dict(data)

                return redaction_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PostExecutionsIdRetryResponse200DataRedactionInfoType0 | Unset, data)

        redaction_info = _parse_redaction_info(d.pop("redactionInfo", UNSET))

        post_executions_id_retry_response_200_data = cls(
            redaction_info=redaction_info,
        )

        post_executions_id_retry_response_200_data.additional_properties = d
        return post_executions_id_retry_response_200_data

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
