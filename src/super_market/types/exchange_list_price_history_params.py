# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExchangeListPriceHistoryParams"]


class ExchangeListPriceHistoryParams(TypedDict, total=False):
    tournament_id: Annotated[str, PropertyInfo(alias="tournamentId")]
    """When provided, returns candles computed from that accessible tournament's trades. Omit for the organization's default tournament with an organization-bound key or public-global history with an unbound key."""

    resolution: Literal["1m", "5m", "1h", "1d", "1w"]
    """Candle size. Buckets are aligned to UTC multiples of the resolution measured from the Unix epoch, so `1w` buckets begin on Thursdays."""

    from_: Annotated[str, PropertyInfo(alias="from")]
    """ISO-8601 start timestamp (inclusive). Floored down to the selected resolution's bucket boundary; the response `from` reflects the floored value. When omitted, returns the newest candles up to `to`."""

    to: str
    """ISO-8601 end timestamp (exclusive). When supplied, floored down to the selected resolution's bucket boundary. Defaults to now (not floored)."""

    limit: int
    """Maximum number of candles to return (max 1000). Selects the newest candles when `from` is omitted and the oldest candles forward from an explicit `from`."""
