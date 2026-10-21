# File generated from our OpenAPI spec by Scalar. See README.md for details.

from .market_read_context_descriptor import MarketReadContextDescriptor
from .combined_market_orderbook import CombinedMarketOrderbook

__all__ = ["MarketOrderbookContext"]


class MarketOrderbookContext(MarketReadContextDescriptor):
    orderbook: CombinedMarketOrderbook
