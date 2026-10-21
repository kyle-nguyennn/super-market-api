# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .exchange_trade import ExchangeTrade

__all__ = ["ExchangeListTradesResponse", "Pagination", "Coverage"]


class Coverage(BaseModel):
    complete: bool
    """Always true because cursor pagination exposes the full requested trade history without window truncation."""

    projected_through_sequence: Optional[int] = FieldInfo(alias="projectedThroughSequence", default=None)
    """Latest trading-engine sequence reflected by the reporting projection, or null when no checkpoint exists."""


class Pagination(BaseModel):
    limit: int

    has_more: bool = FieldInfo(alias="hasMore")

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)


class ExchangeListTradesResponse(BaseModel):
    exchange_id: str = FieldInfo(alias="exchangeId")

    market_id: str = FieldInfo(alias="marketId")

    from_: str = FieldInfo(alias="from")

    to: str

    data: List[ExchangeTrade]

    pagination: Pagination

    coverage: Coverage
    """Reporting projection coverage metadata. Always present."""
