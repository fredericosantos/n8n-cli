from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostWorkflowsBodyMetaType0")


@_attrs_define
class PostWorkflowsBodyMetaType0:
    """Workflow metadata such as template information

    Attributes:
        onboarding_id (str | Unset):
        template_id (str | Unset):
        instance_id (str | Unset):
        template_creds_setup_completed (bool | Unset):
    """

    onboarding_id: str | Unset = UNSET
    template_id: str | Unset = UNSET
    instance_id: str | Unset = UNSET
    template_creds_setup_completed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        onboarding_id = self.onboarding_id

        template_id = self.template_id

        instance_id = self.instance_id

        template_creds_setup_completed = self.template_creds_setup_completed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if onboarding_id is not UNSET:
            field_dict["onboardingId"] = onboarding_id
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if template_creds_setup_completed is not UNSET:
            field_dict["templateCredsSetupCompleted"] = template_creds_setup_completed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        onboarding_id = d.pop("onboardingId", UNSET)

        template_id = d.pop("templateId", UNSET)

        instance_id = d.pop("instanceId", UNSET)

        template_creds_setup_completed = d.pop("templateCredsSetupCompleted", UNSET)

        post_workflows_body_meta_type_0 = cls(
            onboarding_id=onboarding_id,
            template_id=template_id,
            instance_id=instance_id,
            template_creds_setup_completed=template_creds_setup_completed,
        )

        post_workflows_body_meta_type_0.additional_properties = d
        return post_workflows_body_meta_type_0

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
