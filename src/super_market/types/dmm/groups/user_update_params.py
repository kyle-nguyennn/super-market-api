# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    name: str

    slug: str
    """1-100 lowercase letters, digits, and hyphens, with no leading or trailing hyphen."""

    description: Optional[str]
