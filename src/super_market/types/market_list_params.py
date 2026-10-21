# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["MarketListParams"]


class MarketListParams(TypedDict, total=False):
    limit: int
    """Number of results per page (max 100)."""

    cursor: str
    """Pagination cursor from a previous response."""

    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """Optional tournament UUID for an explicit tournament context. Omit to use the API key's default scope: public global markets for an unbound key, or all accessible tournaments in the bound organization for an organization-bound key."""

    search: str
    """Case-insensitive title keyword search (at most 200 characters)."""

    sort: Literal["recent", "trending", "closing", "oldest"]
    """Sort order."""

    status: Literal["open", "closed", "settled", "resolved", "any"]
    """Filter by market lifecycle status. `resolved` is a deprecated alias for `settled`."""

    category: Literal[
        "sports-outcome",
        "election-outcome",
        "economic-indicator",
        "financial-product",
        "freeform",
        "existing-market",
        "corporate-earnings",
    ]
    """Filter by category slug. A market's category is the single contract type all of its legs share; markets mixing several types are composite and match no slug (use `is_composite`)."""

    ids: str
    """Comma-separated list of market IDs to fetch."""

    is_composite: Literal["true", "false"]
    """Filter composite (multi-condition) markets."""

    is_multi_outcome: Literal["true", "false"]
    """Filter multi-outcome markets (more than one exchange)."""
