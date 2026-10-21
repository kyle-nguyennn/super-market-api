# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PortfolioListSettlementsParams"]


class PortfolioListSettlementsParams(TypedDict, total=False):
    limit: int
    """Results per page (max 200)."""

    cursor: str
    """Opaque pagination cursor from a previous response."""

    type: str
    """Comma-separated settlement type filter. Valid values: win, loss, refund, correction."""

    market_id: Annotated[str, PropertyInfo(alias="marketId")]
    """Restrict to settlements on a single market."""
