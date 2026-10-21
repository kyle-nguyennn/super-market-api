# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PortfolioListTransactionsParams"]


class PortfolioListTransactionsParams(TypedDict, total=False):
    limit: int
    """Results per page (max 200)."""

    cursor: str
    """Opaque pagination cursor from a previous response."""

    type: str
    """Comma-separated event type filter. Valid values: trade, settlement, deposit, fee, market_creation."""
