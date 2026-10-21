# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExchangeListTradesParams"]


class ExchangeListTradesParams(TypedDict, total=False):
    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """When provided, returns trades from that accessible tournament. Omit for the organization's default tournament with an organization-bound key or public-global trades with an unbound key."""

    from_: Annotated[str, PropertyInfo(alias="from")]
    """ISO-8601 start timestamp (inclusive). Defaults to the beginning of exchange history."""

    to: str
    """ISO-8601 end timestamp (exclusive). Defaults to now."""

    limit: int
    """Trades per page (max 200)."""

    cursor: str
    """Opaque pagination cursor from a previous response."""
