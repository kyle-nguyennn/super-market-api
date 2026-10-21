# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["Group"]


class Group(BaseModel):
    id: str

    name: str

    slug: str

    description: Optional[str] = None

    organization_id: str = FieldInfo(alias="organizationId")

    organization_slug: Optional[str] = FieldInfo(alias="organizationSlug", default=None)

    member_count: int = FieldInfo(alias="memberCount")
    """Number of markets (or users) bound to this group."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)

    created_at: str = FieldInfo(alias="createdAt")

    updated_at: str = FieldInfo(alias="updatedAt")
