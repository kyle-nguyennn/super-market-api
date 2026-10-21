# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, Required, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MarketCreateParams"]


class MarketCreateParams(TypedDict, total=False):
    name: Required[str]

    slug: str
    """1-100 lowercase letters, digits, and hyphens, with no leading or trailing hyphen. Auto-generated from `name` when omitted."""

    description: Optional[str]

    organization_slug: Annotated[str, PropertyInfo(alias="organizationSlug")]
    """Required for platform-admin callers. Org-admin callers may omit it (their own org is used)."""
