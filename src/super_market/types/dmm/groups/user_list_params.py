# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    limit: int

    cursor: str

    search: str
    """Case-insensitive match on name or slug (at most 200 characters)."""

    organization_slug: Annotated[str, PropertyInfo(alias="organizationSlug")]
    """Platform-admin only; restrict to a specific org. Org-admin callers always see their own org."""
