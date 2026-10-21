# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExchangeListParams"]


class ExchangeListParams(TypedDict, total=False):
    market_id: Annotated[str, PropertyInfo(alias="marketId")]
    """Filter to all exchanges in a single market. Mutually exclusive with `ids`."""

    ids: str
    """Comma-separated list of exchange IDs (max 100). Mutually exclusive with `marketId`. Useful for bulk-refreshing a watchlist in one request."""

    limit: int
    """Results per page (max 200)."""

    cursor: str
    """Pagination cursor from a previous response."""

    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """Optional explicit tournament UUID. Omit for the API key's public or organization-wide default scope."""
