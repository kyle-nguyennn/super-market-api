# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DmmListFailedAutosettlementParams"]


class DmmListFailedAutosettlementParams(TypedDict, total=False):
    limit: int
    """Page size (default 50, max 200)."""

    offset: Optional[int]
