# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PortfolioListFillsParams"]


class PortfolioListFillsParams(TypedDict, total=False):
    exchange_id: Annotated[str, PropertyInfo(alias="exchangeId")]
    """Filter to a specific exchange."""

    market_id: Annotated[str, PropertyInfo(alias="marketId")]
    """Filter to all exchanges in a market."""

    limit: int
    """Results per page (max 200)."""

    cursor: str
    """Pagination cursor from a previous response."""

    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """Return fills from one accessible tournament. Omit to use the organization's default tournament for an organization-bound key or the public global context for an unbound key."""
