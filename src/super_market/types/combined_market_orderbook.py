# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

from .combined_orderbook_exchange import CombinedOrderbookExchange

__all__ = ["CombinedMarketOrderbook"]


class CombinedMarketOrderbook(BaseModel):
    exchanges: List[CombinedOrderbookExchange]

    overround: Optional[float] = None
    """Sum of implied probabilities across all outcomes. Null when any outcome has no implied probability."""

    has_arbitrage_opportunity: bool = FieldInfo(alias="hasArbitrageOpportunity")
    """True when this is a mutually exclusive multi-outcome market whose best prices sum below 1 — a potential arbitrage, not a guaranteed one; false otherwise."""
