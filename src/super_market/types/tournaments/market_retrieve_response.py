# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

from .tournament_exchange_with_orderbook import TournamentExchangeWithOrderbook

__all__ = ["MarketRetrieveResponse", "Creator"]


class Creator(BaseModel):
    id: str

    username: Optional[str] = None


class MarketRetrieveResponse(BaseModel):
    id: str

    title: str

    status: Literal["open", "closed", "settled"]

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    settlement_date: Optional[str] = FieldInfo(alias="settlementDate", default=None)

    settled_with: Optional[str] = FieldInfo(alias="settledWith", default=None)

    settled_on: Optional[str] = FieldInfo(alias="settledOn", default=None)
    """Effective settlement timestamp in this tournament context. When the tournament has its own ruling, this is the tournament-scoped settlement timestamp."""

    categories: List[str]

    is_composite: bool = FieldInfo(alias="isComposite")

    is_multi_outcome: bool = FieldInfo(alias="isMultiOutcome")

    exchanges: List[TournamentExchangeWithOrderbook]

    creator: Optional[Creator] = None

    overround: Optional[float] = None
    """Sum of implied probabilities across all exchanges. Null when any exchange has no implied probability yet."""

    has_arbitrage_opportunity: bool = FieldInfo(alias="hasArbitrageOpportunity")
    """True when this is a mutually exclusive multi-outcome market whose best prices sum below 1 — a potential arbitrage, not a guaranteed one; false otherwise."""
